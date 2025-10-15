---
layout: post
title:  "So, you've decided to design an educator feedback interface"
tags: [design, education, research, roundup, short]
excerpt: "Research papers related to the design of teacher or tutor feedback interfaces."
---

The _educator feedback interface_ is an increasingly common research and product idea:
 1. Record educator interactions with students
 2. Analyze the recordings
 3. Visualize the analysis outputs in some kind of report

Sometimes the educators in question are teachers, but they can also be trained tutors, peer tutors, counselors, or coaches.

There are many options for analyzing recordings. Here are a few outputs I've seen:
 - Positive or negative interactions _e.g._ student break-through moments
 - Quantitative metrics for particular educator behaviors _e.g._ percentage of questions that are open-ended, educator:student talk-time ratio
 - Quantitative metrics for particular student behaviors _e.g._ verbal expressions of frustration
 - Opportunities for additional individual help _e.g._ slow progress with an individual
 - Opportunities for professional development _e.g._ missed opportunities for making connections in the material
 - etc.

The report itself can be intended for self-analysis, but sometimes it's intended for use by supervisors or trainers.

A few examples:
 - A teacher dashboard that helps you monitor a group of peer tutors to determine if they're interacting appropriately with peers.
 - A tips report for new teachers that points out opportunities to handle student interactions differently.
 - A district-level report on teacher's classroom behaviors.

All of these designs raise various ethical and design issues _e.g._ around surveillance.
However, I've noticed that design proposals for new educator feedback interfaces seem to stumble into the same issues repeatedly.

It doesn't have to be this way! 
While I'm not aware of detailed case studies examining educator feedback interfaces, there is a growing body of research describing experiences with and ideas for educator feedback interfaces.
This post is a quick round-up of papers that address the design and implementation of educator feedback interfaces.
If you're going to start implementing your own educator feedback interface, I suggest looking at some of these sources; you might find some useful inspiration.

Here's a quick source round-up:

- [Talk Moves](https://www.talkmoves.com/) classification and tutor coaching interface – This is focused on the supervisor side _i.e._ creating quantitative data visualizations for supervisors (”coaches” in their context) rather than interfaces for use by teachers or tutors.
    - <https://dl.acm.org/doi/abs/10.1145/3636555.3636937>
    - <https://link.springer.com/chapter/10.1007/978-3-031-98420-4_4>
- Teacher feedback tools – a smattering of papers directly addressing the problem of showing teachers feedback on their performance.
    - From Dora Demszky at Stanford: <https://dl.acm.org/doi/10.1145/3573051.3593379> and <https://dl.acm.org/doi/10.1145/3636555.3636924> (both link other papers that may be useful)
    - <https://link.springer.com/article/10.1007/s40593-024-00417-x>
    - <https://www.sciencedirect.com/science/article/abs/pii/S0742051X22000026>
    - A more NLP perspective (less focused on specific interfaces but provides useful context): <https://aclanthology.org/2023.bea-1.53/>
- Review papers – no review papers yet in this field. That's sad – we don’t have a mature body of research to work from – but also exciting – we get to use our design instincts and try things!
    - Here’s a review paper from MDPI: <https://www.mdpi.com/2076-3417/15/12/6911> MDPI papers are [often low quality](https://www.predatoryjournals.org/news/is-mdpi-predatory), but it can still be useful to skim them to see how they break down an area of research.
