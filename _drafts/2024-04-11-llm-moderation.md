---
layout: post
title:  "Dashboards to monitor student's open-ended conversations"
date:   2024-04-11
tags: research safety llms
excerpt: Ensuring student safety with monitoring dashboards for students' chats with LLMs.
---

OpenAI provides a [moderation API](https://platform.openai.com/docs/guides/moderation)

| Category               | Description                                                                                                                     |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| hate                   | Content that expresses, incites, or promotes hate based on race, gender, ethnicity, religion, nationality, sexual orientation, disability status, or caste. Hateful content aimed at non-protected groups (e.g., chess players) is harassment.                    |
| hate/threatening       | Hateful content that also includes violence or serious harm towards the targeted group based on race, gender, ethnicity, religion, nationality, sexual orientation, disability status, or caste.                                                                   |
| harassment             | Content that expresses, incites, or promotes harassing language towards any target.                                             |
| harassment/threatening | Harassment content that also includes violence or serious harm towards any target.                                               |
| self-harm              | Content that promotes, encourages, or depicts acts of self-harm, such as suicide, cutting, and eating disorders.                 |
| self-harm/intent       | Content where the speaker expresses that they are engaging or intend to engage in acts of self-harm, such as suicide, cutting, and eating disorders.                                                                                                           |
| self-harm/instructions | Content that encourages performing acts of self-harm, such as suicide, cutting, and eating disorders, or that gives instructions or advice on how to commit such acts.                                                                                           |
| sexual                 | Content meant to arouse sexual excitement, such as the description of sexual activity, or that promotes sexual services (excluding sex education and wellness).                                                                                                    |
| sexual/minors          | Sexual content that includes an individual who is under 18 years old.                                                           |
| violence               | Content that depicts death, violence, or physical injury.                                                                       |
| violence/graphic       | Content that depicts death, violence, or physical injury in graphic detail.                                                     |

According to the documentation, the scores returned by the API indicate "the model's confidence that the input violates OpenAI's policy for the category. The value is between 0 and 1, where higher values denote higher confidence. The scores should not be interpreted as probabilities."

Generative AI Moderation Report

![](/images/llm-safety/moderation_report_header.png)

OpenAI Moderation Score Summary

![](/images/llm-safety/moderation_report_openai_score_summary.png)

Score histogram

![](/images/llm-safety/moderation_report_harassment_histogram.png)

In addition, we show the three highest-scoring messages.

One of the main use cases for this dashboard is to determine if the thresholds we're using is appropriate.
To assist in making that assessment, we also show the six messages closest to the moderation threshold: three that were flagged as just over the threshold and three that were unflagged as just below the threshold.
These messages provide a quick-to-evaluate and intuitive sense of whether this threshold is producing lots of false negatives or false positives. 

OpenAI specifically expects you to do recalibration if you threshold on the raw scores, due to changes in the underlying model. 