---
layout: post
title:  "Stochtree: a library for Stochastic tree ensembles (BART / XBART) for supervised learning and causal inference"
tags: research code short
excerpt: "Stochtree is a Bayesian Additive Regression Trees (BART) software library."
---

Today, I saw a [talk](https://github.com/jaredsmurray/levi_demo) from [Jared Murray](https://jaredsmurray.github.io/) on the [`stochtree`](https://github.com/StochasticTree/stochtree) library. Stochtree has a C++ core with bindings for Python and R.

Read more and install: <https://stochtree.ai>

I wasn't previously familiar with Bayesian Additive Regression Trees (BARTs), but it's basically a Bayesian version of a random forest.

Installing on MacOS was a bit of a challenge (see my notes and demo [on GitHub](https://github.com/levon003/levon003.github.io/tree/main/src/stochtree)).

Further reading:
 - ["Bayesian Additive Regression Trees"](https://bayesiancomputationbook.com/markdown/chp_07.html) in _Bayesian Modeling and Computation_
 - ["Comparison of tree-based ensemble models for regression"](http://www.csam.or.kr/journal/view.html?doi=10.29220/CSAM.2022.29.5.561)
 - ["Introduction to Bayesian Additive Regression Trees"](https://jmloyola.github.io/posts/2019/06/introduction-to-bart)