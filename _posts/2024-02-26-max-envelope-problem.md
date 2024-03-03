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

## Simulating the max two envelope problem

Does the strategy described above actually work?
Let's try simulating this strategy on fake data so we can convince ourselves it will work.
(I'm a fan of [simulations for estimating probabilities]({% post_url 2024-02-13-stardew-valley-gold-total %}) when we're not confident in our ability to compute the probabilties analytically.)

In the real problem, we don't get to know the distribution from which the envelope values are drawn. For my simulation, I'll just take draws from the standard normal distribution.

![Histogram of four selection strategies, demonstrating that the strategy described above does produce above-chance success probability.](/images/max-envelope-problem-simulation.png){:style="display:block; margin-left: auto; margin-right: auto;"}
*Over 10 million envelope openings, the strategy described above produces above-chance success probability.*

If I draw my "decision value" (X) from the same (_matching_) distribution, I increase my success probability from 50% to 66%.
(That implies Pr[min(A,B) < X < max(A,B)] ≈ 0.166 when A, B, and X are drawn from the standard normal distribution.)
If the distribution I choose has a higher standard deviation (_wide_), my success probability will drop correspondingly (but still be above chance). Similarly, if I shift the distribution's mean (_shifted_) so that fewer decision values lie between A and B, my success probability will also drop. As described in the proof above, it's all about how likely it is that X falls between A and B.

_The code for this simulation is [on GitHub](https://github.com/levon003/levon003.github.io/blob/main/notebooks/MaxTwoEnvelopesSimulation.ipynb)._
