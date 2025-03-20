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

_This post was based on a [tweet](https://twitter.com/zwlevonian/status/1387820787768315904)._

#### Makeism (added 2023-10-27)

Iris van Rooij et al. define the term _makeism_ {{ref4}}:

>Makeism: The view that computationalism implies that (_a_) it is possible to (re)make cognition computationally; (_b_) if we (re)make cognition then we can explain and/or understand it; and possibly (_c_) explaining and/or understanding cognition requires (re)making cognition itself.
>
>.... A well-known quote from [Feynman (1988)](https://digital.archives.caltech.edu/collections/Photographs/1.10-29/), “what I cannot create, I do not understand”, is often used to support the idea of makeism in AI (e.g. [Karpathy et al., 2016](https://web.archive.org/web/20180121082551/https://blog.openai.com/generative-models/)).
>
>Note that it is especially easy for makeists to fall into map-territory confusion—mistaking their modeling artefacts for cognition itself—due to the view that the made thing _could_ be cognition.

To my eyes, van Rooij et al.'s makeism is highly associated with a use of wishful mnemonics. Note in particular the argument around "map-territory confusion": this is a mistake that's easy to make when adopting the mnemonics for computational processes that McDermott laments, like using "UNDERSTAND" isntead of "G0034".

van Rooij et al. go even farther than McDermott and Mitchell, however, arguing that we are too easily convinced. 
In practice, "AIs appear human-like in non-rigorous tests, but the likeness is debunked when more rigorous tests are made .... This back and forth between claims of human-likeness and debunking (_cf._ Mitchell, 2021 {{ref1}}) will keep happening if the field does not realise that AI-by-learning is intractable, and hence any model produced in the short run is but a 'decoy'" {{ref4}}.

#### Critical Technical Practice (added 2025-03-20)

[Phil Agre](https://en.wikipedia.org/wiki/Philip_Agre) introduced the idea of [critical technical practice](https://en.wikipedia.org/wiki/Critical_technical_practice).

Writing in 1997, Agre argues that AI research primarily proceeds through the construction of _narratable systems_.

Here's Agre in _Toward a Critical Technical Practice: Lessons Learned in Trying to Reform AI_ {{ref5}}:

>The premise of AI, in rough terms, is the construction of computer systems that exhibit intelligence. One encounters different formulations of this premise at different labs, and from different individuals in the field. In philosophical and popular forums, the field is often discussed in terms of a seemingly fundamental question: Can computers think? But little of the field's day-to-day work really depends on the answer to such questions. As a practical matter, the purpose of AI is to build computer systems whose operation can be narrated using intentional vocabulary. Innovations frequently involve techniques that bring new vocabulary into the field: reasoning, planning, learning, choosing, strategizing, and so on. Whether the resulting systems really are exhibiting these qualities is hard to say, and AI people generally treat the question as an annoying irrelevance. What matters practically is not the vague issue of what the words "really mean," but the seemingly precise issue of how they can be defined in formal terms that permit suitably narratable systems to be designed. If you disapprove of the way that we formalize the concept of reasoning or planning or learning, they are likely to say, then you are welcome to invent another way to formalize it, and once you have gotten your own system working we will listen to you with rapt attention. If you disapprove of the very project of formalization, or if you insist on sensitivity to the ordinary vernacular uses of the words (e.g., [Button, Coulter, Lee, & Sharrock, 1995](https://archive.org/details/isbn_9780745615714/mode/2up)), then, they would argue, you are simply an obscurantist who prefers things to remain vague.

Agre clarifies:

>The strategic vagueness of AI vocabulary, and the use of technical schemata to narrate the operation of technical artifacts in intentional terms, is not a matter of conscious deception.

This vagueness has two effects:
 - It permits AI methods "to seem broadly applicable, even when particular applications require a designer to make, often without knowing it, some wildly unreasonable assumptions". Good for marketing!
 - It prevents designers from conceptualizing "alternatives to their existing repertoire of technical schemata". Bad for innovation.

Agre points out that this rhetorical environment makes _recognizing_ innovation challenging.

>AI's elastic use of language ensures that nothing will seem genuinely new, even if it actually is, while AI's intricate and largely unconscious cultural system ensures that all innovations, no matter how radical the intentions that motivated them, will turn out to be enmeshed with traditional assumptions and practices. When AI people look at an innovation and pronounce it nothing radically new, they will be wrong in some ways and right in others, and it will require tremendous effort to determine which is which. 

Agre argues that this is where critical technical practice comes in: sorting through "innovations" that have novel technical value but are perceived as nothing new from "innovations" that have nice narratives but offer nothing much useful.

It is fundamentally challenging to recognize genuine innovation. As Agre points out:

>Having coupled a new technical method with a new way of talking about the phenomena, it is difficult to apply the method to any real cases without inventing a lot of additional methods as well, since any worthwhile system will require the application of several interlocking methods, and use of the existing methods may distort the novel method back toward the traditional mechanisms and the traditional ways of talking about them.

### References

<ol class="reference-block">
  <li value="[1]" id="ref1">Melanie Mitchell. 2021. Why AI is Harder Than We Think. DOI:<a href="https://doi.org/10.48550/arXiv.2104.12871">https://doi.org/10.48550/arXiv.2104.12871</a></li>
  <li value="[2]" id="ref2">D. McDermott. Artificial intelligence meets natural stupidity. <i>ACM SIGART Bulletin</i>, (57):4–9, 1976.</li>
  <li value="[3]" id="ref3">R. Thomas McCoy, Shunyu Yao, Dan Friedman, Matthew Hardy, and Thomas L. Griffiths. 2023. Embers of Autoregression: Understanding Large Language Models Through the Problem They are Trained to Solve. DOI:<a href="https://doi.org/10.48550/arXiv.2309.13638">https://doi.org/10.48550/arXiv.2309.13638</a></li>
  <li value="[4]" id="ref4">Iris van Rooij, Olivia Guest, Federico G. Adolfi, Ronald de Haan, Antonina Kolokolova, and Patricia Rich. 2023. “Reclaiming AI as a Theoretical Tool for Cognitive Science.” PsyArXiv. August 1. doi:<a href="https://osf.io/preprints/psyarxiv/4cbuv/">10.31234/osf.io/4cbuv</a>.</li>
  <li value="[5]" id="ref5">Agre, P. 1998. <a href="https://www.taylorfrancis.com/chapters/edit/10.4324/9781315805849-8/toward-critical-technical-practice-lessons-learned-trying-reform-ai-philip-agre">Toward a Critical Technical Practice: Lessons Learned in Trying to Reform AI.</a> Bowker, G., Bowker, G., Star, S.L., Gasser, L., & Turner, W. (Eds.). Social Science, Technical Systems, and Cooperative Work: Beyond the Great Divide (1st ed.). Psychology Press. doi:<a href="https://doi.org/10.4324/9781315805849">10.4324/9781315805849</a>. Available from <a href="https://pages.gseis.ucla.edu/faculty/agre/critical.html">https://pages.gseis.ucla.edu/faculty/agre/critical.html</a>.</li>
</ol>