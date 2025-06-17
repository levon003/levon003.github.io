---
layout: post
title:  "Research idea: estimate the causal impact of sharing your true opinions on social media"
date:   2024-01-02
tags: research politics idea short
excerpt: A research/design opportunity for social media communication behaviors.
---
Should leftists (or any political group) self-censor their true political views in order to appear less off-putting to other social media users?
This basic question is a recurring favorite to argue about (and it has recently resurfaced on Twitter/X).

In ["There Will Be No Message Discipline"](https://sootyempiric.blogspot.com/2022/06/there-will-be-no-message-discipline.html) (June 2022), philosopher Liam Kofi Bright describes a few reasons why we might reject calls to self-censor on social media.

He makes several points, but he sums up a basic argument in this table of ranked preferences for four outcomes:

|                | Win | Lose |
|----------------|-----|------|
| Speak my mind  | 4 (Best)   | 2    |
| Self-censor    | 3   | 1 (Worst)   |

Most people would rather win than lose, and secondarily would rather speak their mind than self-censor (or follow "message discipline").
So, if my speaking my mind won't substantially decrease the probability of my side losing, then I'm better off speaking my mind.
Liam writes:

>If the left is on track to form a winning coalition the probability that it would not occur if a random schmuck tweets something insensitive is just vanishingly small. Social forces are not so easily derailed, and in a tolerably large democracy (and a non-democracy of more than 2 people) most of us simply make no difference.

He points out that this is basically just the [paradox of voting](https://en.wikipedia.org/wiki/Paradox_of_voting), but for social media behaviors. Liam observes that this situation can change in the presence of coordination:

>Something like a party with a mechanism for adopting a mass line — in particular something which assured me that my engaging in message discipline is either evidence others will also be, or will causally contribute to making it more likely they will. But absent organised solidarity we shall all keep furiously tweeting into an indifferent political void.

I think this is basically right, and I would suggest that **mechanisms for reasoning about how my behavior will effect others** is an interesting design and modeling problem for [human-computer interaction](https://www.interaction-design.org/literature/topics/human-computer-interaction) researchers.

I see many plausible research opportunities here:

 - Estimate the causal impacts of sharing your true opinions on social media. It can be hard to tell when you're a "random schmuck" or when you're in a position to genuinely influence relevant others, so visualizing this probability for given issues and behaviors could be useful information for driving decision-making. (These estimates could also be useful for determining the "visibility" of your posting. Most posters have poor intuitions of the visibility and reach of their posts: how likely is it that a given post will be used "against me" by my ideological opponents in a way that will make me unhappy?)
 - Visualize other plausible outcomes from political social media posting. People do a lot of self-monitoring about their own social media behaviors e.g. disclosing [sexual abuse](https://dl.acm.org/doi/10.1145/3234942) or [health issues](https://dl.acm.org/doi/abs/10.1145/1958824.1958876), and political sharing can be stressful. What will my followers think of this post? What will my *non*-followers think? A good "research through design" opportunity for learning more about sharing decision-making, imagined audiences, etc. as well.
 - Designs that enable people to conceptualize their social media behaviors as contributing to a commons. And then to coordinate with others about care for that commons (see e.g. [Elinor Ostrom's work](https://www.yesmagazine.org/issue/america-remix/2010/02/27/elinor-ostrom-wins-nobel-for-common-s-sense)).
 - Automated coordination mechanisms. Ex: a rephrasing interface where I publish two versions of my post (one true to my beliefs, one closer to mainstream opinions) into a delayed pool. Then, the mainstream tweet is published when another user submits their own post pair into the pool, thus ensuring that my own choice to moderate my posting influenced the content of another person's post as well.

All of these have at least some existing research on the modeling or design side, but it seems like there are good opportunities to bridge modeling and design in a single interface to see how the availability of new information changes people's social media posting behaviors.

## Further Reading

 - In June 2025, I stumbled about Will Schulz's dissertation _[Warped Words: How Online Speech Misrepresents Opinion](https://willschulz.com/wp-content/uploads/2024/06/Schulz-Dissertation.pdf)_. Chapter 3 is quite relevant to political self-censorship online; Schulz presented a version of that chapter as ["Political Catchphrases Reveal Polarizing Self-Censorship on Facebook and Twitter"](https://willschulz.com/wp-content/uploads/2024/10/Schulz_WWYS_Online.pdf) at ICA 2025.
