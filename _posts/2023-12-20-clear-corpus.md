---
layout: post
title:  The CommonLit Ease of Readability (CLEAR) Corpus
date:   2023-12-20
tags: research data short
excerpt: A dataset for advancing readability research.
---
The [CLEAR corpus](https://www.commonlit.org/blog/introducing-the-clear-corpus-an-open-dataset-to-advance-research-28ff8cfea84a/) is a cool dataset of teacher ratings of texts.

In [the paper](https://link.springer.com/article/10.3758/s13428-022-01802-x), they say:

> We recruited ~ 1800 teachers from the CommonLit teacher pool through an e-mail marketing campaign. .... Teachers were then expected to read 100 pairs of excerpts and make a judgment for each pair as to which excerpt was easier to understand. Teachers were paid $50 in an Amazon gift card for their participation.

They collected 111,347 pairwise judgments on about 4793 excerpts.
These 4793 excerpts were the result of a somewhat complex filtering process. The primary inclusion criteria are (1) "likelihood of being used in a 3rd–12th grade classroom" and (2) "whether or not the topic was appropriate". 

Based on the pairwise judgments, they compute readability scores for each excerpt using a [Bradley–Terry model](https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model). (Here's a useful December 2023 preprint from Ian Hamilton, Nick Tawn, David Firth: ["The many routes to the ubiquitous Bradley-Terry model"](https://arxiv.org/abs/2312.13619))

They appear not to have released the pairwise judgment data, which is disappointing. 
