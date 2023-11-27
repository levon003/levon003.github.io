---
layout: post
title:  Graphing Shakespeare and dramatizing data
date:   2023-11-26
tags: research
excerpt: Coupette et al.'s paper "All the world’s a (hyper)graph"
---
{% include references.html %}

Corinna Coupette, Jilles Vreeken, and Bastian Rieck released a paper titled "All the world’s a (hyper)graph: a data drama" {{ref1}}.

I'd recommend reading the paper just because of its format: as a Shakespearean play.
No iambic pentameter, but characters are introduced and stage directions are given. 
Here's an excerpt, highlighting the core argument of the paper about the varied decisions made by researchers when constructing graphs from data.

>When we transform reality to math,
>
>Graphs are but outputs, in—phenomena.
>
>The myriad transformations that we see,
>
>How do they differ systematically?
>
>For now, we shall distinguish three dimensions.
>
>First, our **semantic mapping**—Nodes and edges:
>
>What types of entities do we assign?
>
>Second, our **granularity**—What are
>
>Our modeling units for semantic mapping?
>
>And third, our **expressivity**: What more
>
>Do we attach to all our modeling units?
>
>Directions, weights, and multiplicities,
>
>Or attributes and cardinalities. . .
>
>What universe! *Haec facta, fiant data.*

I call the process the authors are describing here ["operationalizing"](https://ojs.aaai.org/index.php/ICWSM/article/view/7310); taking our theoretical understanding of a phenomena and using it to motivate choices about how we model the construct we're interested in. They identify three aspects that are salient when operationalizing graphs.

 1. Semantic mapping - what entities get assigned to nodes and edges
 2. Granularity - the "unit" used to do the semantic mapping
 3. Expressivity - what metadata about nodes and edges we include

 In their example, they choose to define nodes as "characters in a given Shakespeare play" and edges as "co-occurrence": that's the semantic mapping. Granularity involves defining the units: characters have at least one spoken line, co-occurrence means speaking in the same scene. 
 Expressivity involves enriching the graphs perspective to capture the phenomena at the cost of added complexity: in this case, adding edge weights corresponding to the number of lines spoken in a scene.

 The core observation of the paper is that these modeling choices admit many possibilities, and they suggest adopting a hypergraph perspective to capture some of the multiplicities involved in operationalizing data into a graph and analyzing that graph.

 In my own work {{ref3}}, I remember feeling very frustrated making decisions about how to construct a graph from online social interaction data. It was hard to tell which graph modeling decisions were consequential for my analysis and which were not.
 If I was going to do that study again, I would consider using some of the hypergraph modeling and visualization approaches described in the paper (and repleased in the [`hyperbard`](https://github.com/hyperbard/hyperbard) Python implementation).

The choice of a playful presentation format for a genuine research topic reminds me of publications in [alt.CHI](https://kieranbrowne.com/research/altchi-2020-a-readers-guide/); I wish more venues would be open to this kind of experimentation and [non-standard academic forms](https://osf.io/preprints/psyarxiv/2uxwk/) for publication. 
(My favorite alt.CHI paper is McNutt et al.'s "Divining Insights" {{ref2}}, which doesn't mess much with form but is a lovely research provocation.)

### References

<ol class="reference-block">
  <li value="[1]" id="ref1">Corinna Coupette, Jilles Vreeken, Bastian Rieck, <a href="https://academic.oup.com/dsh/advance-article/doi/10.1093/llc/fqad071/7429467">All the world’s a (hyper)graph: A data drama</a>, <em>Digital Scholarship in the Humanities</em>, 2023, <a href="https://doi.org/10.1093/llc/fqad071">https://doi.org/10.1093/llc/fqad071</a></li>
  <li value="[2]" id="ref2">Andrew McNutt, Anamaria Crisan, and Michael Correll. 2020. <a href="https://dl.acm.org/doi/10.1145/3334480.3381814">Divining Insights: Visual Analytics Through Cartomancy</a>. In Extended Abstracts of the 2020 CHI Conference on Human Factors in Computing Systems (CHI EA '20). Association for Computing Machinery, New York, NY, USA, 1–16. <a href="https://doi.org/10.1145/3334480.3381814">https://doi.org/10.1145/3334480.3381814</a></li>
  <li value="[3]" id="ref3">Zachary Levonian, Marco Dow, Drew Erikson, Sourojit Ghosh, Hannah Miller Hillberg, Saumik Narayanan, Loren Terveen, and Svetlana Yarosh. 2021. <a href="https://arxiv.org/abs/2007.16172">Patterns of Patient and Caregiver Mutual Support Connections in an Online Health Community</a>. <em>Proc. ACM Hum.-Comput. Interact.</em> 4, CSCW3, Article 275 (December 2020), 46 pages. <a href="https://doi.org/10.1145/3434184">https://doi.org/10.1145/3434184</a></li>
</ol>