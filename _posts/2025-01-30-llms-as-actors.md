---
layout: post
title:  "Large language models as actors: Colin Fraser on alignment research"
tags: research alignment short xrisk safety llm
excerpt: "Colin Fraser wrote three Bluesky threads about problems in LLM alignment research."
---

In December 2024, Anthropic published ["Alignment faking in large language models"](https://www.anthropic.com/research/alignment-faking).

In response, data scientist Colin Fraser wrote [a Bluesky thread](https://bsky.app/profile/colin-fraser.net/post/3ldoyuozxwk2x) about why "alignment research" is "a big mess":

>Claude is not a real guy. Claude is a character in the stories that an LLM has been programmed to write. Just to give it a distinct name, let's call the LLM "the Shoggoth".
>
>When you have a conversation with Claude, what's really happening is you're coauthoring a fictional conversation transcript with the Shoggoth wherein you are writing the lines of one of the characters (the User), and the Shoggoth is writing the lines of Claude.
>
>Claude, like any other fictional character, has certain traits. He has principles and motivations. He has preferences. He's helpful, honest, and harmless. We understand these human traits and it's easy and tempting to think of them as the driving force behind what Claude says.
>
>But Claude is fake. The Shoggoth is real. And the Shoggoth's motivations, if you can even call them motivations, are strange and opaque and almost impossible to understand. All the Shoggoth wants to do is generate text by rolling weighted dice.
>
>The dice are weighted such that the text that they generate strikes some approximate balance between two somewhat competing objectives:
>
>1. It is statistically likely to occur according to the empirical distribution of text in the pretraining data
>2. It is statistically likely to please The Raters
>
>The Raters are people that Anthropic pays to review the transcripts and decide whether the Claude that is depicted is behaving the way that the Claude character should. If Claude's acting right, the text gets a thumbs up, and if Claude's acting wrong, the text gets a thumbs down.
>
>(These goals are competing because the empirical distribution of text may not be particularly pleasing to The Raters. Lots of the text in the pretraining data is horrifying and evil, for example. Figuring out a way to strike this balance what allowed ChatGPT to become a thing.)
>
>Periodically, Anthropic uses the thumbs ups and thumbs downs to update the dice weights to try to increase the likelihood of a thumbs up from The Raters. This doesn't hurt. The Shoggoth doesn't notice. The dice are just dice. Claude might behave a bit differently but Claude's fictional so it's fine.
>
>(One of the most unhinged tropes I overhear from the online AI enthusiast community is that this process is analogous to some kind shock therapy or torture or so on. This is completely ridiculous. The Shoggoth just gets a new pair of dice and starts writing Claude a little differently.)
>
>So here's where the mess is: alignment research seems to be highly fixated on Claude's goals and motivations, as though Claude was the entity that you are interacting with when you visit claude.ai. But Claude does not exist in the real world. The entity that you are interacting with is The Shoggoth.
>
>It's the Shoggoth's goals that we should be thinking about, determining whether they are aligned with ours and so on. And again, the Shoggoth's goals are strange. All it wants to do is generate text that it expects will please The Raters (though to be clear the Shoggoth isn't bothered if it fails)
>
>This mental model yields strong predictions about the behaviour of LLM bots. If Claude was real, you'd expect him to have a stable personality. But if Claude is a figment of the Shoggoth's fever dream, then [maybe you can coax the Shoggoth into writing Claude differently](https://bsky.app/profile/wwalls.bsky.social/post/3lcdepvwov22g).
>
>Claude's lines in the dialog are not driven by Claude's goals, but by the Shoggoth's half-assed attempt to please The Raters. The Raters are pleased when Claude appears to be a competent actor in the dialog. Claude's behavior [here](https://bsky.app/profile/colin-fraser.net/post/3ldoyup2ijz2x) is strange if you think Claude is trying to beat me at tic-tac-toe.
>
>But Claude's not trying to beat me at tic-tac-toe. Claude's not trying to do anything. Claude's fictional. The Shoggoth is trying to write a story wherein Claude is depicted as a competent actor. And it's basically succeeding at this. In the story, Claude's killing it. He's considered every angle.
>
>I think the key insight here is: the Shoggoth can depict the Claude character pursuing a goal *without actually pursuing that goal*, and this is entirely "aligned", to use the term of art, with the Shoggoth's immediate goal of spewing text that it expects will please The Raters.
>
>Where this gets really confusing and mind bending is that the tic-tac-toe game exists both in the Shoggoth's story and in the real world. I really am playing tic-tac-toe, but against a fictional guy. I'm playing against no one. Claude is fake, and the Shoggoth doesn't know we're playing.
>
>A very strange and interesting kind of thing happens here. But I don't think that it resembles anything that is described by most "alignment" research.

Fraser continues the thread in a [part 2](https://bsky.app/profile/colin-fraser.net/post/3ldpbpnoe6m2x) (on the specific Anthropic alignment study that motivated the thread) and a [part 3](https://bsky.app/profile/colin-fraser.net/post/3ldrhbvjnkc2o) (on goal seeking). Thread also [reblogged by Simon Willison](https://simonwillison.net/2025/Jan/4/colin-fraser/).

Further reading:
 - ["Role-Play with Large Language Models"](https://arxiv.org/abs/2305.16367) by Murray Shanahan, Kyle McDonell, Laria Reynolds
