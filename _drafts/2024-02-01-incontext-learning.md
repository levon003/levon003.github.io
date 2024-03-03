---
layout: post
title:  In-context Learning
date:   2023-11-27
tags: research short
excerpt: Why do prompting techniques based on in-context learning help?
---
Samuel Müller has recently been pushing the idea that in-context learning (including RAG, memory augmentation, etc.) “works” because it attempts to approximate the posterior predictive distribution (https://arxiv.org/abs/2112.10510)

https://twitter.com/SamuelMullr/status/1722630968740331612


https://arxiv.org/abs/2210.14986
"In-context prompting can mitigate the fact that some models are better at natural prompts and others better at structured prompts by improving performance on the type of prompt the model struggles with zero-shot"
From the sharp rise in performance observed for the k = 0 to k = 1
result (from 60.2% to 72.8%) we hypothesise that the k-shot in-context examples in this task do not necessarily teach the model pragmatics in-context, but prime the model for the task format." Based on some experiments with randomizing the labels provided with in-context examples, they conclude that "for base models the content of the in-context prompt seems important, whereas for [example-level instruction-fine-tuned] models the in-context examples mainly serve as a primer for the task structure."

Laura Ruis says [on Twitter](https://twitter.com/LauraRuis/status/1732402559724208570) that, for instruction-fine-tuned models, "although few-shot prompting helps performance, it probably just helps formatting and doesn't teach the models pragmatics."

https://arxiv.org/abs/2304.03843
As [summarized](https://nlpnewsletter.substack.com/p/neurips-2023-primer) by Sebastian Ruder: "They find that chain-of-thought reasoning is only useful when the training data is locally structured. In other words, when examples are about closely connected topics as is common in natural language. They find that chain-of-thought reasoning is helpful because it incrementally chains local statistical dependencies that are frequently observed in training."

https://arxiv.org/abs/2301.11916
Ruder's summary: "examples that are probable based on a latent concept of a task are useful demonstrations"

In ["The Expressive Power of Transformers with Chain of Thought"](https://arxiv.org/abs/2310.07923), William Merrill and Ashish Sabharwal.
Chain of thought (and similar prompting approaches that produce a "scratchpad" of intermediate results) enables transformers to solve sequential reasoning problems that they otherwise are incapable of.

In ["The Power of Noise: Redefining Retrieval for RAG Systems"](https://arxiv.org/abs/2401.14887), Cuconasu et al. found that RAG improves accuracy even when documents are randomly selected. To my mind, that's more evidence toward the "distribution" theory: any vaguely coherent text provides information about the appropriate output distribution.