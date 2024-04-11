---
layout: post
title:  "Inference with predicted data"
date:   2024-04-11
tags: research short
excerpt: Inference with predicted data, including from text data.
---

Inference with predicted data refers to making inferences (causal or otherwise) about a phenomena when some or all of the data we use to make inferences is the result of a predictive algorithm of some kind.
The dream of using statistical models to make data collection cheaper has intoxicated many researchers over the years, although the use of predictive models introduces bias.
Quantifying and correcting that bias remains a long-term open research question.

I may clean this post up later, but here are a few sources discussing these issues:

Kentaro Hoffman et al. ["Do We Really Even Need Data?"](https://arxiv.org/abs/2401.08702) (Feb 2024).

Zach Wood-Doughty et al. ["Challenges of Using Text Classifiers for Causal Inference"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6800252/)

In ["Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond"](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00511/113490/Causal-Inference-in-Natural-Language-Processing), Amir Feder et al. discuss how "causal assumptions are complicated when variables necessary for a causal analysis are extracted automatically from text".

>The main idea is to use NLP methods to extract confounding aspects from text and then adjust for those aspects in an estimation approach such as propensity score matching. However, how and when these methods violate causal assumptions are still open questions.

My favorite example of this approach is the work of Koustuv Saha, e.g. ["A Social Media Study on the Effects of Psychiatric Medication Use"](https://ojs.aaai.org/index.php/ICWSM/article/view/3242).

Open questions I have:
 - I would love to see a good taxonomy of the different types of inference with predicted data, beyond Hoffman et al. There are huge bodies of work on, for example, missing data imputation and causal inference that could be united under a single framework.
 - In what circumstances might using a predictive model reduce bias relative to alternative data collection instruments? Seems hard but valuable to try to quantify this.
