---
layout: post
title:  "Transcribing Zoom recordings with WhisperX on AWS Fargate"
date:   2024-05-23
tags: code short
excerpt: "A Dockerized transcription and diarization pipeline using WhisperX."
---

I [recently wrote]({% post_url 2024-05-15-aws-copilot %}) about AWS Copilot, a CLI tool that makes it easy to deploy Dockerized applications on AWS.

I used AWS Copilot to run CPU-only WhisperX on AWS Fargate: <https://github.com/DigitalHarborFoundation/whisperx-on-aws-fargate>

Take a look at the repository to learn more, but the basic point is that it's straightforward to Dockerize complex ML models and deploy them in ETL jobs using Copilot.
I used the [WhisperX](https://github.com/m-bain/whisperX) library to do automatic speech recognition and speaker diarization, with the intended use case of batch-transcribing Zoom recordings.

If you're using AWS already and interested in transcribing batches of audio or video files, take a look.
