---
layout: post
title:  My debugging process
date:   2024-01-30
tags: code short
excerpt: My process for debugging software.
---

What should I do when I find a software bug? For many junior software developers, it's not obvious what steps we might take to find and fix bugs.
This is my bug-finding process, at a high level.

Let's assume we found the bug because of a failing unit test (a somewhat idealized case):

1. Look at the failing test. What is it trying to do? Is there an obvious reason the test is failing? What is the error message?
2. Did what I am trying to do _ever_ work? As an initial step, I would verify the test is still broken on the prior commit on this branch.
3. If there isn't an obvious reason or I don't know enough about this aspect of the system, I might be interested in understanding _when_ the test stopped working. Did the test work at any prior commit?
   1. The simple way to do this is to look at the commit history (in GitHub or in VSCode) and identify a few recent commits (merge commits are generally good candidates), grabbing their hashes. Then, you can checkout those commits (`git checkout {revision hash}`) and run the unit tests again.
   2. If you can't find a good commit (where the unit tests pass), then something changed in your local configuration (not versioned in the git repository) and we'll need to figure out what that it was.
   3. If you can find a previous commit where the unit tests pass, you can find the exact commit that broke this test by using [git bisect](https://git-scm.com/docs/git-bisect). That should help you understand what is breaking.
 4. To understand exactly why the test is failing, you should trace through that specific test using the [VSCode debugger](https://code.visualstudio.com/docs/editor/debugging).

If you fully hit a wall, that's a good time to ask another colleague for help.

Edit (May 2024): Stas Bekman has been writing the ["The Art of Debugging"](https://github.com/stas00/the-art-of-debugging) with a variety of guidance on debugging software systems.
