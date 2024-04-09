---
layout: post
title:  "Research paper: Inconsistent multiple testing corrections"
date:   2024-04-09
tags: research statistics short
excerpt: Mark Rubin's position paper on statistical adjustments for multiple comparions.
---

In ["Inconsistent multiple testing corrections: The fallacy of using family-based error rates to make inferences about individual hypotheses"](https://www.sciencedirect.com/science/article/pii/S2590260124000067), Mark Rubin argues that multiple comparisons corrections like [Bonferroni correction](https://en.wikipedia.org/wiki/Bonferroni_correction) are often misapplied. (Rubin also wrote a [shorter summary on his own site](https://sites.google.com/site/markrubinsocialpsychresearch/replication-crisis/inconsistent-multiple-testing-corrections).)

Rubin's summary of his argument:

>My key point is that researchers should be logically consistent in their use of multiple testing corrections. If researchers use multiple testing corrections, then they should make corresponding statistical inferences about family-based _joint_ hypotheses. They should not correct their alpha level and then only proceed to make statistical inferences about _individual_ hypotheses because such inferences do not require an alpha adjustment.

>An _inconsistent correction_ occurs when a researcher corrects their alpha level during multiple testing but does not make an inference about a union alternative hypothesis. In this new article, I discuss this inconsistent correction problem.

What to do about inconsistent corrections?

>We should adopt an inference-based perspective that advocates an alpha adjustment in the case of inferences about intersection null hypotheses but not in the case of inferences about individual null hypotheses.

"Intersection null hypothesis" refers to hypotheses of the form "there is no difference in X for groups A, B, and C". The union alternative hypothesis is that "at least one of A, B, or C differs in X".

The question of when to apply a correction for multiple comparisons is not an easy one; in my own work, I've often been struck by the difficulty of determining which hypotheses are "grouped". The challenge is that grouped hypotheses are often implicit and reporting decisions are made conditional on the result of those tests.

Consider the common sub-group analysis: I want to say whether some main effect X expresses itself differently in subgroups A, B, and C. If my null hypothesis test is non-significant at my chosen alpha threshold for all three subgroups, I might report this as a test against the intersection null hypothesis. But if one or two (but not all three) tests are significant, I might report this as tests against individual null hypotheses (and proceed to speculate wildly about what makes A and X related). Not a good practice, but I suspect a common one.

In these cases, multiple comparisons corrections are still appropriate because I was implicitly interested in the intersection null hypothesis.
For that reason, I generally recommend correction if it will determine what you draw attention to in your results. (If tests are being conducted exhaustively, such as in an appendix table, I don't think it matters; avoid correction in those cases and present summary statistics clearly to make the life of researchers doing meta-analyses a bit easier.)
