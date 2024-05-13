from __future__ import annotations

from abc import ABC, abstractmethod
from typing import (
    Any,
    Callable,
    Generic,
    Iterator,
    List,
    Mapping,
    Union,
    TypeVar,
)


# Contravariant types: https://peps.python.org/pep-0484/#covariance-and-contravariance
Input = TypeVar("Input", contravariant=True)
Output = TypeVar("Output", contravariant=True)
Other = TypeVar("Other")


class Runnable(Generic[Input, Output], ABC):
    """A unit of work that can be invoked, batched, streamed, transformed and composed.

    The LangChain Expression Language (LCEL) is a declarative way to compose Runnables
    into chains. Any chain constructed this way will automatically have sync, async,
    batch, and streaming support.

    The main composition primitives are RunnableSequence and RunnableParallel.

    RunnableSequence invokes a series of runnables sequentially, with one runnable's
    output serving as the next's input. Construct using the `|` operator or by
    passing a list of runnables to RunnableSequence.

    .. code-block:: python

        from langchain_core.runnables import RunnableLambda

        # A RunnableSequence constructed using the `|` operator
        sequence = RunnableLambda(lambda x: x + 1) | RunnableLambda(lambda x: x * 2)
        sequence.invoke(1) # 4
        sequence.batch([1, 2, 3]) # [4, 6, 8]

    (Note: the langchain code here is under an MIT license. See source: https://github.com/langchain-ai/langchain/blob/f92006de3ce2ef6795c9a3f5bc798a8d2fa02bb7/libs/core/langchain_core/runnables/base.py)
    """

    def __or__(
        self,
        other: Union[
            Runnable[Any, Other],
            Callable[[Any], Other],
            Callable[[Iterator[Any]], Iterator[Other]],
            Mapping[str, Union[Runnable[Any, Other], Callable[[Any], Other], Any]],
        ],
    ) -> Runnable[Input, Other]:
        """Compose this runnable with another object to create a RunnableSequence."""
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
        """Compose this runnable with another object to create a RunnableSequence."""
        return RunnableSequence(coerce_to_runnable(other), self)

    @abstractmethod
    def invoke(self, input: Input) -> Output:
        """Transform a single input into an output. Override to implement.

        Args:
            input: The input to the runnable.

        Returns:
            The output of the runnable.
        """


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
        # invoke all steps in sequence
        try:
            for step in self.steps:
                input = step.invoke(input)
        # finish the root run
        except Exception as ex:
            raise ex
        else:
            return input


class RunnableLambda(Runnable[Input, Output]):
    """RunnableLambda converts a python callable into a Runnable."""

    def __init__(self, func: Callable):
        self.func = func

    def invoke(self, input: Input) -> Output:
        return self.func(input)


def coerce_to_runnable(thing) -> Runnable[Input, Output]:
    if isinstance(thing, Runnable):
        return thing
    elif callable(thing):
        return RunnableLambda(thing)
    else:
        raise TypeError("Expected a Runnable or callable.")


class Adder(Runnable):
    def __init__(self, value: int):
        self.value = value

    def invoke(self, input: Input) -> Output:
        return input + self.value


if __name__ == "__main__":
    a = Adder(5)
    assert a.invoke(1) == 6

    b = Adder(4)
    assert b.invoke(a.invoke(1)) == 10

    c = a | b
    assert c.invoke(1) == 10

    d = a | b | str
    assert d.invoke(1) == "10"

    e = a | b | (lambda i: f"value: {i}")
    assert e.invoke(1) == "value: 10"
