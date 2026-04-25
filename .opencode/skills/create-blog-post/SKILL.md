---
name: create-blog-post
description: A skill to create new blog post drafts.
license: MIT
---

## What I do

- Create new blog post drafts in the _posts directory

##

Create new blog posts in the _posts directory.

To create a new blog post, create an appropriate filename: "{date}_{post_slug}.md"
 - The date should be today's date unless the user specifies a different date.
 - The post_slug should be a reasonable value.

Create the new file with standard front matter:
```
---
layout: post
title:  "{post_title}"
tags: [tag1, tag2, short]
excerpt: "{post_description}"
---
```

Ask the user for the post_title or choose something reasonable based on their request for them to edit later.

Tags are to your discretion. The most common tags on the blog are:
 - short (indicates a short post)
 - research (post relates to research)
 - code (post relates to code or coding)

Use Jekyll-flavored Markdown within the post body.

Subheadings should generally start at the second emphasis level (`##`).
