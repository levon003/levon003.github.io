---
layout: post
title:  Connecting to GCP Cloud SQL from a local Docker container 
date:   2024-01-25
tags: code short
excerpt: Connecting to GCP Cloud SQL from a local Docker container using `host.docker.internal`
---

As a developer, you might be using [`cloud-sql-proxy`](https://cloud.google.com/sql/docs/mysql/sql-proxy) during development to connect to a Cloud SQL instance, e.g. to run local integration tests.

Here's what that workflow might look like:

 1. Run the Cloud SQL proxy: `cloud-sql-proxy {project-id}:{region}:{cloud-sql-instance-id}`
 2. Connect using a database URL that points at localhost, e.g. `"DATABASE_URL="postgres://{username}:{password}@localhost:5432/{db-name}"`

That works great for local testing, but what if you want to test your application in a local Docker container?

For that, you can use a [workaround implemented in Docker Desktop](https://docs.docker.com/desktop/networking/#use-cases-and-workarounds-for-all-platforms) for connecting to a service running on the Docker host from within the container: instead of `localhost`, refer to `gateway.docker.internal` instead.

Here's a revised flow for connecting to a Cloud SQL instance from within a Docker container:

 1. Run the Cloud SQL proxy on the host: `cloud-sql-proxy {project-id}:{region}:{cloud-sql-instance-id}`
 2. Run the Docker container, exposing the relevant proxy port e.g. `docker run -p 5432:5432`. (Exposing the port may not be necessary...)
 2. From within the container, use a database URL that points at the internal gateway, e.g. `"DATABASE_URL="postgres://{username}:{password}@gateway.docker.internal:5432/{db-name}"`

I was not aware of this Docker feature: thanks to [this StackOverflow answer](https://stackoverflow.com/a/75176302/4146714) for suggesting it.
