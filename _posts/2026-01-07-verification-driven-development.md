---
layout: post
title:  "Verification-driven development: using large language models for software development"
tags: [llm, code, agents, roundup, short]
excerpt: "Doll's verification-driven development approach."
---

Software developer [Doll](https://bsky.app/profile/dollspace.gay) has recently been posting on Bluesky about its process for using large language models agents to create verifiable software.

Doll [was challenged](https://bsky.app/profile/dollspace.gay/post/3mblunsref224) by applied mathematician Maxine Levesque to produce a tool outside of Doll's expertise:

>Write a Python package that does multivariate Nadaraya-Watson and local polynomial kernel regression with homo-/heteroscedastic goodness of fit checking and automatic crossvalidated order and bandwidth selection as an sklearn (fit/predict) compatible class.
>
>From experience this is like a two-week task for a competent third year grad student in applied data science.

(In my opinion, "two-week task" is very optimistic, but it depends on how polished or engineered you expect code written by data science Master's students to be.)

In response, Doll produced [this package](https://github.com/dollspace-gay/package) in a few hours, and in my opinion this is a good solution to the problem.

Doll calls this approach ["verification-driven development"](https://gist.github.com/dollspace-gay/45c95ebfb5a3a3bae84d8bebd662cc25) (VDD).

Here's my understanding of verification-driven development:

 1. Decomposition – Given a software goal, decompose the goal into a hierarchy of epics, issues, and sub-issues.
 2. Implementation – LLM uses the goal decomposition to create the codebase and a set of unit and integration tests.
 2. Verification – A human iteratively refines the software interface and the unit/integration tests until satisfied.
 3. Refinement
    a. Adversarial critique – A separate LLM with a fresh context window generates a critique of the codebase.
    b. Feedback integration – The LLM software agent selectively incorporates accurate feedback.
    c. Exit criteria – If the software agent determines that 75% of the issues in the critique are false positives, we exit the refinement loop.

As I read it, the basic intuition behind this approach is:

 - Enforce test coverage at the Implementation phase to correspond to the work units in the task decomposition.
 - Incorporate formal verification tools where possible; the adversarial LLM should use static analysis tools as a component of its critique generation.
 - Keep human focus on the software interface (the features) and the integration tests (are we actually testing the features in a reasonable way?).
 - Accept that LLMs will hallucinate during the critique phase. It's plausibly easier for an LLM to determine if a critique is reasonable than it is to produce a critique, so we can ignore bad feedback.

I think this approach is very interesting! There are two key insights that I expect to see in a lot of agentic software development with large language models:

 - The use of external verifiers and code quality tools wherever possible
 - The use of an adversarial critique loop

Further reading & useful links:
- The [Methodology](https://github.com/dollspace-gay/Tesseract-Vault/blob/main/WHITE_PAPER.md#101-methodology-overview) of Doll's `Tesseract-Vault`
- Doll's [Chainlink](https://github.com/dollspace-gay/chainlink/tree/main) – "A simple, lean issue tracker CLI designed for AI-assisted development. Track tasks across sessions with context preservation."
- Doll's [CodeScanner](https://github.com/dollspace-gay/codescanner) – "A multi-tool security vulnerability scanner that combines 17 industry-standard static analysis tools with AI-powered code scanning using Google Gemini."
- ["Propose, Solve, Verify: Self-Play Through Formal Verification"](https://arxiv.org/abs/2512.18160) (arXiv)
- ["The Adversarial Prover: A Skeptic’s Approach to LLM-Assisted Mathematics"](https://tjoresearchnotes.wordpress.com/2026/01/02/the-adversarial-prover-a-skeptics-approach-to-llm-assisted-mathematics/) (blog)
