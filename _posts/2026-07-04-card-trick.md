---
layout: post
title:  "Penn & Teller's Love Ritual: a self-working card trick"
tags: math simulation games magic algorithms
excerpt: "Animating a self-working card trick."
---

Penn and Teller performed a "self-working" card trick on [_Penn & Teller: Fool Us_](https://en.wikipedia.org/wiki/Penn_%26_Teller:_Fool_Us). You can watch the trick [on YouTube](https://youtu.be/K9vEYyBwgp4?t=2040).

The trick is themed around finding love and and the presentation has several good gags. But the basis of the trick is just executing a series of steps:

1. Shuffle 4 randomly-selected playing cards into a stack.
2. Tear the stack in half, placing one half on top of the other, producing a new stack of 8 half-cards.
3. Put the top card on the bottom of the stack.
4. Put the top 2 cards on the bottom of the stack.
5. Put the top 3 cards (together) somewhere in the middle.
6. Pull the top card aside — this is the **comparison card**.
7. Take 1, 2, or 3 cards from the top and put them somewhere in the middle.
8. Put the top card somewhere in the middle.
9. Throw away 1, 2, or 3 cards from the top.
10. Seven times: put the top card on the bottom.
11. Then, alternating until one card is left: top card to the bottom, then throw away the new top card.
12. The surviving card matches the comparison card.

There are choices in steps 2, 7, 8, and 9, but the trick works regardless. Why?

## Try it yourself

First, try the trick yourself. Step through the moves and make the choices to get a feel for the trick.

{% include card-trick/card-trick-play.html %}

You can check "highlight comparison card" and run the trick again to visualize how both halves move through the stack.

## Why does the trick work?

The moves feel like they introduce randomness, but the trick works for three reasons:

1. The initial steps put the partner of the comparison card on the bottom
2. None of the choices can disturb the bottom card
3. The ending deal always picks the bottom card

In other words, the trick is just obfuscation around a simple procedure: put the partner of the comparison card on the bottom, then run a deal that always returns the bottom card.

### The initial steps put the partner of the comparison card on the bottom

- In the initial stack of half cards, the two halves of each full card – including the comparison card – are exactly 4 positions apart. (The "which half-stack goes on top" choice doesn't matter at all; it's a false choice.)
- Steps 3 and 4 (moving 1, then 2 cards from top to bottom) don't change this structure for the comparison card, and now the two halves of the comparison card are forth and eighth in the stack.
- Step 5 removes the top 3 cards as a block and buries them somewhere in the middle. Before you decide where to bury those 3 cards, notice that the top and bottom card of the 5 remaining cards are **two halves of the same card**.
- Step 6 takes the top card as the comparison card — so its partner is sitting at the bottom of the stack before any of the subsequent choices are made.


### None of the choices can disturb the bottom card

- Steps 7 and 8 insert cards "somewhere in the middle" — inserting in the middle never changes what's on the bottom. Note that "somewhere in the middle" has to mean *strictly interior*: not on the very bottom of the stack, which would disrupt the location of the comparison card's half.
- Step 9 discards from the top — discarding from the top can't affect the bottom.

### The ending deal always picks the bottom card

- After step 9, you have 4, 5, or 6 cards left (you discarded 1–3 from 7).
- Step 10 deals 7 cards to the bottom.
  - If you had 4 cards left, the comparison card is now in the first position.
  - If you had 5 cards left, the comparison card is now in the third position.
  - If you had 6 cards left, the comparison card is now in the fifth position.
- Step 11 asks us to "down-under deal" (one card dealt to the bottom, the next is discarded) until one survives.

The 7 in Step 10 is not arbitrary: it's the only choice that makes the bottom card survive for all three possible stack sizes at once. You can test this yourself below: pick any other number of times to cut the top card to the bottom and see which cards are selected at each possible deck size. The ♥ marks each stack's bottom card.

{% include card-trick/card-trick-deal.html %}

Only 7 cuts works to choose the bottom card regardless of whether 4, 5, or 6 cards remained after step 9. That does explain _how_ the ending works, but it doesn't explain _why_ the ending works. To understand that, we can notice that the ending of the trick is the _Josephus problem_.

### The Josephus problem

Imagine that the stack of remaining cards after step 9 was laid out in a circle. Before worrying about the deal, let's just think about the bottom cuts in step 10: each individual cut keeps the same order but changes which card is the "top".

{% include card-trick/card-trick-cut.html %}

The number of cuts only changes which card is the top card, which we keep track of in the ring using an orange ▶ pointer. 
In the 6-card stack, 6 cuts moves the pointer marking the top of the stack all the way around the ring and back to your starting point, leaving the stack completely unchanged.

In the actual trick, we do 7 cuts, which for the 6-card stack is equivalent to 6 cuts followed by 1 cut. We already know 6 cuts leaves the stack unchanged, so 7 cuts must be equivalent to just doing 1 cut.
We can figure out the actual number of cuts you need to do by dividing the number of cuts by the number of cards in the stack and looking only at the _remainder_.

If I tell you to cut the 6-card stack 36 times, you could recognize that (# of cuts / # of cards) = 36 / 6 = 0, so you don't need to do any cuts! 36 cuts is equivalent to doing 0 cuts, 6 cuts, 12 cuts, etc. (The mathematical way to describe this equivalence is to use [modular arithmetic](https://en.wikipedia.org/wiki/Modular_arithmetic), writing 36 ≡ 0 (mod 6).)

Ultimately, that means the number of cuts is just a way of choosing a new top card – the selected card in the ring.

Why is it useful to think about the problem this way? Because the repeated down-under deal in step 11 is a [Josephus problem](https://en.wikipedia.org/wiki/Josephus_problem).
Given a ring of a particular size and starting from a particular point in that ring, the Josephus problem involves discarding and sparing every other card until we have one card remaining.

Here's the Josephus procedure applied to a 6-card stack.

{% include card-trick/card-trick-josephus.html %}

Notice that the 5th card is always the remaining card. In fact, the Josephus problem is solved, and it has a nice formula (see the [Wikipedia page](https://en.wikipedia.org/wiki/Josephus_problem)). We can look up which card survives relative to the starting card:

| Ring size | Surviving card |
|:---------:|:--------------:|
| 4         | 1st            |
| 5         | 3rd            |
| 6         | 5th            |

Because the Josephus procedure always spares a specific card position in the stack, we just need to first do a number of cuts such that the comparison card ends up as the 1st card in the 4-card stack, the 3rd card in the 5-card stack, or the 5th card in the 6-card stack.
As we've already seen, this is exactly what 7 total cuts accomplishes.

- In the 6-card stack, 7 cuts is equivalent to 1 cut, moving the comparison card from the bottom to the 5th position.
- In the 5-card stack, 7 cuts is equivalent to 2 cuts, moving the comparison card from the bottom to the 3rd position.
- In the 4-card stack, 7 cuts is equivalent to 3 cuts, moving the comparison card from the bottom to the 1st position.

We can now run the ending from differing numbers of cuts, confirming that 7 cuts is the only option to move the comparison card to the appropriate position in the stack at all three possible stack sizes.

{% include card-trick/card-trick-ring.html %}

(If you're familiar with modular arithmetic, you'll note that 7 ≡ 3 (mod 4), 2 (mod 5), and 1 (mod 6) – the right top card for all three stack sizes simultaneously.)

I thought this was a neat trick. I had Claude Opus create the visualizations for me so I could understand the trick better (although I wrote the text in the animations and in the rest of the post). I guess that's another use of large language models... removing a little magic from the world!

## Further reading

 - [The Josephus Problem](https://www.youtube.com/watch?v=uCsD3ZGzMgE) by Numberphile (YouTube)
