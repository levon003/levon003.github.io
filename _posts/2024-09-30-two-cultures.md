---
layout: post
title:  "Two approaches to statistical modeling?"
date:   2024-09-30
tags: research statistics
excerpt: "Three papers that break down the goals of statistical modeling."
---

This post is a quick summary of three papers that break down the goals and approaches of statistical modeling. I find myself returning to these papers often, and I heartily recommend reading all three:

 - Breiman's ["Statistical Modeling: The Two Cultures"](https://projecteuclid.org/journals/statistical-science/volume-16/issue-3/Statistical-Modeling--The-Two-Cultures-with-comments-and-a/10.1214/ss/1009213726.full) (2001)
 - ["On Discriminative vs. Generative Classifiers: A comparison of logistic regression and naive Bayes"](https://papers.nips.cc/paper_files/paper/2001/hash/7b7a53e239400a13bd6be6c91c4f6c4e-Abstract.html) (2001)
 - Hofman et al.'s ["Integrating explanation and prediction in computational social science"](https://www.nature.com/articles/s41586-021-03659-0) (2021)

## Statistical Modeling: The Two Cultures

Leo Breiman wrote ["Statistical Modeling: The Two Cultures"](https://projecteuclid.org/journals/statistical-science/volume-16/issue-3/Statistical-Modeling--The-Two-Cultures-with-comments-and-a/10.1214/ss/1009213726.full) in 2001.

Breiman argues that there are two goals in analyzing data:

 - **Prediction**: To be able to predict what the responses (y) are going to be to future input variables (X).
- **Information**: To extract some information about how nature is associating the response variables (y) to the input variables (X).

Breiman is using the common analogy of a black box data-generating process that receives a vector of independent variables (X) and produces repsonse variables (y).

The **data modeling** culture assume "a stochastic data model for the inside of the black box". Think linear regression.

The **algorithmic modeling** culture assume the inside of the box is "complex and unknown". Think deep learning or gradient boosting.

>I am not against data models per se. .... But the emphasis needs to be on the problem and
on the data.

I associate data modeling culture with an interest in [interpretable machine learning]({% post_url 2024-05-18-interpretable-ml %}).

#### Interpretability

>Unfortunately, in prediction, accuracy and simplicity (interpretability) are in conflict. For instance, linear regression gives a fairly interpretable picture of the y, X relation. But its accuracy is usually less than that of the less interpretable neural nets.

Breiman calls this the _Occam dilemma_: "Accuracy generally requires more complex prediction methods. Simple and interpretable functions do not make the most accurate predictors." He claims that "the models that best emulate nature in terms of predictive accuracy are also the most complex and inscrutable."

>The point of a model is to get useful information about the relation between the response and predictor variables. Interpretability is a way of getting information.

I like this re-framing of interpretability as a process for getting information about the variables. It's interesting that in the 20 years since this was published a whole field (mechanistic interpretability) arose using interpretability methods to understand the functioning of the _model_, which demonstrates how complex the models have gotten!

#### Responses

In 2021, the journal _Observational Studies_ published a [special issue with 28 commentaries](https://muse.jhu.edu/pub/56/issue/45147) on Breiman's essay. [Nandita Mitra](https://www.mitrastatslab.com/team) [summarizes the repsonses](https://muse.jhu.edu/pub/56/article/799740) as covering:

 1. The blending and cross-fertilization of modeling cultures (not just two distinct ones) under historical, foundational, and flexible paradigms 
 2. The importance of interpretable algorithms, understanding the data, outcome reasoning, modeling based on scientific theory, and social responsibility
 3. Causal modeling 
 4. Bayesian inference
 5. Distributed learning, targeted learning, supervised learning, and computational thinking

 Judea Pearl, for example, [writes](https://muse.jhu.edu/pub/56/article/799733) that "the two cultures contrasted by Breiman are not descriptive vs. causal but, rather, two styles of descriptive modeling, one interpretable, the other uninterpretable". He argues (as he always does) for causal modeling: "As we read Breiman's paper today ... we may say that his advocacy of algorithmic prediction was justified. Guided by a formal causal model for identification and bias reduction, the predictive component in the analysis can safely be trusted to non-interpretable algorithms. The interpretation can be accomplished separately by the causal component of the analysis."

## On Discriminative vs. Generative Classifiers

["On Discriminative vs. Generative Classifiers: A comparison of logistic regression and naive Bayes"](https://papers.nips.cc/paper_files/paper/2001/hash/7b7a53e239400a13bd6be6c91c4f6c4e-Abstract.html) is a famous paper by famous authors: Andrew Ng and Michael I. Jordan.
It focuses on the distinction between _discriminative_ and _generative_ classifiers, providing a useful abstraction for thinking about modeling.

>Generative classifiers learn a model of the joint probability, _p(x,y)_, of the inputs _x_ and the label _y_, and make their predictions by using Bayes rules to calculate _p(y\|x)_, and then picking the most likely label _y_. Discriminative classifiers model the posterior _p(y\|x)_ directly, or learn a direct map from inputs _x_ to the class labels. There are several compelling reasons for using discriminative rather than generative classifiers, one of which, succinctly articulated by [Vapnik](https://www.wiley.com/en-us/Statistical+Learning+Theory-p-9780471030034), is that "one should solve the [classification] problem directly and never solve a more general problem as an intermediate step [such as modeling _p(x\|y)_]."

I found this distinction hugely helpful when I was first learning about machine learning, although this distinction between the posterior and the joint probability is fairly tenuous for many modeling approaches.

## Integrating explanation and prediction in computational social science

In ["Integrating explanation and prediction in computational social science"](https://www.nature.com/articles/s41586-021-03659-0) ([open-access pdf](https://par.nsf.gov/servlets/purl/10321875)), Hofman et al. articulate the use of statistical modeling for answering social science research questions.

They articulate four approaches to modeling:

 1. Descriptive modeling: Describe situations in the past or present (but neither causal nor predictive)
 2. Explanatory modeling: Estimate effects of changing a situation (but many effects are small)
 3. Predictive modeling: Forecast outcomes for similar situations in the future (but can break under changes)
 4. Integrative modeling: Predict outcomes and estimate effects in as yet unseen situations

They lay these four approaches to modeling in a 2x2 grid reflecting two primary axes:
 - Focusing on _specific features or causal effects_ vs _outcomes_
 - One dataset (no experimental intervention or distributional shift) vs multiple datasets (e.g. comparisons under intervention or under distributional shift)

 Descriptive and explanatory modeling are mostly self-explanatory, but the distinction between predictive and integrative modeling is a little more subtle:

>Whereas [predictive modeling] concerns itself with data that are out of sample, but still from the same (statistical) distribution, [for integrative modeling] the focus is on generalizing ‘out of distribution’ to a situation that might change either naturally, owing to some factor out of our control, or because of some intentional intervention such as an experiment or change in policy.

While planning a new modeling project, I encourage researchers to think through the specific type of modeling they are trying to do.
These days, many people I work with try to apply predictive modeling tools for explanatory or integrative modeling tasks. 
