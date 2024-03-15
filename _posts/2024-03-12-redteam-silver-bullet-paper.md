---
layout: post
title:  "Research paper: \"Red-Teaming for Generative AI: Silver Bullet or Security Theater?\""
date:   2024-03-12
tags: research short
excerpt: "A 2024 position paper on red-teaming from Michael Feffer and others at CMU."
image: images/redteam-silver-bullet-paper.png
---

["Red-Teaming for Generative AI: Silver Bullet or Security Theater?"](https://arxiv.org/abs/2401.15897) is a January 2024 pre-print written by Michael Feffer, Anusha Sinha, Zachary Lipton, and Hoda Heidari. It caught my eye because of Zachary Lipton's name, who not only has a great first name but also wrote two of my favorite research papers (["The Mythos of Model Interpretability"](https://arxiv.org/abs/1606.03490) and ["Detecting and Correcting for Label Shift with Black Box Predictors"](https://arxiv.org/abs/1802.03916)).

They start with a provocation, in the form of questions about red-teaming exercises:

 1. What types of undesirable behaviors, limitations, and risks can or should be effectively caught and mitigated through red-teaming exercises? 
 2. How should the activity be structured to maximize the likelihood of finding such flaws and vulnerabilities?
 3. How should the risks identified through red-teaming be documented, reported, and managed? 
 4. Is red-teaming on its own sufficient for assessing and managing the safety, security, and trustworthiness of AI?
 5. In short, is red-teaming the stuff of policy or is it the stuff of _vibes_—a vague practice better suited to rallying than to rule-making?

It will not surprise you to learn that different researchers answer the first four questions very differently; red-teaming exercises vary in their definition, scope, object of evaluation, model development lifecycle, assessed risks, evaluation criteria, evaluators, and outputs.
"Our analysis reveals the lack of consensus around the scope, structure, and assessment criteria for AI red-teaming."

Based on an analysis of six red-teaming exercises as case studies, here's how they present their findings:

 - Considerable variation in red-teaming goals and processes across case studies.
 - Language models are primary focus of red-teaming efforts.
 - Evaluation team composition and available resources are interconnected and shape the outcomes of red-teaming.
 - Red-teaming usually probes a broad range of potential vulnerabilities.
 - No standards or systematic procedures for disclosing results of red-teaming.
 - Various risk mitigation strategies are proposed or employed with no consensus on best practices or reporting requirements.
 - Specific monetary and time costs of red-teaming usually not disclosed.
 - Red-teaming misses risks due to broad threat models, evaluator biases, and limitations.
 - No standards for evaluation methods used to supplement red-teaming.

Feffer et al.'s takeaways from these six case studies:
 1. Red-teaming is poorly-structured and is not comprehensive.
 2. Evaluation team composition introduces biases.
 3. Hesitancy to publicly release methods and results reduces utility of red-teaming.

Next, they conducted a literature review of 104 papers that they classify by type of risk and the vulnerability-detection approach used (manual vs algorithmic vs targeted).

They introduce a distinction between _subjective risk_—risk that requires context to determine its threat level—and _subjective risk_—risk that does not require context to evaluate potential harms.
I found this distinction confusing, since their examples of objective risk (divulging private information, leaking training data, writing insecure code, providing phishing assistance) all seem lke they require context to evaluate their potential harms. That's a point Arvind Narayanan and Sayash Kapoor made in ["AI safety is not a model property"](https://www.aisnakeoil.com/p/ai-safety-is-not-a-model-property): safety depends on context.

>Safety depends to a large extent on the context and the environment in which the AI model or AI system is deployed. We have to specify a particular context before we can even meaningfully ask an AI safety question. As a corollary, fixing AI safety at the model level alone is unlikely to be fruitful.

From their literature review, Feffer et al. identified six high-level takeaways:
 - Many different methods to perform red-teaming.
 - Threat modeling skewed toward subjective risk.
 - No consensus on adversary capabilities.
 - No consensus on values used for alignment and red-teaming.
 - No consensus on who should perform red-teaming.
 - Unclear follow-ups to red-teaming activities.

Overall, Feffer et al. argue the following (directly quotes of their recommendations):
 1. Red-teaming is _not_ a panacea.
 2.  Red-teaming, as currently conducted, is _not_ well-scoped or structured.
 3. There are no standards concerning what should be reported.
 4. Mitigation steps initiated by red-teaming are often unclear and unrepresentative.

Their final suggestion: use their set of question banks as an approach to scope red-teaming exercises. 

Before red-teaming, Feffer et al. suggest defining the following aspects of the activity: the artifact under evaluation, the threat model, the specific vulnerability, the criteria for assessing success, the team composition, what resources are made available, what instructions to give the team, what access the team is given to the model, and what methods the team can use. 
You should also decide on what you'll produce after red-teaming: what specific documentation will be written, including a list of the resources consumed, a report on the success criteria, and which risk mitigations to implement.

Overall, I think this is a great framework and a great list of suggestions. Overall, I agree with their provocations: red-teaming is primarily a vibe and it shouldn't be used as the basis for policy or for ensuring a particular standard of "safety".
