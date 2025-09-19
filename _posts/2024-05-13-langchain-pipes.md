---
layout: post
title:  "Why can you use the pipe operator ('|') in LangChain?"
date:   2024-05-13
tags: code python llm langchain
excerpt: "LangChain lets you write chains using vertical pipes. How? By overriding __or__."
---

The popular Python library [LangChain](https://python.langchain.com/v0.1/docs/get_started/quickstart/) lets you define LLM chains using the vertical pipe operator:

```python
chain = prompt | llm
chain.invoke({"input": "What is human-computer interaction?"})
```

I'm [not the first](https://www.reddit.com/r/LangChain/comments/175edd4/how_does_the_pipe_symbol_work_in_python_from_this/) to be surprised by this syntax: why does this work?

You may know that the | is the [bitwise OR](https://stackoverflow.com/a/77141519/4146714) operator, although you may not know that the operator can be overridden by overriding the [`__or__` method](https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types) in a class definition.
That's why you can use the bitwise OR operation to take the union of two sets, for example: Python overrides the numeric bitwise OR operation for `set`s by overriding the `__or__` implementation.

Unsurprisingly, that's how LangChain achieves this functionality as well.

In a [GitHub gist](https://gist.github.com/levon003/42c33f505262d19306afb8eca24f6c25), I stripped down the LangChain Runnable code to understand how LangChain achieves this effect.

It starts with defining a [Runnable](https://github.com/langchain-ai/langchain/blob/f92006de3ce2ef6795c9a3f5bc798a8d2fa02bb7/libs/core/langchain_core/runnables/base.py) class that overrides `__or__` (and its inverse `__ror__`):

```python
class Runnable(Generic[Input, Output], ABC):
    def __or__(
        self,
        other: Union[
            Runnable[Any, Other],
            Callable[[Any], Other],
            Callable[[Iterator[Any]], Iterator[Other]],
            Mapping[str, Union[Runnable[Any, Other], Callable[[Any], Other], Any]],
        ],
    ) -> Runnable[Input, Other]:
        return RunnableSequence(self, coerce_to_runnable(other))

    def __ror__(
        self,
        other: Union[
            Runnable[Other, Any],
            Callable[[Other], Any],
            Callable[[Iterator[Other]], Iterator[Any]],
            Mapping[str, Union[Runnable[Other, Any], Callable[[Other], Any], Any]],
        ],
    ) -> Runnable[Other, Output]:
        return RunnableSequence(coerce_to_runnable(other), self)

    @abstractmethod
    def invoke(self, input: Input) -> Output:
```

Composing a Runnable implementation with another via the vertical pipe creates a RunnableSequence, which is straightforward to implement: it stores and executes a list of steps in sequence!

```python
class RunnableSequence(Runnable[Input, Output]):
    def __init__(
        self,
        *steps: Runnable,
    ) -> None:
        steps_flat: List[Runnable] = []
        for step in steps:
            if isinstance(step, RunnableSequence):
                steps_flat.extend(step.steps)
            else:
                steps_flat.append(step)
        self.steps = steps_flat

    def invoke(self, input: Input) -> Output:
        for step in self.steps:
            input = step.invoke(input)
```

We can then implement a Runnable and chain them together:

```python
class Adder(Runnable):
    def __init__(self, value: int):
        self.value = value

    def invoke(self, input: Input) -> Output:
        return input + self.value


a = Adder(5)
b = Adder(4)
c = a | b
assert c.invoke(1) == 10
```

But LangChain also allows you to chain together functions as though they were Runnable objects. How? That's what the call to `coerce_to_runnable` in the `Runnable.__or__` implementation is used for.

```python
def coerce_to_runnable(thing) -> Runnable[Input, Output]:
    if isinstance(thing, Runnable):
        return thing
    elif callable(thing):
        return RunnableLambda(thing)
    else:
        raise TypeError("Expected a Runnable or callable.")


class RunnableLambda(Runnable[Input, Output]):
    """RunnableLambda converts a python callable into a Runnable."""

    def __init__(self, func: Callable):
        self.func = func

    def invoke(self, input: Input) -> Output:
        return self.func(input)
```

RunnableLambda is a sub-class of Runnable that takes a function and executes the function on inputs to `invoke`. By calling `coerce_to_runnable`, functions are wrapped in RunnableLambda instances.

That lets us chain with arbitrary functions:

```python
d = Adder(9) | str
assert d.invoke(1) == "10"
# or even a lambda:
e = Adder(9) | (lambda i: f"value: {i}")
assert e.invoke(1) == "value: 10"
```

The downside to this approach is that we must have at least one Runnable in the chain or Python won't know we're expecting to produce a RunnableSequence, which could be unintuitive if you didn't understand how LangChain overrides the binary OR operator.

Overall, I found myself surprised at how easy it is to achieve this complex bit of syntactic sugar. I'm not sure this is better than the more vanilla approach used by scikit-learn's [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html), for example, but the approach is interesting and creates a unique feel to the core operation in LangChain: chaining together operations.

_You might also be interested in reading about how Langfuse monitors function calls in the OpenAI Python library [with "drop-in replacement" imports]({% post_url 2024-10-07-python-wrapping %})._
