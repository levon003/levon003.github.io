---
layout: post
title:  "Prompting large language models"
tags: llm research short
excerpt: "Resources for prompt engineering with large language models."
---

_Prompt engineering_ refers to tweaking a pre-written _prompt_ - the text context provided to a large language model (LLM) - in order to improve LLM response quality.
I've used prompt engineering [to improve student math Q&A]({% post_url 2024-02-02-rag-for-math-qa %}), for example.

This post rounds up a few resources related to prompt engineering.

Resources:
 - LLM Prompt Tuning Playbook by Varun Godbole, Ellie Pavlick: <https://github.com/varungodbole/prompt-tuning-playbook>
 - From Ethan Mollick:
   - "Innovation through prompting": <https://www.oneusefulthing.org/p/innovation-through-prompting>
   - "Prompts for Instructors": <https://www.moreusefulthings.com/instructor-prompts>
   - "Stop Writing All Your AI Prompts from Scratch": <https://hbsp.harvard.edu/inspiring-minds/an-ai-prompting-template-for-teaching-tasks>
 - There are approaches beyond writing and refining a single prompt that we might use in the future: ["You probably don't know how to do Prompt Engineering"](https://gist.github.com/Hellisotherpeople/45c619ee22aac6865ca4bb328eb58faf) by Allen Roush
 - A useful overview and catalog of terms used to refer to various flavors of prompt engineering: <https://www.promptingguide.ai/>
 
Example prompts:
 - LangIndex prompts: <https://github.com/run-llama/llama_index/blob/main/llama-index-core/llama_index/core/prompts/default_prompts.py>
