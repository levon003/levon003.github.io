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
