---
layout: post
title:  "In-context learning: why does it work?"
date:   2024-04-16
tags: research short
excerpt: Why do prompting techniques based on in-context learning improve LLM performance?
image: /images/icl_meme.png
---

In their recent work, [Anthropic provide](https://www.anthropic.com/research/many-shot-jailbreaking) a succinct definition of in-context learning:

>In-context learning is where an LLM learns using just the information provided within the prompt, without any later fine-tuning.

![Drake meme that reads "Add examples to the model prompt" on top and "Condition the model through in-context learning with few-shot demonstrations" on bottom.](/images/icl_meme.png){:style="display:block; margin-left: auto; margin-right: auto;"}
*From Jo Kristian Bergum [on Twitter](https://twitter.com/jobergum/status/1789197209340141837).*

Anthropic, along with many others [including me]({% post_url 2024-02-02-rag-for-math-qa %}), find that in-context learning helps.
In-context learning techniques have blown up in the last few years, including [retrieval augmented generation]({% post_url 2024-02-02-rag-for-math-qa %}), memory augmentation, few-shot learning, [many-shot learning](https://arxiv.org/abs/2404.11018), and more.
Few-shot learning is a specific in-context learning technique that involves providing a discrete set of examples in the prompt: increasing the number of provided examples/"shots" will increase performance on a wide range of tasks (with [diminishing returns i.e. power-law performance increases](https://www.anthropic.com/research/many-shot-jailbreaking)).
For in-context learning in general, many papers have found that benefits scale by power law, e.g. in [2020](https://arxiv.org/abs/2001.08361), [2023](https://arxiv.org/abs/2309.16039), and [2024](https://arxiv.org/abs/2402.00795). Many of the remarkable abilities of LLMs on custom tasks may be primarily attributable to in-context learning (see ["Are Emergent Abilities in Large Language Models just In-Context Learning?"](https://arxiv.org/abs/2309.01809)).

But why does in-context learning "work"? It does seem to help, but our knowledge of why is still preliminary. I've been collecting works with something to say about that topic, and I'm actively interested in seeing more work along these lines. Please send me additional papers (on [Mastodon](https://hci.social/@zwlevonian) or [Twitter](https://twitter.com/zwlevonian)).

Samuel Müller has [recently been pushing](https://twitter.com/SamuelMullr/status/1722630968740331612
) the idea that in-context learning "works" because it attempts to approximate the posterior predictive distribution (see ["Transformers Can Do Bayesian Inference"](https://arxiv.org/abs/2112.10510)).

Laura Ruis says [on Twitter](https://twitter.com/LauraRuis/status/1732402559724208570) that, for instruction-fine-tuned models, "although few-shot prompting helps performance, it probably just helps formatting and doesn't teach the models pragmatics."
Here's Ruis et al. in ["The Goldilocks of Pragmatic Understanding: Fine-Tuning Strategy Matters for Implicature Resolution by LLMs"](https://arxiv.org/abs/2210.14986):

>In-context prompting can mitigate the fact that some models are better at natural prompts and others better at structured prompts by improving performance on the type of prompt the model struggles with zero-shot.

>From the sharp rise in performance observed for the k = 0 to k = 1 result (from 60.2% to 72.8%) we hypothesise that the k-shot in-context examples in this task do not necessarily teach the model pragmatics in-context, but prime the model for the task format.

Based on some experiments with randomizing the labels provided with in-context examples, Ruis et al. conclude that "for base models the content of the in-context prompt seems important, whereas for [example-level instruction-fine-tuned] models the in-context examples mainly serve as a primer for the task structure."

In ["Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?"](https://arxiv.org/abs/2202.12837), Min et al. randomizing the labels provided during few-shot learning still produces in-context learning benefits. From the abstract:

>We show that ground truth demonstrations are in fact not required—randomly replacing labels in the demonstrations barely hurts performance on a range of classification and multi-choce tasks, consistently over 12 different models including GPT-3. Instead, we find that other aspects of the demonstrations
are the key drivers of end task performance, including the fact that they provide a few examples of (1) the label space, (2) the distribution of the input text, and (3) the overall format of the sequence.

Min et al.'s finding is consistent with later work (like Ruis et al.'s discussed above) that format is a critical aspect of in-context learning. (An important implication of this work is that researchers are probably under-reporting *zero*-shot performance in cases where additional unlabeled data is available.)

As [summarized](https://nlpnewsletter.substack.com/p/neurips-2023-primer) by Sebastian Ruder: Prystawski et al. "find that chain-of-thought reasoning is only useful when the training data is locally structured. In other words, when examples are about closely connected topics as is common in natural language. They find that chain-of-thought reasoning is helpful because it incrementally chains local statistical dependencies that are frequently observed in training." See ["Why think step by step? Reasoning emerges from the locality of experience"](https://arxiv.org/abs/2304.03843).

Ruder also summarizes the findings in ["Large Language Models Are Latent Variable Models: Explaining and Finding Good Demonstrations for In-Context Learning"](https://arxiv.org/abs/2301.11916): "examples that are probable based on a latent concept of a task are useful demonstrations"

In ["The Power of Noise: Redefining Retrieval for RAG Systems"](https://arxiv.org/abs/2401.14887), Cuconasu et al. found that RAG improves accuracy even when documents are randomly selected. To my mind, that's more evidence toward the "distribution" theory: any vaguely coherent text provides information about the appropriate output distribution.

In ["The Expressive Power of Transformers with Chain of Thought"](https://arxiv.org/abs/2310.07923), Merrill and Sabharwal argue:

>Chain of thought (and similar prompting approaches that produce a "scratchpad" of intermediate results) enables transformers to solve sequential reasoning problems that they otherwise are incapable of.

In ["The Learnability of In-Context Learning"](https://proceedings.neurips.cc/paper_files/paper/2023/hash/73950f0eb4ac0925dc71ba2406893320-Abstract-Conference.html) at NeurIPS'23, Wies et al. derive thoeretical results that align with some of the empirical results described above: "in-context learning is more about identifying the task than about learning it, a result which is in line with a series of recent empirical findings".

Again, these are work-in-progress notes. Please send me additional research with insights on why in-context learning works!

Edit (2024-11-13): In ["Bayesian scaling laws for in-context learning"](https://arxiv.org/abs/2410.16531), Arora et al. argue that ICL approximates a "Bayesian learner": "Prior work has established strong correlations between the number of in-context examples provided and the accuracy of the model's predictions. In this paper, we seek to explain this correlation by showing that ICL approximates a Bayesian learner. This perspective gives rise to a family of novel Bayesian scaling laws for ICL." They point to a number of other papers that make similar claims about the link between ICL and Bayesian perspetives.

They define the Bayesian model of ICL using by conceptualizing ICL as an expectation maximization problem over tasks.
That is, given a set of tasks τ = {_T_<sub>1</sub>, _T_<sub>2</sub>, ..., _T_<sub>M</sub>} and a document D consisting of a set of terms {σ<sub>1</sub>, σ<sub>2</sub>, ..., σ<sub>n</sub>}, the model estimates the probability that a document is a particular task _p_(_T_<sub>m</sub> | D) using Bayes rule: _p_(_T_<sub>m</sub> | D) = _p_(D | _T_<sub>m</sub>) _p_(_T_<sub>m</sub>) / _p_(D).

 - _p_(_T_<sub>m</sub>) is assumed/given.
 - _p_(D) can be computed as the sum of _p_(D \| _T_<sub>m</sub>) _p_(_T_<sub>m</sub>) for all m ∈ τ.
 - _p_(D \| _T_<sub>m</sub>) can be estimated using each task's likelihood function δ(_T_<sub>m</sub>, σ), which is a probability distribution over the tokens for each task i.e. δ(_T_<sub>m</sub>, σ) = _p_(σ \| _T_<sub>m</sub>).

So, _p_(D \| _T_<sub>m</sub>) could be computed as ∏<sub>σ ∈ D</sub> δ(_T_<sub>m</sub>, σ).

For each task _T*_, they define the scaling law for that task by defining a sampling distribution λ<sub><i>T*</i></sub> over the terms that comprise examples from that task. In other words, they sample a document D from λ<sub><i>T*</i></sub> with n in-context examples, and compute the "next-example probability" as the expectation 𝔼<sub>σ ~ λ<sub><i>T*</i></sub></sub> [ _p_(σ | D) ].
In other words, this expectation relates the number of in-context examples in D to the expected probability of the next example, asserting a direct relationship between n and _p_(σ | D).
They assert the following Bayesian scaling law for the expectation:

>𝔼<sub>σ ~ λ<sub><i>T*</i></sub></sub> [ _p_(σ \| D) ] = ⟮ ∑<sub><i>T</i> ∈ τ</sub> 𝔼<sub>σ ~ λ<sub><i>T</i></sub></sub> [ _p_(σ \| _T_) ]<sup>n+1</sup> _p_(_T_) ⟯ / ⟮ ∑<sub><i>T</i> ∈ τ</sub> 𝔼<sub>σ ~ λ<sub><i>T</i></sub></sub> [ _p_(σ \| _T_) ]<sup>n</sup> _p_(_T_) ⟯ 

where _p_(_T_) is the prior probability of task _T_ and 𝔼<sub>σ ~ λ<sub><i>T</i></sub></sub> is estimated using δ(_T_, σ).
I'm quite confused by their notational choices, so some of those details may be wrong.
They play a little fast and loose with the distinction between a term and an in-context example (which is a sequence of terms) in this formulation; for example, they assume that a Bayesian update only occurs after each
in-context _example_ is processed, not after each _term_ is processed. They resolve this confusion later in the paper by reformulating their law in terms of a scoring matrix.

Ultimately, the work is still preliminary. Arora et al. summarize their view:

>We believe that our results strengthen the claim that LLMs perform Bayesian inference, but do not necessarily prove it. We note that previous works claiming that LLMs are theoretically Bayesian prove their claims on toy models that vastly simplify the complexity of natural language and web-scale pretraining data; it’s possible that actual web-scale Bayesian reasoning is beyond the capacity of current LLMs, but they still may behave approximately Bayesian, explaining the success of our scaling law.

