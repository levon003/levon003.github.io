---
layout: post
title:  "Jekyll on GitHub Pages"
date:   2023-10-13 00:00:00 -0700
categories: code
---
I had some difficulty setting up Jekyll for this GitHub site, where a static index page exists alongside a Jekyll blog.

My issue was that I created the Jekyll site in a subdirectory (`/blog`) like so:

```
jekyll new blog
```

I should have created the site in the root directory.

```
jekyll new .
```

This was hard to debug, because the posts were still accessible at the expected paths and the Jekyll build succeeded.
The biggest indicator of the issue was that the blog was formatted with the Primer theme (the GitHub default, as of October 2023) while the `_config.yml` file specified the Minima theme (the Jekyll default).

This code for this site is released under the MIT license; if it's useful, feel free to [build from it](https://github.com/levon003/levon003.github.io).
