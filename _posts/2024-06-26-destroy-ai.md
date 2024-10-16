---
layout: post
title:  "Destroy 'AI', but keep designing with ML"
date:   2024-06-26
tags: research hci wikipedia design
excerpt: "Ali Alkhatib argues in a blog post that we should destroy AI. I see a few glimmers of hope."
---

The inimitable [Ali Alkhatib](https://ali-alkhatib.com/) published ["Destroy AI"](https://ali-alkhatib.com/blog/fuck-up-ai), a short and thought-provoking blog post.

>I'm finding myself fixated on articulating the moral case for sabotaging, circumventing, and destroying “AI”, machine learning systems, and their surrounding political projects as valid responses to harm.

Alkhatib argues that human-computer interaction (HCI) researchers have failed to oppose the capital-backed proliferation of "hegemonic algorithmic systems".

>I’ve come to feel like human-centered design (HCD) and the overarching project of HCI has reached a state of abject failure. ... The field’s inability to rise forcefully to the ascent of large language models and the pervasive use of chatbots as panaceas to every conceivable problem is uncharitably illustrative of its current state.

I agree with most of the blog, and it's a concise and compelling read.
However, I find myself not quite so pessimistic.
Here, I wanted to explore why by highlighting a few points of disagreement I have and why we might find hope in the broader HCD and HCI project.

### Data science for bureaucratic good?

A core tension in research (and life) is deciding when one should embrace an existing framing/system/politics in order to change it versus creating a new understanding in opposition to existing systems.

Alkhatib writes:

>There’s no way to make the administrative and bureaucratic systems of apartheid and violence more humane for the people subjugated by that system.

I think this is false, or at least incomplete.
Unthinkingly increasing the efficiency of automated systems does enable greater harms, but violent systems _can_ be made more humane by design. 
Visibility and contestability are two important system traits that can be improved using HCD.

Visibility enables understanding. Research like [Pythia](https://arxiv.org/abs/2304.01373) and [LLM Dataset Inference](https://arxiv.org/abs/2406.06443) enable people to make invisible harms describable. Contestability refers not to the specific design of a technology, but to the design of the surrounding social, legal, and political systems that enable and constrain that technology. By designing for contestability, we are implicitly operating within the bureaucracy: we aim to influence the design of the whole socio-technical system, rather than creating competing alternatives.

We have to be careful about when we choose to design within a system and when we choose to compete with it.

In ["Forking paths in LLMs for data analysis"](https://statmodeling.stat.columbia.edu/2024/06/24/forking-paths-in-llms-for-data-analysis/), Jessica Hullman writes about this tension: "how different people react when they see something in their domain of expertise that could be a train wreck starting to occur."

> Do you jump in and try to redirect it, or avoid the situation altogether? I guess in this case I'm advocating that at least some of the experts jump in.

Hullman's post also raises an important point about designing with algorithmic approaches intended to replace or supplement human labor:

>People sometimes resist the thought of formalizing the goals of some human-computer interaction, as if that automatically equates to taking agency from the human. .... When we leave things fully to the human at the highest level, that is also a design choice, one that usually makes problems harder to find because we're less clear on what we're looking for. So I tend to think that when the thought of formalizing or automating some task makes us prickly, it's probably something we could learn from thinking more about.

A critic might respond that formalizing and designing with 'AI' might not _automatically_ equate to taking agency from the human, but - in the context of hegemonic algorithmic systems - it is the expected outcome (cf. Brian Merchant, ["Understanding the real threat generative AI poses to our jobs"](https://www.bloodinthemachine.com/p/understanding-the-real-threat-generative)).
It is this risk that requires us to embrace conceptual work (like Nick Seaver's ethnographic research with [recommendation systems](https://press.uchicago.edu/ucp/books/book/chicago/C/bo183892298.html)) that enables us to understand where design can be useful and where it will merely enable more efficient harm.

### Designing is formalizing

The point I'm trying to make is that design work is one approach to formalizing and thus reasoning about human activities. Hullman writes that designing with ML systems "forces us to reflect a little harder on what exactly we think the human is doing/adding at each step".
It is that reflection that leads to work that expands rather than removes possibilities (like the [Glaze](https://arxiv.org/abs/2302.04222) and [data poisoning](https://dl.acm.org/doi/abs/10.1145/3442188.3445885) work that Alkhatib references).

By designing with ML, researchers can break down the hype-fueled concept of 'AI' and focus on creating humane, everyday technologies (like [tarmac]({% post_url 2024-05-19-ml-infrastructure %})).
'AI' is such an overloaded concept that we would do well to discard it, but discarding HCD with machine learning technologies risks throwing out the baby with the bathwater.
In particular, there is a significant cost to doing design and research work that _doesn't_ engage with the material reality of the socio-technical systems we're designing for.
Alkhatib is right to imply that most HCD work for "measuring and fixing" ML tech doesn't engage with the reality of how these systems are used and deployed, but some does!

I find hope for design with 'AI' by looking for research activities that are genuinely community-centered and bottom-up. My first stop is always Wikipedia.
There is so much low-hanging design work to be done on Wikipedia!
At the [Wiki Workshop](https://wikiworkshop.org) last week, I presented [ORES-Inspect](https://arxiv.org/abs/2406.08453), a web app for auditing one of the ML models used for vandalism detection on Wikipedia.
In many ways, auditing work represents the worst of HCD: a bandaid, tinkering on the edges while companies build and deploy ML models without concern for visibility or contestability.
But on Wikipedia, the bureaucracy is visible and participatory in ways that give me hope for designing more effective community-building and knowledge-sharing infrastructure.

I'm genuinely excited to see more applied research on circumvention, sabotage, and destruction of harmful systems, but that work will succeed or fail in part by the same standards as most existing HCD research: does it formalize and automate human activities in ways that support humans and prevent harms?
Alkhatib's post is a prescient challenge to drive to the root of the harms our systems can cause when we are designing with ML technologies.
I hope that HCI researchers will respond to this challenge by building systems that subvert hegemonic expectations and reflect the values of the communities we're hoping to support.
