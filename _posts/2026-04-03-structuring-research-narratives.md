---
layout: post
title:  "Structuring research narratives"
tags: research writing
excerpt: "How to structure research narratives for talks, papers, and posters"
image: /images/appleton_openings.webp
---
<style>
  /* ---------- annotated-abstract ---------- */
  .annotated-abstract {
    font-family: Georgia, "Times New Roman", serif;
    line-height: 1.7;
    background: transparent;
  }

  .annotated-abstract .label {
    display: inline-block;
    font-family: -apple-system, system-ui, "Segoe UI", Helvetica, Arial, sans-serif;
    font-size: 0.65em;
    font-weight: 600;
    letter-spacing: 0.02em;
    padding: 0.05em 0.45em;
    border-radius: 999px;
    vertical-align: middle;
    margin-right: 0.25em;
    line-height: 1.5;
    white-space: nowrap;
  }

  .annotated-abstract .sentence {
    border-radius: 3px;
    padding: 0.1em 0.25em;
    margin-right: 0.15em;
  }

  /*
    Color palette — each category gets:
      --pill-bg / --pill-fg  → label pill
      --sent-bg              → sentence highlight

    These are intentionally muted so they read well on both white
    and dark backgrounds. In dark mode we just nudge opacity/lightness.
  */

  /* 1 · Background / Setting — slate blue */
  .cat-background .label { background: #4a6fa5; color: #fff; }
  .cat-background .sentence { background: rgba(74, 111, 165, 0.12); }

  /* 2 · Societal Problem — warm rose */
  .cat-society .label { background: #b5485a; color: #fff; }
  .cat-society .sentence { background: rgba(181, 72, 90, 0.12); }

  /* 3 · Technical Problem — amber */
  .cat-techproblem .label { background: #b8860b; color: #fff; }
  .cat-techproblem .sentence { background: rgba(184, 134, 11, 0.12); }

  /* 4 · Technical Solution — teal */
  .cat-techsolution .label { background: #2a9d8f; color: #fff; }
  .cat-techsolution .sentence { background: rgba(42, 157, 143, 0.12); }

  /* 5 · Societal Benefit — green */
  .cat-benefit .label { background: #548c3a; color: #fff; }
  .cat-benefit .sentence { background: rgba(84, 140, 58, 0.12); }

  /* 6 · Roadmapping — purple */
  .cat-roadmap .label { background: #7b5ea7; color: #fff; }
  .cat-roadmap .sentence { background: rgba(123, 94, 167, 0.12); }

  /* 7 · Details — steel */
  .cat-details .label { background: #6b7d8a; color: #fff; }
  .cat-details .sentence { background: rgba(107, 125, 138, 0.12); }

  /* ---- Dark-mode overrides ---- */
  @media (prefers-color-scheme: dark) {
    .annotated-abstract {
      border-left-color: #666;
    }
    .cat-background .label  { background: #5b83be; }
    .cat-background .sentence { background: rgba(91, 131, 190, 0.18); }

    .cat-society .label { background: #cf6275; }
    .cat-society .sentence { background: rgba(207, 98, 117, 0.18); }

    .cat-techproblem .label { background: #d4a017; }
    .cat-techproblem .sentence { background: rgba(212, 160, 23, 0.18); }

    .cat-techsolution .label { background: #3bc0ad; }
    .cat-techsolution .sentence { background: rgba(59, 192, 173, 0.18); }

    .cat-benefit .label { background: #6aad4e; }
    .cat-benefit .sentence { background: rgba(106, 173, 78, 0.18); }

    .cat-roadmap .label { background: #9678c2; }
    .cat-roadmap .sentence { background: rgba(150, 120, 194, 0.18); }

    .cat-details .label { background: #839bab; }
    .cat-details .sentence { background: rgba(131, 155, 171, 0.18); }
  }
</style>

The story you tell about your research _is_ the research.
The narrative you share with the research community is how your findings are understood by others; without a story, there is no research.

Research papers are the most common medium for presenting research stories, but talks, posters, and hallway conversations all involve making choices about how to structure your research narrative.

Learning to structure research narratives doesn't come naturally, and it's one of the things you'll learn during a PhD.
Many researchers learn by imitating the structure of existing abstracts or Introduction sections, but I find it's really useful to have a rough framework in mind.
What follows is the framework I use, as taught to me by [Mike Wittie](https://mwittie.io/) during a 2012 [REU program](https://en.wikipedia.org/wiki/Research_Experiences_for_Undergraduates).
I would think about this framework like the [five-paragraph essay](https://en.wikipedia.org/wiki/Five-paragraph_essay): a structure that helps you produce a reasonable argument, but overly restrictive once you get more experience structuring research narratives.

## A framework for structuring research narratives

The framework has four components:

 1. Societal Problem
 2. Technical Problem
 3. Technical Solution
 4. How the Solution Helps Society

### Societal problem

The **societal problem** tells us how the world is lacking.

The society in question can be as broad as you choose, from all of humanity to a small group of researchers, engineers, or practitioners trying to accomplish something.

A problem must – in principle – be solvable.

The problem should be as specific as you can make it for the audience you have in mind. "Food insecurity exists" _is_ a societal problem, but "food distribution networks cannot meet existing needs" is more appropriate if the research you conducted is specific to food distribution.

### Technical problem

The **technical problem** is why we can't just _fix_ the societal problem.

The technical problem is the domain-specific problem contained within the broader problem that is amenable to attack by our discipline's methods.

Resolving the technical problem should recognizably move us closer to solving the societal problem.

The line between the societal problem and the technical problem is necessarily fuzzy. In general, you should start with a problem recognizable to any member of your audience and take argumentative steps toward a concrete technical problem specific to your discipline.

The societal problem and technical problem together are your strongest motivations for conducting this research. There may be other motivations that you mention incidentally or while discussing how your research relates to prior work, but lead with your strongest argument and ensure that addressing the technical problem clearly addresses the societal problem.

### Technical solution

The **technical solution** is how our research fixes the identified technical problem.

Your solution should correspond clearly to the points you raised in the technical problem. If your technical solution seems to respond to a broader or more narrow problem than your technical problem suggests, that's a good indicator that you should rework the technical problem or consider presenting less of the work.

For in-progress work, it works fine for the technical solution to be tentative or incomplete; by explicitly characterizing the technical problem you're trying to solve, you make it obvious where the holes are in your solution.

It can be appropriate for the technical solution to include only a brief teaser of your research work. In longer formats, it is fine to include additional details about the methods you used and your results alongside the technical solution.

### How the solution helps society

**How the solution helps society** draws us back from the specifics of your solution to the new state of the societal problem following your research.

If you discussed specific results while describing your technical solution, you should link those results to specific changes for researchers or practitioners who are facing the same societal problem.

Describing the societal benefit can be very brief, but you must do it: remind your reader where you started, or you'll be left with an incomplete narrative.

## Arguments to avoid

Choosing an appropriate societal problem and technical problem is important because these communicate your core motivations for conducting the research. Unconvincing or vague motivations will leave your audience confused about the potential value of your research.

Here are two common 'bad' arguments to avoid:

### "X is hard"

Why haven't we fixed the societal or technical problem yet? Well, because they're hard problems!

Consider this argument:

<blockquote class="annotated-abstract">
    <span class="cat-society"><span class="label">Societal problem</span> <span class="sentence">Lack of access to food causes human misery. Food distribution networks can provide access, but designing and implementing these networks is challenging.</span></span>
    <span class="cat-techproblem"><span class="label">Technical problem</span> <span class="sentence">Networks need stable supply chain data to distribute food.</span></span>
    <span class="cat-techsolution"><span class="label">Technical solution</span> <span class="sentence">We propose a new method for collecting and structuring supply chain data.</span></span>
    <span class="cat-benefit"><span class="label">How the solution helps society</span> <span class="sentence">Our method enables food distribution networks to operate more efficiently and so increase access to food.</span></span>
</blockquote>

Instead, we should be more specific about _why_ these problems are challenging.

<blockquote class="annotated-abstract">
    <span class="cat-society"><span class="label">Societal problem</span> <span class="sentence">Food distribution networks can provide access to food, but designing effective networks depends on access to stable supply chain data.</span></span>
    <span class="cat-techproblem"><span class="label">Technical problem</span> <span class="sentence">Suppliers provide data in diverse formats or not at all.</span></span>
    <span class="cat-techsolution"><span class="label">Technical solution</span> <span class="sentence">We propose a new method for collecting and structuring supply chain data.</span></span>
    <span class="cat-benefit"><span class="label">How the solution helps society</span> <span class="sentence">Our method enables food distribution networks to operate more efficiently and so increase access to food.</span></span>
</blockquote>

Sharpening the societal problem and specifying a concrete cause forced us to be more specific about the technical problem we actually solved.

When you feel tempted to make an "X is hard" argument, that's usually a sign that your argument is too high-level. That can be okay for an elevator pitch, but you can make a stronger argument by being specific about _what_ is hard.

### Research gaps

One common piece of advice is to identify a ["research gap"](https://libanswers.snhu.edu/faq/264001): a research question that hasn't yet been addressed in the published literature.

However, research gaps make for ineffective motivations.

As Casey Fiesler [writes on Bluesky](https://bsky.app/profile/cfiesler.bsky.social/post/3lmursrhukc2b):

>I would love to never see the phrase "little is known about" in a paper ever again.
>
>(1) Most of the time the authors are far more confident about that statement than they should be.
>
>(2) There are lots of things we know little about because no one cares. Just not knowing isn't a good motivation.

Fiesler is correct: "there's a gap" is not a compelling justification for doing research.
It _is_ good to notice when there are gaps, but you should first ask: 

>_Why_ is there a gap?

Use the answer to that question as your technical problem instead.

## Example: My first paper

Let's look at the abstract from my first paper and see how well I followed this framework.

The paper was called ["Bridging Qualitative and Quantitative Methods for User Modeling: Tracing Cancer Patient Behavior in an Online Health Community"](https://ojs.aaai.org/index.php/ICWSM/article/view/7310), and it proposed a new method for researchers to use when constructing quantitative [user models](https://en.wikipedia.org/wiki/User_modeling).
This is a hard test for this framework, because the contribution – and thus my motivations – were very conceptual.

Here's the abstract, with annotations added:

<blockquote class="annotated-abstract">
    <span class="cat-society"><span class="label">Societal problem</span> <span class="sentence">Researchers construct models of social media users to understand human behavior and deliver improved digital services. Such models use conceptual categories arranged in a taxonomy to classify unstructured user text data.</span></span>
    <span class="cat-techproblem"><span class="label">Technical problem</span> <span class="sentence">In many contexts, useful taxonomies can be defined via the incorporation of qualitative findings, a mixed-methods approach that offers the ability to create qualitatively-informed user models. But operationalizing taxonomies from the themes described in qualitative work is non-trivial and has received little explicit focus.</span></span>
    <span class="cat-techsolution"><span class="label">Technical solution</span> <span class="sentence">We propose a process and explore challenges bridging qualitative themes to user models, for both operationalization of themes to taxonomies and the use of these taxonomies in constructing classification models.</span></span>
    <span class="cat-details"><span class="label">Method details</span><span class="sentence">For classification of new data, we compare common keyword-based approaches to machine learning models. We demonstrate our process through an example in the health domain, constructing two user models tracing cancer patient experience over time in an online health community.</span></span>
    <span class="cat-benefit"><span class="label">How the solution helps society</span> <span class="sentence">We identify patterns in the model outputs for describing the longitudinal experience of cancer patients and reflect on the use of this process in future research.</span></span>
</blockquote>

Overall, I think this abstract is _okay_.

- My societal problem is expressed very _implicitly_. That can be okay, but I could consider an explicit frame instead: "Models of social media users without valid conceptual categories can produce misunderstandings and lead to ineffective designs."
- The technical problem uses _both_ of the arguments to avoid: I say the process is hard and that there's a research gap! Instead, I should be specific: "But operationalizing taxonomies from the themes described in qualitative work requires a process that can bridge from the thematic to the concrete."
- My description of the technical solution is vague, although I think that's mostly okay in an abstract.
- My description of how the solution helps society is too vague. I should tie it back to the problems I identified more explicitly: "Our process creates quantitative user models that are both useful and valid."

If I had used this framework more explicitly, I would have produced a stronger abstract! Here's a revised version:

<blockquote class="annotated-abstract">
    <span class="cat-society"><span class="label">Societal problem</span> <span class="sentence">Quantitative models of social media users without valid conceptual categories can produce misunderstandings and lead to ineffective designs.</span></span>
    <span class="cat-techproblem"><span class="label">Technical problem</span> <span class="sentence">In many contexts, useful category taxonomies can be defined via the incorporation of qualitative findings, a mixed-methods approach that offers the ability to create qualitatively-informed user models. But operationalizing taxonomies from the themes described in qualitative work requires a process that can bridge from the thematic to the concrete.</span></span>
    <span class="cat-techsolution"><span class="label">Technical solution</span> <span class="sentence">We propose a process and explore challenges bridging qualitative themes to user models, for both operationalization of themes to taxonomies and the use of these taxonomies in constructing classification models.</span></span>
    <span class="cat-details"><span class="label">Method details</span><span class="sentence">For classification of new data, we compare common keyword-based approaches to machine learning models. We demonstrate our process through an example in the health domain, constructing two user models tracing cancer patient experience over time in an online health community.</span></span>
    <span class="cat-benefit"><span class="label">How the solution helps society</span> <span class="sentence">Our process produces user models with qualitatively-grounded categories that better capture user behavior and are more useful for researchers.</span></span>
</blockquote>

## Using this framework

I try to use this framework as early as possible in a research project. I'll write four high-level bullet points and see if I find the narrative compelling even without detail. Each month, I return to my bullet points, revising them to be more specific and to see how my thinking about the research has changed.

Research abstracts lend themselves well to this framework, since an abstract should usually serve as a brief summary of the research narrative. But abstracts can include other details as well (listings of results, calls to action, important related work), so I like to keep a "clean" version of the narrative for any research project I'm working on.

In longer formats, such as a research talk or an Introduction section, you might choose to include more or less detail in each component of this framework. 
It can be fine to start with a smaller "abstract" version of your research narrative – essentially functioning as a roadmap – or to introduce only the societal problem initially.
Highly conceptual work might require significant exposition before the audience can even understand the technical problem. 
For example, many pure math talks are 80% "technical problem", with a sliver of higher-level context at the start and a final theorem presented at the end, with details left to a longer-form write-up.

## Other frameworks

There are many frameworks for structuring research narratives. While writing up this post, I stumbled on Maggie Appleton's notes on ["On Opening Essays, Conference Talks, and Jam Jars"](https://maggieappleton.com/openings), which uses a very similar narrative framing.

![Flowchart: a problem needs solutions. A status quo is changed, which has consequences for a community of people.](/images/appleton_openings.webp)
*Maggie Appleton's beautiful figure adapting Joseph Williams' writing on problem structure.*

I was taught to write abstracts by John Carlis' ["Thinking about Abstracts"](https://wacclearinghouse.org/proceedings/iwac2014/presentations/8A-carlis-paper.pdf).
He breaks down the story of a research abstract into a set of "sentence purposes", and several of his examples strongly resemble the framework above. But Carlis makes an important point: there's nothing sacred about a particular narrative structure.
The framework above aligns with researcher expectations that are highly applicable to the fields I know well, but other fields can have very different expectations regarding research stories.

>A good abstract tells a story. Furthermore, the parts of the story appear in a sensible order, one commonly seen by its (limited) audience. It, therefore, meets its readers' expectations. When writing my own abstracts or helping others, I find that stating the purpose(s) of each sentence helps me see the story's flow from a reader's point of view, and readily find flaws in the story. If you think of an abstract as telling a story, then of course only some content and orderings are effective, and you can judge when content and order works or doesn't.

When you start to diverge from the structure I present above, ask yourself: does this meet my readers' expectations? Does my story 'work'?

## Other resources

 - ["10 tips for academic talks"](https://matt.might.net/articles/academic-presentation-tips/). See the section on "Motivation" in particular.
 - ["Ten simple rules for structuring papers"](https://www.biorxiv.org/content/10.1101/088278v5.full)
 - Eugene Yan's ["Frequently Asked Questions about My Writing Process"](https://eugeneyan.com/writing/writing-faq/) – Includes a nice set of resources related to writing at the bottom of the post

## Related posts

 -  [Peer reviewing]({% post_url 2025-03-07-peer-review %})
 -  [Common academic writing pitfalls]({% post_url 2024-01-31-academic-writing %})

