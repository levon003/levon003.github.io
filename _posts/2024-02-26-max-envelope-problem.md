---
layout: post
title: "An interesting two envelopes problem"
date:   2024-02-26
tags: statistics algorithms short
excerpt: "A probability question posted on Twitter."
---

Shared by [Leonardo Cotta on Twitter](https://twitter.com/cottascience/status/1761933758003827161):

>I find it interesting that people often don't know this riddle, but it tells you everything you need to know about randomized algorithms ;)

I have never studied randomized algorithms, and I found the problem and its solution very interesting.

The problem:

>Consider two envelopes labeled A and B, each containing a real number. You’re allowed to select one envelope and view its value before deciding whether A or B has the max value. Can you devise a strategy to decide the max envelope with a probability greater than 0.5?

The solution:

> 1) Pick your favourite distribution with support over R, e.g. Gaussian.
>
> 2) Pick a random number X according to this distribution. 
>
> 3) You pick one envelope uniformly at random and see the value Y. 
>
> 4) You switch if X > Y and keep your envelope if X <= Y. 
>
> What is your success probability? 
>If X > max(A,B), your algorithm picks an envelope unif at random (because you pick one at random, and always switch, which is equivalent to pick one unif at random). 
>If X <= min(A,B), your algorithm picks an envelope at random (same reason). 
>If min(A,B) < X < max(A,B) you are always correct! 
>
>So your success probability is 0.5 + Pr[min(A,B) < X < max(A,B)] > 0.5. 

I don't know if this problem or class of problems has a name. Intuitively, it seems related to the [two envelopes problem](https://en.wikipedia.org/wiki/Two_envelopes_problem).
