"""If you use the OpenAI Python SDK, you can use the Langfuse drop-in replacement to get full logging by changing only the import.

```diff
- import openai
+ from langfuse.openai import openai
```

Langfuse automatically tracks:

- All prompts/completions with support for streaming, async and functions
- Latencies
- API Errors
- Model usage (tokens) and cost (USD)

The integration is fully interoperable with the `observe()` decorator and the low-level tracing SDK.

See docs for more details: https://langfuse.com/docs/integrations/openai
"""

from typing import Optional

from wrapt import wrap_function_wrapper

import re


class ReDefinition:
    module: str
    function_name: str  # e.g. Completions.create

    def __init__(self, module: str, function_name: str):
        self.module = module
        self.function_name = function_name


RE_METHODS = [
    ReDefinition(
        module="re",
        function_name="search",
    )
]


class WrapperClient:
    def __init__(self):
        self.memory = []


"""
OPENAI_METHODS_V1 = [
    OpenAiDefinition(
        module="openai.resources.chat.completions",
        object="Completions",
        method="create",
        type="chat",
        sync=True,
    ),
    OpenAiDefinition(
        module="openai.resources.completions",
        object="Completions",
        method="create",
        type="completion",
        sync=True,
    ),
    OpenAiDefinition(
        module="openai.resources.chat.completions",
        object="AsyncCompletions",
        method="create",
        type="chat",
        sync=False,
    ),
    OpenAiDefinition(
        module="openai.resources.completions",
        object="AsyncCompletions",
        method="create",
        type="completion",
        sync=False,
    ),
]"""


def _re_wrapper(func):
    def _with_re(re_definitions, initialize):
        # these are the arguments expected in a wrapt wrapper function
        # see: https://wrapt.readthedocs.io/en/master/quick-start.html
        def wrapper(wrapped, instance, args, kwargs):
            return func(re_definitions, initialize, wrapped, args, kwargs)

        return wrapper

    return _with_re


@_re_wrapper
def _wrap(re_resource: ReDefinition, initialize, wrapped, args, kwargs):
    new_langfuse: WrapperClient = initialize()
    new_memory = {"args": args, "kwargs": kwargs}

    try:
        result = wrapped(*args, **kwargs)
        new_memory["result"] = result
        return result
    except Exception as ex:
        new_memory["error"] = str(ex)
        raise ex
    finally:
        new_langfuse.memory.append(new_memory)


class ReWrapped:
    _wrapper_client: Optional[WrapperClient] = None

    def initialize(self) -> WrapperClient:
        if self._wrapper_client is None:
            self._wrapper_client = WrapperClient()
        return self._wrapper_client

    def register_tracing(self):
        resources = RE_METHODS
        for resource in resources:
            wrap_function_wrapper(
                resource.module,
                resource.function_name,
                (_wrap(resource, self.initialize)),
            )


modifier = ReWrapped()
modifier.register_tracing()
