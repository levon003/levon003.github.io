---
layout: post
title:  "“Wishful Mnemonics” in Machine Learning Research"
date:   2023-10-17
tags: research
excerpt: An always-relevant term from researcher Melanie Mitchell.
---
{% include references.html %}

In "Why AI is Harder Than We Think", researcher [Melanie Mitchell](https://en.wikipedia.org/wiki/Melanie_Mitchell) describes fallacies in our collective thinking about AI {{ref1}}.
The third fallacy is "the lure of wishful mnemonics", for which Mitchell appropriates a phrase first used by computer scientist [Drew McDermott](https://en.wikipedia.org/wiki/Drew_McDermott) in 1976.

Here's McDermott, as quoted by Mitchell:

>A major source of simple-mindedness in AI programs is the use of mnemonics like "UNDERSTAND" or "GOAL" to refer to programs and data structures. ...If a researcher...calls the main loop of his program “UNDERSTAND,” he is (until proven innocent) merely begging the question. He may mislead a lot of people, most prominently himself. ...What he should do instead is refer to this main loop as “G0034,” and see if he can convince himself or anyone else that G0034 implements some part of understanding. ... Many instructive examples of wishful mnemonics by AI researchers come to mind once you see the point {{ref2}}.

Mitchell defines **wishful mnemonics** as "terms associated with human intelligence that are used to describe the behavior and evaluation of AI programs."

Mitchell points to the ubiquity of anthropomorphic terms like 'understand' or 'reasons' that influence "our conceptions of how general those abilities really are".  When researchers choose anthropomorphic terms, they intentionally or unintentionally position themselves as marketers, obscuring the behavior of a system and making it harder to compare and benchmark system performance.

The rise of large language models has only accelerated this trend; analogies to human thinking abound in recent machine learning research and software. What is needed is careful work that operationalizes these "wishful mnemonics" into more descriptive language and creates rigorous tests of those capabilities. McCoy et al. are a great recent example {{ref3}}, and I hope to see a turn away from hype-driven terminology to focus on accurately characterizing observed system properties and behaviors.

#### Addendum (2023-10-27): Makeism

Iris van Rooij et al. define the term _makeism_ {{ref4}}:

>Makeism: The view that computationalism implies that (_a_) it is possible to (re)make cognition computationally; (_b_) if we (re)make cognition then we can explain and/or understand it; and possibly (_c_) explaining and/or understanding cognition requires (re)making cognition itself.
>
>.... A well-known quote from [Feynman (1988)](https://digital.archives.caltech.edu/collections/Photographs/1.10-29/), “what I cannot create, I do not understand”, is often used to support the idea of makeism in AI (e.g. [Karpathy et al., 2016](https://web.archive.org/web/20180121082551/https://blog.openai.com/generative-models/)).
>
>Note that it is especially easy for makeists to fall into map-territory confusion—mistaking their modeling artefacts for cognition itself—due to the view that the made thing _could_ be cognition.

To my eyes, van Rooij et al.'s makeism is highly associated with a use of wishful mnemonics. Note in particular the argument around "map-territory confusion": this is a mistake that's easy to make when adopting the mnemonics for computational processes that McDermott laments, like using "UNDERSTAND" isntead of "G0034".

van Rooij et al. go even farther than McDermott and Mitchell, however, arguing that we are too easily convinced. 
In practice, "AIs appear human-like in non-rigorous tests, but the likeness is debunked when more rigorous tests are made .... This back and forth between claims of human-likeness and debunking (_cf._ Mitchell, 2021 {{ref1}}) will keep happening if the field does not realise that AI-by-learning is intractable, and hence any model produced in the short run is but a 'decoy'" {{ref4}}.

_This post was based on a [tweet](https://twitter.com/zwlevonian/status/1387820787768315904)._

### References

<ol class="reference-block">
  <li value="[1]" id="ref1">Melanie Mitchell. 2021. Why AI is Harder Than We Think. DOI:<a href="https://doi.org/10.48550/arXiv.2104.12871">https://doi.org/10.48550/arXiv.2104.12871</a></li>
  <li value="[2]" id="ref2">D. McDermott. Artificial intelligence meets natural stupidity. <i>ACM SIGART Bulletin</i>, (57):4–9, 1976.</li>
  <li value="[3]" id="ref3">R. Thomas McCoy, Shunyu Yao, Dan Friedman, Matthew Hardy, and Thomas L. Griffiths. 2023. Embers of Autoregression: Understanding Large Language Models Through the Problem They are Trained to Solve. DOI:<a href="https://doi.org/10.48550/arXiv.2309.13638">https://doi.org/10.48550/arXiv.2309.13638</a></li>
  <li value="[4]" id="ref4">Iris van Rooij, Olivia Guest, Federico G. Adolfi, Ronald de Haan, Antonina Kolokolova, and Patricia Rich. 2023. “Reclaiming AI as a Theoretical Tool for Cognitive Science.” PsyArXiv. August 1. doi:<a href="https://osf.io/preprints/psyarxiv/4cbuv/">10.31234/osf.io/4cbuv</a>.</li>
</ol>