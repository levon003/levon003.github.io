---
layout: post
title:  "AI Safety: is there an existential risk?"
tags: llm xrisk safety short
excerpt: "A few notes on the existential risk posed by artifical intelligence."
---

A few weeks ago, I had a conversation with [Jeffrey Ladish](https://jeffreyladish.com/) and [Eli Tyre](https://elityre.com/), two AI safety researchers and activists who put out a [call](https://twitter.com/JeffLadish/status/1848885766849761353) for open conversations with skepticism about "AI risk" arguments:

>I'm looking for people to have 30-60 minute conversations with about AI. I'm especially interested in talking with people who have heard some of the AI risk arguments, and have used ChatGPT, but don't see why or how AI could actually take over or seize control from humanity
>
>My plan is to briefly walk through the reasons why I am concerned about near-term existential AI risk, with space for you to ask questions or state objections, and then mostly have an informal conversation about whatever seems most relevant and interesting to the two of us

This discussion was interesting, because I've had pretty minimal exposure to AI "existential risk" arguments.
In general, I remain skeptical of existential risk arguments, but I'm interested in continuing to learn more.

A few of my personal take-aways from the conversation and from reflecting on the conversation afterward:
 - The format was great. Compared to other interview studies I've been involved in, Jeffrey and Eli were more interested in posing specific arguments and hearing me respond to them. They seemed to be most interested in figuring out which of the many premises needed to support existential risk claims seemed plausible vs implausible to people like me who haven't thought deeply about them.
   - At the end of the call, I asked them for recommendations of learning resources (which I link below). My hope is that the data they collect from these conversations will inform more useful learning resources for people working adjacent to ML that are interested in learning more about AI safety.
 - Existential risk arguments rely fundamentaly on logical or philosophical arguments. There are relatively few empirical questions related to existential AI risk that can be answered in principle, and those that can be answered might only be easy to answer in hindsight.
   - In general, I've done almost no thinking about the relevant philosophical issues. For that reason, social consensus among the people I perceive to be experts (e.g. philosophers of AI, computer science researchers, etc.) is important to me.
   - For example, is it possible to build a silicon mind? I have no idea. As someone with very little exposure to ideas like this, I find it essentially impossible to imagine "consciousness, but not human-like". But existential risk arguments seem to rely on non-human-like consciousness.
     - I learned after the call that Bostrom and Yudkowsky have referred to these as ["minds with exotic properties"](https://nickbostrom.com/ethics/artificial-intelligence.pdf).
   - Similarly, I find "super intelligence" hard to reason about as a concept, and I was generally skeptical of claims about systems that meaningfully outperform existing groups of humans (e.g. teams, corporations).
   - Generally, I agreed with Jeffrey and Eli about their empirical description of the current world.
 - Existential risk from AI is fundamentally about making predictions about the future, and I believe that humans are very bad forecasters.
   - cf. Rodney Brooks' writing in _MIT Technology Review_: ["The Seven Deadly Sins of AI Predictions"](https://www.technologyreview.com/2017/10/06/241837/the-seven-deadly-sins-of-ai-predictions/) 
 - A lot of our conversation focused on group coordination.
   - Humans have gotten a lot better at group coordination, but we notably don't seem to be improving our coordination exponentially.
   - Could AI systems improve themselves exponentially through better coordination? I'd expect them to experience significant coordination friction (in the same sorts of ways that humans do), but maybe AI systems have qualities that will enable them to avoid coordination problems? For example:
     - Access to your own and other's memories in a direct way
     - Faster communication
     - Shared goals, or at least communicable goals
 - It seems like getting a good signal for self-improvement is hard.
   - A system with a reliable self-improvement signal and sufficient resources could probably improve itself.
 - It seems like there's something distinct about the signal you get from "real life", as opposed to doing a lot of computing on data you already have, but it's hard to say what that is.
    - A Zoom call is a real reward signal! An AI system could certainly improve itself by talking with humans via Zoom, in the same way that humans improve ourselves by talking with humans via Zoom. But, it's slow; intuitively, you're constrained by communication speed.

## Resources

Resources recommended by Jeffrey and Eli at the conclusion of the call:
 - Robert Miles' [YouTube channel](https://www.youtube.com/@RobertMilesAI/featured)
 - <https://aisafety.info/>
 - <https://www.aisafety.com/>

Other resources I've stumbled across:
 - Introductions/summaries
   - "The case for taking AI seriously as a threat to humanity" by Kelsey Piper: <https://www.vox.com/future-perfect/2018/12/21/18126576/ai-artificial-intelligence-machine-learning-safety-alignment>
   - "Preventing an AI-related catastrophe" by Benjamin Hilton: <https://80000hours.org/problem-profiles/artificial-intelligence/>
   - "Intro to brain-like-AGI safety" by Steve Brynes: <https://www.alignmentforum.org/s/HzcM2dkCq7fwXBej8>
   - "AGI safety from first principles" by Richard Ngo: <https://www.alignmentforum.org/s/mzgtmmTKKn5MuCzFJ>
   - "The Compendium" by Connor Leahy, Gabriel Alfour, Chris Scammell, Andrea Miotti, Adam Shimi: <https://www.thecompendium.ai/>
     - "The Compendium aims to present a coherent worldview explaining the race to AGI and extinction risks and what to do about them, in a way that is accessible to non-technical readers who have no prior knowledge about AI." From a quick look, seems too vague and one-sided to be useful beyond a high-level exposure to one perspective. 
 - "The implausibility of intelligence explosion" by François Chollet: <https://medium.com/@francois.chollet/the-impossibility-of-intelligence-explosion-5be4a9eda6ec>
   - This blog post from 2017 was very influential on my early thinking about AI safety risks, particularly the importance of coordination and communication problems.
 - "Beyond Preferences in AI Alignment" by Tan Zhi-Xuan, Micah Carroll, Matija Franklin, Hal Ashton: <https://arxiv.org/abs/2408.16984>
   - This useful overview paper speaks to a diversity of philosophical perspectives on the value alignment problem.
 - "Debunking Robot Rights Metaphysically, Ethically, and Legally" by Abeba Birhane, Jelle van Dijk, Frank Pasquale: <https://arxiv.org/abs/2404.10072>
   - A useful overview of arguments for not accepting "robot rights" arguments, although the V1 draft appears pretty rough.
 - "Reclaiming AI as a Theoretical Tool for Cognitive Science" by Iris van Rooij, Olivia Guest, Federico Adolfi, Ronald de Haan, Antonina Kolokolova, Patricia Rich: <https://link.springer.com/article/10.1007/s42113-024-00217-5>
   - I've previously written about van Rooij's term [_makeism_]({% post_url 2023-10-17-wishful-mnemonics %}).
 - Consciousness
   - "The Hard Problem of Consciousness": <https://iep.utm.edu/hard-problem-of-conciousness/>
   - "Consciousness": <https://plato.stanford.edu/entries/consciousness/>
   - "Linguistic Bodies: The Continuity between Life and Language" by Ezequiel A. Di Paolo, Elena Clare Cuffari, Hanne De Jaegher: <https://direct.mit.edu/books/monograph/4107/Linguistic-BodiesThe-Continuity-between-Life-and>
   - "The Edge of Sentience: Risk and Precaution in Humans, Other Animals, and AI" by Jonathan Birch: <https://academic.oup.com/book/57949>
 - Coordination
   - "Exploring the Impact of Coordination in Human–Agent Teams": <https://journals.sagepub.com/doi/full/10.1177/15553434211010573>
 - "Should AI Progress Speed Up, Slow Down, or Stay the Same?" by Miles Brundage: <https://milesbrundage.substack.com/p/should-ai-progress-speed-up-slow>
   - Not specifically related to existential risks, but a good argument for the utility of building policy and governance structures capable of slowing the rate of AI progress (even if we choose not to use them).
 - "Promotionalism, orthogonality, and instrumental convergence" by Nathaniel Sharadin: <https://link.springer.com/article/10.1007/s11098-024-02212-9>
   - A philosophical critique of [instrumental convergence](https://en.wikipedia.org/wiki/Instrumental_convergence).
   - See Bostrom's ["The Superintelligent Will: Motivation and Instrumental Rationality in Advanced Artificial Agents"](https://nickbostrom.com/superintelligentwill.pdf) for more on instrumental convergence.
 - ["The Maverick Nanny with a Dopamine Drip: Debunking Fallacies in the Theory of AI Motivation"](https://aaai.org/papers/07752-7752-the-maverick-nanny-with-a-dopamine-drip-debunking-fallacies-in-the-theory-of-ai-motivation/) by Richard Loosemore.
   - 2014 AAAI paper attacking the plausibility of some AI doom scenarios as a product of assumptions about the strucutre of AGI.

### Notes on Richard Ngo's [_AGI safety from first principles_](https://www.alignmentforum.org/s/mzgtmmTKKn5MuCzFJ)

I'm finding Ngo's [_AGI safety from first principles_](https://www.alignmentforum.org/s/mzgtmmTKKn5MuCzFJ) to be a useful and even-handed introduction.

In the chapter on Superintelligence, Ngo makes several claims that I found surprising or non-obvious.

>I think it’s difficult to deny that in principle it’s possible to build individual generalisation-based AGIs which are superintelligent, since human brains are constrained by [many factors](https://intelligenceexplosion.com/2011/plenty-of-room-above-us/) which will be much less limiting for AIs.

I don't think it's at all obvious that this is true. There may be many factors that constrain humans that won't constrain hypothetical AGIs, but if those constraints aren't the primary bottleneck to greater-than-human intelligence then AGIs may not be qualitatively different in their capabilities than humans.
For example, I suspect I would be _more_ capable if I could think 100x "faster" than I currently do, but it's not at all clear to me how _much_ more capable I would be.

>There is little reason to believe that [humans] have reached the peak of [the ability to coordinate and benefit from cultural learning], or that AGIs couldn’t have a much larger advantage over a human than that human has over a chimp, in acquiring knowledge from other agents.

This seems like an empirical claim about group dynamics and hypothetical limits on coordination.
Because I don't know what the practical barriers are to improving _human_ coordination, it's not clear to me if silicon agents would or wouldn't be substantially more effective at this.

For both of these claims, I would like to better understand the relevant human dynamics before assuming that AGIs can easily overcome those dynamics.
