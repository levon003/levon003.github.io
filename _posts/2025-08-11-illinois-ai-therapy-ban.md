---
layout: post
title:  "An Illinois AI therapy ban – exempting peer support and religious counseling"
tags: llm therapy law "peer support" "social support"
excerpt: "Legislation around application-specific LLM use is here."
---

Illinois just passed [Public Act 104-0054](https://www.ilga.gov/Legislation/PublicActs/View/104-0054), the "Wellness and Oversight for Psychological Resources Act". See [_StateScoop_ summary](https://statescoop.com/illinois-bans-ai-mental-health-services/) and [Melanie Mitchell's Bluesky thread](https://bsky.app/profile/mmitchell.bsky.social/post/3lw5erptbrs25).

<small>Obligatory: this post discusses a public law, but I am not a lawyer and any interpretations may be horribly wrong.</small>

The crux of the bill is a restriction of therapy provision to licensed professionals:

>The purpose of this Act is to safeguard individuals seeking therapy or psychotherapy services by ensuring these services are delivered by qualified, licensed, or certified professionals.

Tangibly, the bill explicitly restricts four uses of "artificial intelligence":

>A licensed professional may not allow artificial intelligence to do any of the following:
> 1. make independent therapeutic decisions;
> 2. directly interact with clients in any form of therapeutic communication;
> 3. generate therapeutic recommendations or treatment plans without review and approval by the licensed professional; or
> 4. detect emotions or mental states.

What does the state of Illinois think "artificial intelligence" means? As defined in [Section 2-101 of the Illinois Human Rights Act](https://www.ilga.gov/Documents/legislation/ilcs/documents/077500050K2-101.htm):

>A machine-based system that, for explicit or implicit objectives, infers, from the input it receives, how to generate outputs such as predictions, content, recommendations, or decisions that can influence physical or virtual environments. "Artificial intelligence" includes generative artificial intelligence.
>
>"Generative artificial intelligence" means an automated computing system that, when prompted with human prompts, descriptions, or queries, can produce outputs that simulate human-produced content. [longer definition snipped]

This is a very broad definition that is focused on _purpose_, not a particular implementation. If the goal of a system is to simulate human-produced content or to _infer_ from an input, it's considered "artificial intelligence".
The bill is clearly motivated by large language models (LLMs), but _any_ technology meeting this definition can't be used for the four listed uses.

The prohibition on detecting "emotions or mental states" is a notable inclusion; many models exist for these purposes, although emotion detection is generally a hard/impossible problem and they have significant ethical risks.
However, inferring mental states may include some intent detection algorithms, such as those used in some 'context sensitive' moderation filters. This might make it illegal to use standard moderation tooling in online communities organized by mental-health professionals, which are not common but do crop up in research prototypes from time to time.

I suspect there are other unintended consequences associated with this specific ban, although none immediately jump to mind.
A likely _intended_ consequence is the prohibition of some automated analysis tools for patient notes or session recordings.
Any system that attempts to infer a patient's mental state – such as from a session transcript – is prohibited by this act.
That could rule out the use of some training or "assistant" tools.

## Permissible uses

What are therapists _allowed_ to do with "artificial intelligence"? With prior disclosure and the consent of the patient, therapists are permitted to use "artificial intelligence"

>in providing administrative support or supplementary support in therapy or psychotherapy services where the licensed professional maintains full responsibility for all interactions, outputs, and data use associated with the system.

I like the focus on _responsibility_ here, which avoids potential traps around treating machine systems as legal persons (see [Joanna Bryson](https://link.springer.com/article/10.1007/s10506-017-9214-9)).

The disclosure requirement does mean that Illinoisan therapists will likely need to start explicitly listing the technology they use for administrative support. The search feature in an email browser would seem to meet the "artificial intelligence" definition, for example; if the therapist does any electronic patient communication that isn't about scheduling appointments, they'll need to inform the patient "that artificial intelligence will be used" and "the specific purpose of the artificial intelligence tool or system that will be used". 

This mostly seems like an unnecessary administrative burden on therapists, but it's also a good general practice to report the systems that index and process patient data.
In practice, I assume existing therapy practices will not report any of the systems they use as long as they aren't intended for any of the four explicitly-forbidden uses.

## Exemptions

The prohibitions are interesting, but I'm _most_ interested in the three exemptions:

1. Religious counseling
2. Peer support
3. Self-help materials and educational resources that are available to the public and do not purport to offer therapy or psychotherapy services

A few things stand out to me about these exemptions:
 - Spiritual support chatbots remain legal. Implementation of LLM-backed spiritual support systems is [likely to be frought](https://arxiv.org/abs/2506.11366) (Bezabih et al. 2025), but this remains an avenue for independent technology development.
 - I have no idea what the line is between therapy and self-help. It seems likely that some "LLMs for therapy" products might be able to successfully reorient themselves as an interactive self-help or education tool.
 - The act defines _peer support_ as "services provided by individuals with lived experience of mental health conditions or recovery from substance use that are intended to offer encouragement, understanding, and guidance without clinical intervention". So non-professional advice in online health communities or on social media can still be created by LLMs.
 - I wonder if online health communities like 7 Cups (see [Fang and Zhu 2022](https://dl.acm.org/doi/abs/10.1145/3555202)) that rely on matching peer supporters with support seekers will be effected by this law. "Without clinical intervention" seems like the key, and I have no idea what that means. While 7 Cups volunteers do receive training, they don't seem like they're providing "clinical interventions", although they may be _replacing_ clinical interventions that support seekers would otherwise go to therapists for.
