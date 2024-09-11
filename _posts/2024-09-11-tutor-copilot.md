---
layout: post
title:  "Tutor Co-pilot: real-time scaffolding for peer tutors"
date:   2024-09-11
tags: research short
excerpt: "A project at PLUS using large language models for real-time support."
---

I recently implemented a Tutor Co-pilot in collaboration with the team at Carnegie Mellon working on [PLUS](https://www.tutors.plus/en/). PLUS (Personalized Learning Squared) is training and management software for math tutors.

I recently implemented Tutor Co-pilot with the PLUS team, a feature to provide real-time scaffolding for math problems.

[According to instructor Rebecca Alber](https://www.edutopia.org/blog/scaffolding-lessons-six-strategies-rebecca-alber):

> _Scaffolding_ is breaking up the learning into chunks and providing a tool, or structure, with each chunk.

The Tutor Co-pilot works by having tutors copy-paste or upload a screenshot of the problem a student is working on. The Tutor Co-pilot then shows a structured table with three columns:
 - Steps: a step-by-step guide on how to solve the problem
 - Tell The Student: a bit of positive reinforcement appropriate to that step of the problem
 - Ask The Student: an open-ended, strategic question motivating students to actively participate and think independently about the problem-solving goal

Tutors choose what they want to use from the table to improve their communication with students about that math problem.

Naturally, we used large language models (LLMs) to actually generate the table we show to students.
One advantage of the "Co-pilot" design is that it's acceptable (but not preferable) to show hallucinations to tutors in a way that it isn't for students. The tutor will always serve as a buffer between the LLM output and the student.
For the tutor, Tutor Co-pilot can function as a safety net for moments when they find themselves unsure or stuck.

I worked closely with designers Tina Chen and Zhiyuan Chen on Tutor Co-pilot. Tina has a more detailed write-up about the design process [on her website](https://www.tinachen.work/tutor-co-pilot).

A use of LLMs that I did _not_ expect for this project was during the first phase of design. Tina and Zhiyuan used multiple LLMs to generate initial seed ideas for discussion, rather than processes I've used before like [IDEO's brainstorming process](https://www.ideou.com/pages/brainstorming).
This idea is really intriguing, although I'm a bit skeptical.
["Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers"](https://arxiv.org/abs/2409.04109) (2024) explored the use of LLMs for research idea generation and argued that LLMs produced ideas that were more novel but less technically feasible.
I'm sure there's a lot more work going on in this space right now, and I'm curious to see how LLMs will best fit into the early design process.
