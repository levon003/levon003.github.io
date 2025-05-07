---
layout: post
title:  "Using Docker with pytest for integration testing"
tags: code python testing docker pytest sql short
excerpt: "A few packages using Docker with Python's pytest for integration and functional testing."
---

Writing integration and functional tests that depend on databases is important but not easy. 

Many teams run integration tests against a shared development or staging database, although that can create weird dependencies on the current state of the database or cause hard-to-diagnose test interleaving bugs. 

A common alternative is to run a containerized database for each developer, either locally or on a testing cluster. The CI process can share the same process but use a dedicated database.

Intuitively, that means starting a Docker container running Postgres, MySQL, etc. and connecting to the container during test execution.

I'm most interested in testing Python applications, especially using [`pytest`](https://docs.pytest.org/en/stable/), which I prefer over [`unittest`](https://docs.python.org/3/library/unittest.html).

How should you manage your Docker containers? You could just use the [Docker Python SDK](https://docker-py.readthedocs.io/en/stable/).
Lars Kellogg-Stedman describes that approach in his blog post ["Managing containers with Pytest fixtures"](https://blog.oddbit.com/post/2023-07-15-pytest-and-containers/).

If you don't want to use the Docker SDK directly, a number of libraries have been built specifically to manage Docker containers during testing of Python modules:

1. [testcontainers-python](https://testcontainers-python.readthedocs.io/en/latest/)
2. [pytest-docker](https://github.com/avast/pytest-docker)
3. [pytest-docker-tools](https://github.com/Jc2k/pytest-docker-tools)

pytest-docker implements an approach similar to Kellogg-Stedman's blog post, but specifically designed for `docker compose`.

testcontainers-python looks the most mature, and does integrate with Docker Compose as well.
In an environment that already defines a `compose.yaml`, that may be particularly appealing.

## testcontainers-python Example

I ended up using testcontainers-python for a recent project. 
I would recommend using this in situations where I felt the urge to write my own subprocess calls to invoke Docker Compose; instead, let testcontainers-python handle that.

First, let's define the services we need in `tests/integration/compose.yaml`:

```yaml
x-common-variables: &sql-common-variables
  MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
  MYSQL_DATABASE: ${MYSQL_DATABASE}

services:
  sql:
    platform: linux/amd64
    image: mysql:5.9
    environment:
      <<: *sql-common-variables
      MYSQL_ROOT_HOST: '%'
    healthcheck:
      test: [ "CMD", "mysqladmin" ,"ping", "-h", "localhost" ]
      interval: 1s
      timeout: 15s
      retries: 12
      start_period: 5s
    ports:
      - '3306:3306'
  db_creator:
    image: create-database:latest
    pull_policy: never
    build:
      context: ../..
      dockerfile: tests/integration/db_creator.dockerfile
    environment:
      <<: *sql-common-variables
      MYSQL_HOST: 'sql'
      MYSQL_USER: 'root'
    depends_on:
      sql:
        condition: service_healthy
  db_ready:
    image: alpine
    command: echo
    depends_on:
      db_creator:
        condition: service_completed_successfully
```

I won't provide `tests/integration/db_creator.dockerfile` in full, but it just invokes a shell script:
```dockerfile
RUN apk add --no-cache mysql-client
ENTRYPOINT ["/entrypoint.sh"]
```

`entrypoint.sh` runs a SQL script to populate the database with the appropriate schema. If you were using a Python-based migration or schema management tool, this wouldn't be necessary.
In my context, it was convenient to create a test database setup that was language-agnostic.

```bash
until mysqladmin ping -h "$MYSQL_HOST" -u $MYSQL_USER -p$MYSQL_ROOT_PASSWORD --silent; do
  echo "Waiting on MySQL to be ready."
  sleep 1
done
mysql --protocol=tcp -h $MYSQL_HOST -u $MYSQL_USER -p$MYSQL_ROOT_PASSWORD $MYSQL_DATABASE < some_sql_script.sql
```

Note that the `mysqladmin ping` check is a good idea even while using a Docker Compose healthcheck; the external healthcheck may start returning "healthy" before the database server container has completed all initialization steps e.g. before the specific database name has been created.

The needed environment variables can be defined in a `.env`. Here's `tests/integration/test.env`:

```
MYSQL_DATABASE="db_name"
MYSQL_ROOT_PASSWORD="inttest"
MYSQL_DATABASE_URL="mysql+pymysql://root:inttest@localhost:3307/db_name"
```

Using Docker Compose, you could create the test database like this:

```bash
docker compose -f tests/integration/compose.yaml --env-file tests/integration/test.env up --build sql db_creator db_ready
```

But we want to use testcontainers-python to do that instead, so we don't need to run two commands during integration testing.

In a Pytest `conftest.py`, we can define a fixture that provides access to the database:

```python
import testcontainers.compose


@pytest.fixture(scope="session")
def docker_compose_filepath(pytestconfig):
    return pytestconfig.rootpath / "tests" / "integration" / "compose.yaml"


@pytest.fixture(scope="session")
def docker_mysql_db(docker_compose_filepath, pytestconfig):
    env_file = pytestconfig.rootpath / "tests" / "integration" / "test.env"
    with testcontainers.compose.DockerCompose(
        str(pytestconfig.rootpath),
        compose_file_name=str(docker_compose_filepath),
        build=True,
        wait=False,  # note: using --wait will result in non-zero status codes
        keep_volumes=False,
        env_file=str(env_file),
        services=["sql", "db_creator", "db_ready"],
    ) as compose:
        settings.set_dotenv_path(str(env_file))
        settings.set_current_command("integration-test")
        settings.load_settings(override_env=True)
        yield compose
```

Now, any test definition that uses the `docker_mysql_db` fixture will execute while the database container is running and available at MYSQL_DATABASE_URL.

Note that the same database will be shared for the full testing session, so you'll need to be careful to avoid writing tests that expect the presence or absence of data that they themselves do not ensure during test setup.

I'm finding this to be a perfectly reasonable approach to integration testing; still local to my dev machine and fast to set up, but more appropriate than using an SQLite or other mocked database connection.

Depending on your setup, you may not need a separate Docker Compose file; if you have an existing set of service definitions, you could use Docker Compose profiles to flag only some services as being required for integration testing.
