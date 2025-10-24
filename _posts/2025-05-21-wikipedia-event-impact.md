---
layout: post
title:  "How does Wikipedia article quality impact decision-making?"
tags: research wikipedia football law short
excerpt: "A randomized experiment on Irish judges and a Wiki Workshop 2025 paper on the NFL draft."
---
<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true });
</script>

The [_Wikipedia Signpost_](https://en.wikipedia.org/wiki/Wikipedia:Wikipedia_Signpost/2025-05-14/In_the_media) pointed me to a fun research controversy.

Thompson et al. conducted a [randomized controlled trial](https://en.wikipedia.org/wiki/Randomized_controlled_trial) to examine the impact of Wikipedia article quality on the probability of a particular court case being cited as precedent in Irish judges' rulings.
In other words, are judges more likely to cite a ruling that has a Wikipedia article?
The papers chose 154 court cases without articles and had law students upload new articles for half of them.
Lo and behold, articles with Wikipedia pages were subsequently cited more.

As you can imagine, Irish judges were not happy about this finding and disputed it vigorously.
Their criticisms mostly miss the mark, and the authors' response to this criticism is very much worth a read.

- The original paper: ["Trial by Internet: A Randomized Field Experiment on Wikipedia’s Influence on Judges’ Legal Reasoning"](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4174200)
- The authors' response to criticism: ["Trial by Internet: A Response to Judicial Critics"](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5248329)
- Also covered [in _The Irish Times_](https://www.irishtimes.com/crime-law/2025/05/12/authors-of-paper-claiming-irish-judges-use-wikipedia-as-a-source-for-rulings-dispute-flawed-research-criticisms/)

As Wikipedia is one of the most visited websites, it probably shouldn't surprise us that the information on Wikipedia would influence real-world behavior.
Previous studies have found that [improving Wikipedia articles can increase tourism](https://onlinelibrary.wiley.com/doi/abs/10.1111/jems.12421) and that papers referenced in Wikipedia articles [get more academic citations](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3039505).

I suspect we would see similar impacts in many domains if we randomly improved some articles and not others.

### Predicting the future with Wikipedia?

One potential impact of Wikipedia article quality is on future events that involve decisions – like elections, [Eurovision](https://en.wikipedia.org/wiki/Eurovision_Song_Contest), or the [NFL draft](https://en.wikipedia.org/wiki/NFL_draft).

The basic idea is that the content of Wikipedia articles that are related to an event affects the information that decision-makers are exposed to, which in turn affects the decisions made during that event.

<div class="mermaid" style="display: flex; justify-content: center;">
flowchart LR 
    A[Wikipedia article] --> B[Information]
    B --> C[Decision]
</div>

I attended [WikiWorkshop 2025](https://meta.wikimedia.org/wiki/Wiki_Workshop_2025/Attendees) this morning, which is a fun little virtual conference where people present small or in-progress research related to Wikipedia. In it, MS student Jordan Kesner presented ["Playbooks and Pageviews: How Wikipedia’s NFL Pages Reveal the Evolution of Digital Fandom"](https://wikiworkshop.org/2025/paper/wikiworkshop_2025_paper_40.pdf), a look at editing of prospective NFL player biographies on the English Wikipedia.

Kesner trains a logistic regression model to predict whether a player will be selected in the first round of the [NFL draft](https://en.wikipedia.org/wiki/NFL_draft), achieving 80% accuracy based _only on Wikipedia editing behaviors on each player's Wikipedia biographies_.

We probably shouldn't be surprised by this predictability, as Wikipedia articles are supposed to reflect what other sources already say about the subject.
Perhaps Wikipedia is just serving as a crude proxy for the amount of coverage a player gets: more coverage = better Wikipedia article = more likely to get picked in the first round.
It would be interesting to attempt to control for the amount of non-Wikipedia coverage available for a player to isolate out the impact of Wikipedia article quality specifically on event outcomes.

I suspect we would only find a substantial effect in cases where Wikipedia article quality is much lower than it could be. For example, in that [tourism research](https://www.econstor.eu/handle/10419/173092) I mentioned above, the authors mention that most of the effect on tourism was the result of bringing low-quality articles up to par; turning good articles into great articles may be less important than turning bad articles into good articles.

If true, that would give us some comfort that Wikipedia itself is not having a major impact on future events that attract lots of attention already, like elections.
However, we might still see big causal impacts of Wikipedia editing on smaller, regional elections or for events where a single motivated editor can have an outsized impact on the information presented on Wikipedia.

Personally, I would love to see additional research attempting to tease out the causal impact of Wikipedia editing on behavior in a variety of information-driven decision-making contexts.
