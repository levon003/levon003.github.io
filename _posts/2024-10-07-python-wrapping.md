---
layout: post
title:  "Wrapping Python modules with Wrapt"
tags: python code short
excerpt: "The Python package Langfuse uses Wrapt to intercept calls to module functions."
---

The Python SDK for [Langfuse](https://langfuse.com/) provides a ["drop-in replacement" for the `openai` module](https://langfuse.com/docs/integrations/openai/python/get-started). To use it, you just update your import statements:

```diff
- import openai
+ from langfuse.openai import openai
```

Then, you use the `openai` module like normal and it monitors and logs your function calls to a server for later analysis.

This approach uses an `import-from` statement, so there must be a module with the name `openai` assigned in the module `langfuse.openai`.

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
Graham points out that monkey patching is not uncommonly used "to add instrumentation to existing Python code in order to add performance monitoring capabilities".
Langfuse isn't focused on performance, but it is trying to add monitoring capabilities to existing Python code.

## How it works

I implemented a slimmed down version of Langfuse's wrapping code. (See the whole `re_wrapper.py` file [on GitHub](https://github.com/levon003/levon003.github.io/blob/main/src/langfuse_wrapper/re_wrapper.py).) Instead of adding complex monitoring to a third-party module, I'll set my sights a little lower: adding monitoring to the built-in regex module `re`.

To use it, just import `re` from my custom module:

```diff
- import re
+ from re_wrapper import re
```

The core is the same as for Langfuse:

```python
import re
modifier = ReWrapped()
modifier.register_tracing()
```

`register_tracing` uses `wrapt.wrap_function_wrapper()` to wrap a function around specific functions in the `re` module. In this case, I only override `re.search`. (The full demo code follows the structure of the Langfuse code and accepts a list of functions to wrap.)

```python
wrap_function_wrapper(
    re,
    "search",
    _wrap("search", get_singleton_monitor),
)
```

`get_singleton_monitor` is a method that retrieves a singleton class instance that will do whatever monitoring activities we need to do. The Langfuse implementation called the function that retrieves this singleton `initialize`. I think that's a bit confusing since all the function currently does is retrieve this singleton, but conceptually this function _initializes_ monitoring within the wrapped function invocation by retrieving the monitor object. For this demo, I just had the monitor object keep track of function calls in a list:

```python
class ReMonitor:
    def __init__(self):
        self.memory = []
```

It's the `_wrap` function that contains the complexity. `wrap_function_wrapper` will ensure that when `re.search` is called, `_wrap` will be executed instead. Let's look at the complete implementation of `_wrap`:

```python
@_re_wrapper
def _wrap(function_name, get_singleton_monitor, wrapped, args, kwargs):
    monitor: ReMonitor = get_singleton_monitor()
    new_memory = {"function": function_name, "args": args, "kwargs": kwargs}
    try:
        result = wrapped(*args, **kwargs)
        new_memory["result"] = result
        return result
    except Exception as ex:
        new_memory["error"] = str(ex)
        raise ex
    finally:
        monitor.memory.append(new_memory)
```

There's a lot going on here, but we can start by looking at the arguments to `_wrap`:
 - `function_name` -  This is just the name of the function that is being wrapped, which allows our monitor to keep track of which function we wrapped with `wrap_function_wrapper` is being called.
 - `get_singleton_monitor` - This is the function we passed to `wrap_function_wrapper`; it will enable `_wrap` to actually record monitoring results by retrieving the singleton `ReMonitor` instance.
 - `wrapped`, `args`, `kwargs` - Where did these three positional arguments come from? We didn't include them in the above call to `_wrap`. We can guess that these are being populated by the `@_re_wrapper` decorator, which we'll look at next. By looking at their usage in the function, we can further guess that `wrapped` is the wrapped function that we need to execute with the positional (`args`) and keyword (`kwargs`) arguments passed to the wrapped function.

If we ignore the exception handling code, all `_wrap`'s implementation is really doing is:

```python
# get the monitor object
monitor = get_singleton_monitor()
# invoke the function, retrieving a result
result = wrapped(*args, **kwargs)
# have the monitor do something with the arguments and/or result
monitor.do_something(args, kwargs, result)
```

In the implementation above, I'm just saving all of that stuff into a dictionary and adding it to the monitor object's `memory` list.

The last detail to understand is how the `@_re_wrapper` decorator sends the invoked function and its arguments to `_wrap`.

```python
def _re_wrapper(func):
    def _with_re(function_name, get_singleton_monitor):
        def wrapper(wrapped, instance, args, kwargs):
            return func(function_name, get_singleton_monitor, wrapped, args, kwargs)
        return wrapper
    return _with_re
```

If you read ["How you implemented your Python decorator is wrong"](https://github.com/GrahamDumpleton/wrapt/blob/develop/blog/01-how-you-implemented-your-python-decorator-is-wrong.md), you might recognize this coding idiom. 
The [`wrapt` documentation](https://wrapt.readthedocs.io/en/master/quick-start.html) tell us that a wrapper function needs to take four positional arguments:

> - `wrapped` - The wrapped function which in turns needs to be called by your wrapper function.
> - `instance` - The object to which the wrapped function was bound when it was called.
> - `args` - The list of positional arguments supplied when the decorated function was called.
> - `kwargs` - The dictionary of keyword arguments supplied when the decorated function was called.

So `_re_wrapper` is a decorator that builds a wrapper function. The wrapper function itself is wrapped by a wrapper function that injects the inner-most function (`wrapped`) and the original arguments (`args`, `kwargs`). Frankly, I would consider this to be confusing code.

But the punchline is simple enough: by calling `_wrap` with the function name and the function that will retrieve the singleton monitor, it builds a wrapper function suitable for `wrapt.wrap_function_wrapper`.

It's easy to verify the behavior of our wrapper implementation (see [demo code](https://github.com/levon003/levon003.github.io/blob/main/src/langfuse_wrapper/wrapper_demo.py)):

```python
from re_wrapper import re, modifier
def main():
    match = re.search("a", "abcdef")
    # we can retrieve the monitor singleton from the ReWrapped object
    memory = modifier.get_singleton_monitor().memory
    assert memory[0]["result"] == match
    print(memory)
```

This demo will print `[{'function': 'search', 'args': ('a', 'abcdef'), 'kwargs': {}, 'result': <re.Match object; span=(0, 1), match='a'>}]`.

In general, I would think hard before I chose to use this type of module monkey-patching. 
For a monitoring library like Langfuse, it makes a lot of sense.
But if I just wanted to monitor my own usage of a particular module's functions, I would just explicitly wrap those calls within a monitor object created specifically for my monitoring use case. Creating a monitor object or monitoring function makes the monitoring process visible in my code and gives me the flexibility to choose which invocations I want to monitor. But if I was trying to monitor a large codebase where making major changes was impossible or costly but I _could_ tweak the imports, I might consider using the `wrapt` monkey-patching approach to add monitoring without any other code changes.

_I don't write that much about Python, but I've previously written on [chaining with '\|' in LangChain]({% post_url 2024-05-13-langchain-pipes %})._
