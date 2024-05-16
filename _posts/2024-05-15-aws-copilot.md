---
layout: post
title:  "AWS Copilot CLI makes it easy to run containerized ETL jobs"
date:   2024-05-15
tags: code aws short
excerpt: "I missed the release of AWS Copilot CLI back in 2020. It's a useful and opinionated tool."
---

Apparently, AWS [released the "AWS Copilot CLI"](https://aws.amazon.com/blogs/containers/introducing-aws-copilot/) back in July 2020 to make deploying containerized applications more straightforward. (Specifically, those running under the ECS service.)

I created a quick [demonstration repository](https://github.com/levon003/aws-etl-job), showing the use of AWS Copilot for creating ETL jobs on AWS Fargate.

I found this blog post from the AWS developer relations team to be useful: <https://containersonaws.com/pattern/scheduled-cron-job-container-ecs-copilot>

I created a new configuration:
```bash
copilot init
```

If I want to re-deploy (because I've made changes to the Dockerfile, manifests, or code):

```bash
copilot deploy
```

If I want to invoke the job manually, rather than relying on the schedule:

```bash
copilot job run 
```

To view the most recent logs:

```bash
copilot job logs
```

For example, I can confirm that my demo script executed successfully:

```bash
% copilot job logs --env aws-etl-job --name aws-etl-job
copilot/aws-etl-job/6f8d4 Hello world!
```

View all of this [on GitHub](https://github.com/levon003/aws-etl-job).
