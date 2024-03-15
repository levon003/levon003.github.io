---
layout: post
title:  "Research paper: \"Red-Teaming for Generative AI: Silver Bullet or Security Theater?\""
date:   2024-03-12
tags: research short
excerpt: "A 2024 position paper on red-teaming from Michael Feffer and others at CMU."
image: images/redteam-silver-bullet-paper.png
---

["Red-Teaming for Generative AI: Silver Bullet or Security Theater?"](https://arxiv.org/abs/2401.15897) is a January 2024 pre-print written by Michael Feffer, Anusha Sinha, Zachary Lipton, and Hoda Heidari. It caught my eye because of Zachary Lipton's name, who not only has a great first name but also wrote two of my favorite research papers (["The Mythos of Model Interpretability"](https://arxiv.org/abs/1606.03490) and ["Detecting and Correcting for Label Shift with Black Box Predictors"](https://arxiv.org/abs/1802.03916)).

They start with a provocation, in the form of serious questions:

 1. What types of undesirable behaviors, limitations, and risks can or should be effectively caught and mitigated through red-teaming exercises? 
 2. How should the activity be structured to maximize the likelihood of finding such flaws and vulnerabilities?
 3. How should the risks identified through red-teaming be documented, reported, and managed? 
 4. Is red-teaming on its own sufficient for assessing and managing the safety, security, and trustworthiness of AI?
 5. In short, is red-teaming the stuff of policy or is it the stuff of _vibes_—a vague practice better suited to rallying than to rule-making?

It will not surprise you to learn that different researchers answer the first four questions very differently; red-teaming exercises vary in their definition, scope, object of evaluation, model development lifecycle, assessed risks, evaluation criteria, evaluators, and outputs.
"Our analysis reveals the lack of consensus around the scope, structure, and assessment criteria for AI red-teaming."

