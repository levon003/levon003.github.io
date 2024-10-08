---
layout: post
title:  "Wrapping Python modules"
tags: python code short
excerpt: "The Python package Langfuse uses Wrapt to intercept calls to module functions."
---

The Python package Langfuse provides a [drop-in replacement for the `openai` module](https://langfuse.com/docs/integrations/openai/python/get-started). To use it, you can just update your import statements:

```diff
- import openai
+ from langfuse.openai import openai
```

Then, you use the `openai` module like normal and it monitors and logs your calls to a server for later analysis.

This approach uses a `import-from` statement, so there must be a module with the name `openai` assigned in the module `langfuse.openai`.

If we look at [the code](https://github.com/langfuse/langfuse-python/blob/37d0632b65a48803adfdba4c852a2b0b5dfd3d88/langfuse/openai.py#L39), we indeed see that the name is defined (via import):

```python
import openai
# ... a bunch of function and class definitions ...
modifier = OpenAILangfuse()
modifier.register_tracing()
```

So, `OpenAILangfuse.register_tracing()` must be overriding or wrapping the functionality of the imported `openai` module somehow. How does this work?

At a high level, they use Graham Dumpleton's [`wrapt`](https://wrapt.readthedocs.io/en/master/) package. Graham's blog post ["How you implemented your Python decorator is wrong"](https://github.com/GrahamDumpleton/wrapt/blob/develop/blog/01-how-you-implemented-your-python-decorator-is-wrong.md) articulates some of the motivation for `wrapt`.
A later blog (["Safely applying monkey patches in Python"](https://github.com/GrahamDumpleton/wrapt/blob/develop/blog/11-safely-applying-monkey-patches-in-python.md)) is more relevant to our specific use-case here: monkey-patching a module's class methods.
Graham points out that monkey patching is non uncommonly used "to add instrumentation to existing Python code in order to add performance monitoring capabilities".
Langfuse isn't focused on performance, but it is trying to add monitoring capabilities to existing Python code.


_I don't write that much about Python, but I've previously written on [chaining with '|' in LangChain]({% post_url 2024-05-13-langchain-pipes %})._
