---
layout: post
title:  "Non-linearities in floating point arithmetic"
tags: short ml
excerpt: "IEEE 754 floating point arithmetic is non-associative."
---

I recently learned about Tom 7's ["GradIEEEnt half decent"](http://tom7.org/grad/) project (presented in a paper and an excellent [YouTube video](https://www.youtube.com/watch?v=Ae9EKCyI1xU)).

The intuition behind the project is the following: 

1. Neural nets depend on non-linear activation functions; otherwise, you get no benefit from multiple layers and you're just learning a big linear function!
2. However, mathematically linear functions can be non-linear in practice.
  - Standard [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754) floating point arithmetic necessarily does rounding in some cases; floating point numbers can't be represented with infinite precision using the IEEE 754 standard. 
  - Addition and multiplication with IEEE 754 floating point numbers are not associative. i.e. (a + b) + c ≠ a + (b + c)
  - Similarly, addition and multiplication are not commutative. i.e. a * b * c ≠ b * a * c.
3. Can we train a neutral network with a mathematically linear activation function if we exploit the rounding that occurs during IEEE 754 arithmetic to introduce non-linearity?

Tom finds _yes_, and you can do a lot more with the incidental non-linearity that floating point arithmetic introduces besides. I highly recommend checking out his work.

The properties of floating point arithmetic are responsible for some of the non-determinancy that occurs during machine learning model training and inference, and more generally during distributed map-reduce style workflows.

Here's some interesting further reading:

 - ["Nonlinear computation in deep linear networks"](https://openai.com/index/nonlinear-computation-in-deep-linear-networks/) by OpenAI.
 - ["Nondeterminism in MapReduce considered harmful? an empirical study on non-commutative aggregators in MapReduce programs"](https://dl.acm.org/doi/10.1145/2591062.2591177) ([open-access pdf](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/icsecomp14seip-seipid15-p.pdf)) by Tian Xiao, Jiaxing Zhang, Hucheng Zhou, Zhenyu Guo, Sean McDirmid, Wei Lin, Wenguang Chen, and Lidong Zhou.
 - ["A Workaround for Non-Determinism in TensorFlow"](https://www.twosigma.com/articles/a-workaround-for-non-determinism-in-tensorflow/) by Two Sigma.


I learned about this phenomenon from [this Reddit thread](https://reddit.com/r/MachineLearning/comments/1ie15ev/d_nondeterministic_behavior_of_llms_when/).
