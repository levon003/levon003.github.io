---
layout: post
title:  "My auto-updating Bluesky reading list"
tags: [bluesky, data, llm, short]
excerpt: "A vibe-coded pipeline to extract a reading list from my like history on Bluesky."
---

I had Claude Opus 4.8 vibe-code a nightly CI job to maintain a [list of every link I've liked on Bluesky](/bsky-links/).
My goal here was to make a reading list I can consult and search even if people delete later their posts, and I also have the benefit of additional metadata for articles and papers courtesy of [Citoid](https://www.mediawiki.org/wiki/Citoid).

![Most-liked domains and Bluesky accounts](/images/bsky_reading_list_summary.png){:style="display:block; height: auto; max-width: 50%; margin-left: auto; margin-right: auto;"}
*My most-liked domains and Bluesky accounts, as of June 2026. Updated nightly on [the list](/bsky-links/).*

Claude's solution was a few Python scripts:

1. Scrape liked posts using [`getActorLikes`](https://atproto.blue/en/latest/atproto/atproto_client.models.app.bsky.feed.get_actor_likes.html). To capture "new paper" threads better, I capture any links in the whole thread, not just the specific post I liked. I also capture links in quote posts.
2. Use Wikimedia's [Citoid](https://www.mediawiki.org/wiki/Citoid) service to attempt to get better title and author metadata for each link. Citoid fails quite regularly, so we "fall back" to the title and description in Bluesky's preview card, or just display the actual URL if no preview card was created. That means we fail to get the title and author from links like [https://users.eecs.northwestern.edu/~jhullman/AI_metascience_position.pdf](https://users.eecs.northwestern.edu/~jhullman/AI_metascience_position.pdf), even though a PDF-parsing service like Zotero would be able to infer title, author, and date.
3. Check for dead links, attaching a [Wayback Machine](https://web.archive.org/) link if the link seems dead (404, 410, SSL error, connection refused, or DNS failure).

The output is a [YAML file](https://github.com/levon003/levon003.github.io/blob/main/_data/bsky_likes.yml) versioned in this blog's public GitHub repository, which a Jekyll template consumes as site data. GitHub Actions runs nightly to refresh the YAML file.

Claude was great at iteratively identifying issues and fixing them, and there are a number of special cases. The most prominent of these issues is something that's been annoying me on Wikipedia lately too: a lot of the academic publishers have started loading an "are you human" page before directing you on to the article page, which means Citoid can't resolve metadata correctly. The most prominent examples are papers hosted on the ACM Digital Library or in the Open Science Framework's PsyArXiv pre-print repository. Fortunately, the URLs for those two sites contain enough information to extract a DOI from the URL, which enables us to recover in most cases. But it requires a special case, so there's a good chance that Citoid will just stop working in the future for more and more publisher pages.

If you want to do something similar, it's very easy to set up: you'll just need to generate an [App Password](https://bsky.app/settings/app-passwords). Find the code [on GitHub](https://github.com/levon003/levon003.github.io/tree/main/src/bsky_link_history), but again, this was vibe-coded: I literally didn't read the code at all.

(I'll note that I still don't use LLMs for writing... although Claude did generate the URL slug for this post and produced a summary text that I used to write up the post myself. I'm not quite willing to give up my writing yet!)
