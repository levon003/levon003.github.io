---
layout: post
title: "Research paper: Label Sleuth"
date:   2024-03-01
tags: research short
excerpt: "Shnarch et al.'s EMNLP 2022 paper \"Label Sleuth: From Unlabeled Text to a Classifier in a Few Hours\""
---

[Label Sleuth](https://www.label-sleuth.org/) is a system described in the EMNLP 2022 paper ["Label Sleuth: From Unlabeled Text to a Classifier in a Few Hours"](https://aclanthology.org/2022.emnlp-demos.16/).

Label Sleuth is a system for labeling data and training text classifiers on-the-fly. To evaluate a model trained from the already-labeled data, they describe a _Precision Evaluation_ procedure:

>The system samples _n_ sentences that are predicted as positive by the current classifier. [The user] is asked to label these sentences and her feedback is used to estimate the precision of the classifier.

This proposed procedure is the most interesting suggestion of the paper to me. They discuss the challenges of evaluating a classifier in the discussion:

>Maintaining a separate test set, which is not utilized for model training, undermines the goal of minimizing the labeling effort. Cross validation evaluation is incorrect in this scenario as the labeled examples collected in the process are not necessarily a good representation of the data (being biased towards positive examples and by active learning suggestions).

That's a point I made explicitly in my own paper, ["Trade-offs in Sampling and Search for Early-stage Interactive Text Classification"](https://dl.acm.org/doi/10.1145/3490099.3511134), where we found that commonly-used active learning techniques (and the user manually choosing what to annotate) will badly bias cross-validation estimates of model performance.

I like the _Precision Evaluation_ approach, because [many text classification problems are precision-focused](https://zwlevonian.medium.com/how-would-you-deal-with-an-ambiguous-problem-data-science-interview-question-891638470572), although I think recommending unlabeled texts dynamically depending on the user's expressed evaluation goals would complement that approach.

The next time I need to do some data labeling, I might give Label Sleuth a try, since it is open source and looks more mature than the alternatives I've looked at in the past.
