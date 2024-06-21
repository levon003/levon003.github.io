---
layout: post
title:  "Multi-threading for CPU inference in PyTorch"
date:   2024-06-21
tags: code short
excerpt: "Exploring the performance characteristics of multi-threading for CPU inference with PyTorch."
image: /images/cpu_threading_torchscript_inference.svg
---

["CPU threading and TorchScript inference"](https://pytorch.org/docs/stable/notes/cpu_threading_torchscript_inference.html)


![Flowchart showing the Application Thread Pool and an inter-op thread pool.](/images/cpu_threading_torchscript_inference.svg)
*Inter- and intra-op parallelism with PyTorch. Reproduced from the [docs](https://pytorch.org/docs/stable/notes/cpu_threading_torchscript_inference.html) ([source](https://github.com/pytorch/pytorch/blob/main/docs/source/notes/cpu_threading_torchscript_inference.svg)).*

I estimated timing on an Apple M2 Pro, with 10 CPU cores (6 "performance" and 4 "efficiency") and 16GB memory.

Both my Apple M2 Pro and AWS Fargate systems use an OpenMP backend.


## Multi-processing vs multi-threading

StackOverflow has a [useful answer](https://stackoverflow.com/a/19518207/4146714) explaining the distinction between threads and processes.