"""This is a drop-in replacement for the `re` module.
It enables monitoring of function calls with the re module by changing only the import.

```diff
- import re
+ from re_wrapper import re
```
See post for more details: https://levon003.github.io/2024/10/07/python-wrapping.html
"""

from typing import Optional

from wrapt import wrap_function_wrapper

import re


class ReDefinition:
    # I don't discuss this in the blog post, but ReDefinition is just a dataclass for the functions in re that will be replaced.
    # We can store any other metadata we like about the wrapped functions in the ReDefinition, which will be available in the wrapper function.
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
    # If we wanted to replace additional methods in re, we would just add them here.
    # Note there's a subtle "gotcha": you can't wrap functions on immutable objects e.g. function_name "Pattern.search".
    # This isn't a problem for Langfuse, since all the objects that openai creates are mutable.
]


class ReMonitor:
    def __init__(self):
        self.memory = []


def _re_wrapper(func):
    def _with_re(re_definition: ReDefinition, get_singleton_monitor):
        # These are the arguments expected in a wrapt wrapper function
        # See: https://wrapt.readthedocs.io/en/master/quick-start.html
        def wrapper(wrapped, instance, args, kwargs):
            return func(re_definition, get_singleton_monitor, wrapped, args, kwargs)

        return wrapper

    return _with_re


@_re_wrapper
def _wrap(re_resource: ReDefinition, get_singleton_monitor, wrapped, args, kwargs):
    monitor: ReMonitor = get_singleton_monitor()
    new_memory = {"function": re_resource.function_name, "args": args, "kwargs": kwargs}

    try:
        result = wrapped(*args, **kwargs)
        new_memory["result"] = result
        return result
    except Exception as ex:
        new_memory["error"] = str(ex)
        raise ex
    finally:
        monitor.memory.append(new_memory)


class ReWrapped:
    _monitor_singleton: Optional[ReMonitor] = None

    def get_singleton_monitor(self) -> ReMonitor:
        if self._monitor_singleton is None:
            self._monitor_singleton = ReMonitor()
        return self._monitor_singleton

    def register_tracing(self):
        resources = RE_METHODS
        for resource in resources:
            wrap_function_wrapper(
                resource.module,
                resource.function_name,
                (_wrap(resource, self.get_singleton_monitor)),
            )


modifier = ReWrapped()
modifier.register_tracing()
