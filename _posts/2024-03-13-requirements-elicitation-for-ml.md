---
layout: post
title:  "Requirements elicitation for machine learning applications"
date:   2024-03-13
tags: research design short
excerpt: "Requirements elicitation for ML-backed designs can be challenging, through the lens of Qian Yang et al.'s CHI paper."
image: /images/yang_chi2020_fig1.png
---

Here's Hilliard Holbrook writing in 1990 (!) about gathering requirements for design:

>Requirements analysis is the process of identifying a user's needs and determining what to build in an a system. Within requirements analysis is the process of _requirements elicitation_ in which tacit information about "what to build" is obtained from the user and his environment.

That's from ["A scenario-based methodology for conducting requirements elicitation"](https://dl.acm.org/doi/abs/10.1145/382294.382725), which proposes the use of scenarios to "structure the early interaction between users and designers in order to quickly develop a set of initial requirements. The methodology features the parallel development of requirements and a high-level design, the use of scenarios to communicate the behavior of a design, an evaluation function to assess the suitability of the design, and an issue base with which to maintain the issues that arise during the elicitation process."

Nowadays, scenarios (often called by other names) are the standard way that designers engage with users to elicit requirements. However, eliciting requirements when the design space involves machine learning is difficult.

In ["Re-examining Whether, Why, and How Human-AI Interaction Is Uniquely Difficult to Design"](https://dl.acm.org/doi/abs/10.1145/3313831.3376301) (CHI 2020), Qian Yang et al. discuss designs that involve human interaction with machine learning system outputs, identifying two aspects of machine learning that make design uniquely difficult:
 1. "Uncertainty surrounding AI's capabilities"
 2. "AI's output complexity, spanning from simple to adaptive complex"

So why is requirements elicitation harder? Because you're forced to confront realities of capability uncertainty and output complexity _before_ thinking seriously about how a design will affect user experience.

![Human-AI interaction design challenges](/images/yang_chi2020_fig3.png)
*Figure 3 in Yang et al.'s CHI paper. "AI’s capability uncertainty and output complexity add additional steps (the colored segments) to a typical HCI pathway, make some systems distinctly difficult to design."*

Yang et al. provide a nice list of human-AI interaction design challenges that occur pre-development:

 - Difficult to articulate what AI can/cannot do
 - Technical feasibility of a design idea is highly dependent on data
 - Do not know how to purposefully use AI in the design problem at hand
 - Do not know how to express AI design ideas
 - Difficult to sketch divergent AI interactions
 - Cannot fast prototype AI system behavior
 - Difficult to foresee the potential effects of AI
 - Difficult to design fuzzy, open-ended interactions

![Human-AI interaction design challenges](/images/yang_chi2020_fig1.png)
*Figure 1 in Yang et al.'s CHI paper.*

I won't go into detail here about how to adapt requirements elicitation to respond to the novel challenges of designing with machine learning. But I generally think the solution is iterative development of scenarios with designers and developers working together to reduce uncertainty about realistic capabilities and to characterize desired output complexity.
