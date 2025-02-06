---
layout: post
title:  "Overfitting to train/test splits"
tags: research ml overfitting stats benchmarks
excerpt: "Ben Recht writes in a 2023 blog post that train-test splits are shockingly effective for evaluating machine learning models."
---

In a [2023 blog post](https://www.argmin.net/p/you-got-a-9-to-5-so-ill-take-the), Ben Recht describes the surprising effectiveness of a held-out test set for comparing model performance.

The post describes his paper ["Do ImageNet Classifiers Generalize to ImageNet?"](https://arxiv.org/abs/1902.10811). Recht et al. explore the degree to which iterative selection of models based on test set performance leads to [overfitting](https://www.argmin.net/p/flavors-of-overfitting).

The conventional assumption is that iterative modeling against a train-test split will result in inaccurate, overly-optimistic estimates for model behavior. That leads to guidance like "only evaluate your model against the test set once".

To evaluate the extent of these problems on academic machine learning benchmarks, Recht et al. created a new benchmark dataset using the same process as an existing, widely-used dataset. Then, he evaluated years of previously-published models on this new test set.
Recht says that he "was frankly flabbergasted by the results".

>The models that performed the best on the original test set performed the best on the new test set. That is, there is no evidence of “overfitting.”

The rank ordering of the models relative to each other was the same as on the original test set. However, performance was lower on the "new" test set than on the old test set.

>The takeaway from this series of studies is simple. The train-test benchmarking has absurdly robust _internal validity_. It’s incredibly hard to adaptively overfit to a test set. Our “generalization bounds” are wildly conservative for machine learning practice. However, _external validity_ is less simple. How machine learning models will perform on new data is not predictable from benchmarking.

While I am surprised by the strong internal validity Recht et al. observe, I think external validity is critically important. 
In my view, "not predictable from benchmarking" goes too far; I can think of many cases where an _i.i.d._ test set constructed to closely mirror the deployed environment for the prediction model is an excellent predictor of true performance.
In non-academic settings, many "test" datasets are continually refreshed with new data, with old data graduating out to become training data. In my experience, this general approach works well in cases with only modest distribution shifts.

### Simulating external validity impacts of benchmark reuse

It is straightforward to see overfitting happen in practice. (See the code for this section [on GitHub](https://github.com/levon003/levon003.github.io/blob/main/src/overfitting/OverfittingDemo.ipynb).)

I generated a sample benchmark consisting of 400 training data points and 100 testing data points. The task is binary prediction from three variables. The outcome _y_ is a simple function of three variables: sigmoid(3a^2 - 3b + 3c / 2), where a, b, and c are sampled from a normal, beta, and uniform distribution respectively. I publish my benchmark and wait for the results to role in.

This is a far simpler environment than most academic benchmarks, but we can observe overfitting even for this simple modeling task:
 1. Researcher A trains a model (a [Histogram-based Gradient Boosting Decision Tree](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html)) on the training data, evaluates on the test set, and publishing their performance.
 2. Researcher B trains a new model (perhaps a new architecture or set of features, in this case just a different set of hyperparameters) and achieves better performance, publishing their own result.
 3. Repeat this process!

I've seen this process referred to as [graduate student descent](https://arxiv.org/abs/1904.07633). Functionally, publication of new models is a non-random search over all possible models where each new modeling approach is motivated by humans' scientific and engineering intuition. 

With a basic sweep over 24 hyperparameter configurations, the best published model on my benchmark achieves 93% accuracy. But because I know the data-generating function, I can compute the "true" accuracy of the model by just sampling 10,000 new data unseen during training or testing. Unfortunately, the true accuracy is lower: only 91%!

Even in this highly-simplified environment, overestimating tue performance is common. I repeated the same simulation 600 times, and on average the benchmark performance overestimates the true performance by 1.5 percentage points (95% CI 1.2pp-1.7pp).
Benchmark performance is computed as the best model performance of the 24 unique hyperparameter configurations.
The figure below shows the difference in accuracy for all 600 simulations.

![Histogram of 600 benchmarking simulations; a somewhat normal distribution.](/images/overfitting_sim_hist_n600.svg){:style="display:block; margin-left: auto; margin-right: auto;"}
*Difference between benchmark accuracy and "true" accuracy for 600 simulations.*

73% of the simulations produce an overestimate of true performance; 43% overestimate true accuracy by 2 percentage points or more.
This simulation demonstrates the pattern that Recht et al. observe, and it means we should be skeptical of long-standing benchmark performance as a valid estimate of true model performance on the task... even when there is _zero_ shift in the true distribution!

The reality of overestimating true model performance from benchmarks is likely much worse, as researchers get trapped in local minima, explore modeling configurations non-systematically, and avoid publishing negative results. That's why publishing updated versions of benchmarks is one of the most valuable (but under-appreciated) tasks in machine learning research.

The results of this simulation demonstrate the same negative impact on external validity that Recht et al. found, but Ben Recht [would likely deny](https://www.argmin.net/p/flavors-of-overfitting) that we should call this "overfitting". He identifies three kinds of overfitting:
> 1. _Statistical overfitting_. This occurs because a test set gives a nonzero, though unbiased, estimate of prediction error.
> 2. _Adaptive overfitting_. This occurs because we look at the test set too much and then perform poorly on a new iid sample.
> 3. _Contextual overfitting_. This occurs because the new data differs in some way from the data we use to train our model.

I personally find this taxonomy useful, and I would argue that what we observe in this simulation is a combination of statistical overfitting and adaptive overfitting.
By repeating our simulation with a larger test set, the impact of statistical overfitting would decrease and the impact of adaptive overfitting would increase. 
Similarly, exploring more hyperparameters/model improvements before stopping would increase the impact of adaptive overfitting.
However, Recht might argue that the difference between true and benchmarked performance revealed in my simulation shouldn't be called even adaptive overfitting because although the performance decreases as more models are explored, the relative ranking of the 24 models I train in each simulation won't change.
Recht is certainly right that [overfitting has no consistent definition](https://www.argmin.net/p/thou-shalt-not-overfit), which is why it's probably better to describe what the simulation is actually telling us (the negative impact of repeated benchmark usage on external validity) rather than lazily referring to it as "overfitting".

Further reading:

 - Ben Recht's ["Thou Shalt Not Overfit"](https://www.argmin.net/p/thou-shalt-not-overfit)
 - Ben Recht's ["Flavors of overfitting"](https://www.argmin.net/p/flavors-of-overfitting)
 - My own work has looked at cross validation for estimating performance on datasets constructed iteratively, rather than for static benchmarks. ["Trade-offs in Sampling and Search for Early-stage Interactive Text Classification"](https://dl.acm.org/doi/10.1145/3490099.3511134)
