---
layout: post
title:  User experience for a clinical trials screening interface
date:   2023-12-04
tags: research
excerpt: Pushing qualitative perspectives in a data science team
---

In May 2023, I published an abstract at the American Society of Clinical Oncology Annual Meeting (ASCO 2023) with my colleagues from ConcertAI:

>Sudip Bhandari, Zachary Levonian, Robert Annand, Jo-Zahn Baxter, Jericho Cain, Jen Flach, Jiby Joseph-Thomas, Judith Mueller.  [Digital Trial Solutions eScreening: a software solution that ranks patients by their predicted clinical trial eligibility using Real-World Data and Machine Learning](https://ascopubs.org/doi/abs/10.1200/JCO.2023.41.16_suppl.e13587). DOI: [10.1200/JCO.2023.41.16_suppl](https://dx.doi.org/10.1200/JCO.2023.41.16_suppl.e13587).e13587 _Journal of Clinical Oncology_ 41, no. 16_suppl (June 01, 2023) e13587-e13587.

DTS eScreening is a software platform for identifying patients that may be eligible for clinical trials based on data in their patient records.
From a statistical perspective, the problem is a [probabilistic classification](https://en.wikipedia.org/wiki/Probabilistic_classification) problem.
To see why, it helps to have a bit more understanding of clinical trials.
Clinical trials are highly-regulated research investigations into the efficacy of a particular treatment regimen, usually for an extremely specific condition e.g. [will taking ibuprofen _and_ acetaminophen be better for pain relief than taking ibuprofen or acetaminophen alone after having 3+ molars removed](https://clinicaltrials.gov/study/NCT02912650)?
Because they're so regulated and so specific, recruitment for clinical trials is challenging: even simple clinical trials can have hundreds of eligibility criteria!
Programs like [ResearchMatch](https://www.researchmatch.org/) make it easier for people to [find clinical trials](https://www.nih.gov/health-information/nih-clinical-research-trials-you/finding-clinical-trial) they're eligible for so they can get access to the "cutting edge" of new medical care and contribute to the research that makes medical care safer and more effective.

- I proposed thinking about this first as a ranking problem
   - That means, among other things: use ranking metrics for evaluation!
   - They knew it was a useful product, but it was hard to say why it was useful. Precision @ k gives us a ranking-appropriate method that makes it clear why the product is useful.
- Silos: the data science team knew shockingly little about how the team was being used.
 - I proposed interviews.
- How did I explain what I was doing? Confluence documentation pages: ...
- Impact: focus on temporal patterns; thinking about patients who will be "eligible soon".

_To read more about peer support and caregiving in healthcare, I recommend [Susannah Fox's blog](https://susannahfox.com/greatest-hits/)._