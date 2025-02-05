---
layout: post
title:  "Overfitting to train/test splits"
tags: short ml research
excerpt: "Ben Recht writes in a 2023 blog post that train-test splits are shockingly effective for evaluating machine learning models."
---

Ben Recht writes in a blog post about the surprising effectiveness of a held-out test set for comparing model performance: ["You got a 9 to 5, so I'll take the night shift"](https://www.argmin.net/p/you-got-a-9-to-5-so-ill-take-the).

In a paper with some colleagues (["Do ImageNet Classifiers Generalize to ImageNet?"](https://arxiv.org/abs/1902.10811)), he explores the degree to which iterative selection of modeling techniques based on test set performance leads to [overfitting](https://www.argmin.net/p/flavors-of-overfitting).

The conventional assumption is that iterative modeling against a train-test split will result in inaccurate, overly-optimistic estimates for model behavior. That leads to guidance like "only evaluate your model against the test set once".

To evaluate the extent of these problems on academic machine learning benchmarks, Recht et al. created a new benchmark dataset using the same process as an existing, widely-used dataset. Then, he evaluated years of previously-published models on this new test set.
Recht says that he "was frankly flabbergasted by the results".

>The models that performed the best on the original test set performed the best on the new test set. That is, there is no evidence of “overfitting.”

The rank ordering of the models relative to each other was the same as on the original test set. However, performance was lower on the "new" test set than on the old test set.

>The takeaway from this series of studies is simple. The train-test benchmarking has absurdly robust _internal validity_. It’s incredibly hard to adaptively overfit to a test set. Our “generalization bounds” are wildly conservative for machine learning practice. However, _external validity_ is less simple. How machine learning models will perform on new data is not predictable from benchmarking.

While I am surprised by the strong internal validity Recht et al. observe, I think external validity is critically important. 
In my view, "not predictable from benchmarking" goes too far; I can think of many cases where an _i.i.d._ test set constructed to closely mirror the deployed environment for the prediction model is an excellent predictor of true performance.
In industrial settings, many "test" datasets are continually refreshed with new data, with old data graduating out to become training data. In my experience, this general approach works well in cases with only modest distribution shifts.

Further reading:

 - Ben Recht's ["Thou Shalt Not Overfit"](https://www.argmin.net/p/thou-shalt-not-overfit)
 - Ben Recht's ["Flavors of overfitting"](https://www.argmin.net/p/flavors-of-overfitting)
