---
layout: post
title: "Paper/dataset: A Random Sample of YouTube"
date:   2024-01-01
tags: research short
excerpt: A random sample of YouTube.
---

Ethan Zuckerman [writes](https://ethanzuckerman.com/2023/12/22/how-big-is-youtube/):

>How big is YouTube? It's a hard question: it took us almost two years to solve it. But now we know.

This neat paper takes a random sample of YouTube by exploiting the randomization of the 11-character video ID.

>McGrady, R., Zheng, K., Curran, R., Baumgartner, J., & Zuckerman, E. (2023). Dialing for Videos: A Random Sample of YouTube. ''Journal of Quantitative Description: Digital Media'', 3. <https://doi.org/10.51685/jqd.2023.022>


[Paper link.](https://journalqd.org/article/view/4066)

[Ethan Zuckerman's blog post.](https://ethanzuckerman.com/2023/12/22/how-big-is-youtube/)

[Ryan McGrady's blog post.](https://publicinfrastructure.org/2023/12/21/notes-from-random-youtube-coding/)

With 18.4 quintillion possible 11-character video IDs, it's not feasible to just try random video IDs in order to generate a random sample. The paper estimates a total of 13 billion public YouTube videos, so there's only a 0.00000007% chance that a randomly-chosen video ID actually exists. They instead use a quirk of the YouTube search API to generate a sample more quickly.

Their scraper ran from October-December 2022, stopping when they hit 10,000 videos in their sample. The dataset they analyze is then enriched with metadata about the videos.

### Ethics of dataset release

Ethan describes the ethical dilemma they are facing when considering if this dataset should be publically released:

>Most of the videos we’re discovering were only seen by a few dozen people. If we publish those URLs, we run the risk of exposing to public scrutiny videos that are “public” but whose authors could reasonably expect obscurity. Thus our paper does not include the list of videos discovered.

To borrow Amy Bruckman's terminology, these YouTube creators are ["amateur artists"](https://link.springer.com/article/10.1023/A:1021316409277). Generally speaking, I think the harms these kinds of non-disclosure choices are trying to prevent are overblown... and often out-weighed by the harms in deviating from community norms around publishing datasets for replication and to support future work. I hope Ethan and other researchers working with this dataset publish more about their ethical thinking around releasing this and similar datasets.

