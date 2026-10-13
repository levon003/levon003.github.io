---
layout: post
title: "Decision models"
tags: llm ml short
excerpt: "Decision models offer highly-constrained structured outputs, fast."
---

Decision models are a new paradigm for producing schema-compliant responses with large language models by training a small "head" on an existing LLM.

Here's a quick summary image:

![Structured outputs vs. decision models](/images/decision-models/structured-outputs-vs-decision-models.svg)
*Generated with the assistance of Claude Opus 5.5.*

The pros of decision models:
- Faster inference
- Calibrated probabilities

The cons of decision models:
- Restricted schema; no open-ended responses
- No thinking

I'm most excited by decision models as a middle ground between expensive/slow LLM calls and manually-trained classifiers. 

Consider a progression:
- Start extracting some semi-structured information from some process' outputs using an LLM
- Once the most common cases are known, replace most or all LLM calls with decision model calls
- Once data has been collected and audited – by focusing on the most uncertain cases, for example – replace most or all decision model calls with a fast classifier

## Further reading

* Simon Willison, ["Jev introduces a new shape of LLM—System One, aka Decision Models"](https://simonwillison.net/2026/Sep/21/jev/)
* Sean Goedecke, ["System One models like Jev can train their own replacements"](https://www.seangoedecke.com/system-one-models-can-train-their-own-replacements/)
* Cloudflare, ["Introducing Clef: our open-source decision models, and new RL fine-tuning platform"](https://blog.cloudflare.com/clef-decision-models/)
* vLLM, [Decision 3.0](https://huggingface.co/vllm-sr/d3)
