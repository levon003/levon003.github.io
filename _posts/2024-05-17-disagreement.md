---
layout: post
title:  "Annotation, disagreement, and consensus"
date:   2024-05-17
tags: research short
excerpt: "Collection of research related to annotator disagreement and consensus."
---

The conventional approach to machine learning annotation is to have multiple people label each data instance and then take the majority vote. We can do better.

The two primary types of approaches for thinking about achieving consensus are (1) better modeling processes than "majority vote" and (2) discussion or validation processes of some kind.
This blog post rounds up a few papers related to annotator disagreement.

### Modeling

The exemplar approach to probabilistic modeling of annotators and annotator disagreement is the Dawid-Skene model.
The research duo Dawid and Skene [proposed](https://www.jstor.org/stable/2346806) it in 1979. My favorite write-up on the model is Michael Camilleri's ["Reaching a Consensus in crowdsourced data using the Dawid-Skene Model"](https://michaelpjcamilleri.wordpress.com/2020/06/22/reaching-a-consensus-in-crowdsourced-data-using-the-dawid-skene-model/) (2020).

Rebecca Passonneau and Bob Carpenter published ["The Benefits of a Model of Annotation"](https://aclanthology.org/Q14-1025/) (2014) (and a [blog post summary](https://web.archive.org/web/20200818223045/https://lingpipe-blog.com/2014/10/29/beckys-and-my-annotation-paper-in-tacl/)) on a more modern approach. Summarizing from their abstract:

>Standard agreement measures for interannotator reliability are neither necessary nor sufficient to ensure a high quality corpus. [A probabilistic] annotation model provides far more information [than conventional strategies like majority vote], including a certainty measure for each gold standard label; the crowdsourced data was collected at less than half the cost of the conventional approach.

### Discussion processes

My go-to paper for thinking about discussion processes is Schaekermann et al.'s ["Resolvable vs. Irresolvable Disagreement: A Study on Worker Deliberation in Crowd Work"](https://dl.acm.org/doi/10.1145/3274423) (2018), which is comprehensible and provides useful pointers to other research.

### Conceptualizing disagreement and uncertainty

Nan-Chen Chen et al. write usefully about the sources of ambiguity in data annotation, suggesting that there are two primary dimensions of ambiguity: data ambiguity and human subjectivity (["Using Machine Learning to Support Qualitative Coding in Social Science: Shifting the Focus to Ambiguity"](https://dl.acm.org/doi/10.1145/3185515), 2018).

Others have discussed the _uncertainty_ in predictions - including by human annotators and by probabilistic models. The distinction between _aleatoric_ and _epistemic_ uncertainty is a useful way of breaking down the concept, see e.g. ["Deep Learning Uncertainty in Machine Teaching"](https://dl.acm.org/doi/abs/10.1145/3490099.3511117) (2022).

Mitchell Gordon proposed "jury learning". See ["Jury Learning: Integrating Dissenting Voices into Machine Learning Models"](https://dl.acm.org/doi/abs/10.1145/3491102.3502004) (2022) and ["The Disagreement Deconvolution: Bringing Machine Learning Performance Metrics In Line With Reality"](https://dl.acm.org/doi/abs/10.1145/3411764.3445423) (2021).

Also on juries: ["Can Online Juries Make Consistent, Repeatable Decisions?"](https://dl.acm.org/doi/abs/10.1145/3411764.3445433) (2021). In the context of community moderation (which is relevant for many real-world annotation practices), see ["Measuring User-Moderator Alignment on r/ChangeMyView"](https://dl.acm.org/doi/abs/10.1145/3610077) (2023).

Luke Guerdan et al. refer to rating tasks with multiple valid labels as "rating indeterminacy". See ["Validating LLM-as-a-Judge Systems under Rating Indeterminacy"](https://arxiv.org/abs/2503.05965) (2025). (They suggest: "whenever possible, design 'fully-specified' rating tasks that instruct raters how to resolve rating indeterminacy; where tasks cannot be fully specified, elicit multi-label 'response set' ratings and apply multi-label human–judge agreement metrics." In other words, the authors don't think you should compute IRR in a for indeterminate tasks. I think this is probably a bridge too far; in my experience, all annotation tasks are indeterminate to some degree.)
