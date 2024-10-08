# created as an MRE: see https://gist.github.com/levon003/a96bf9d2f7fa3f97a9574e0d39545b8e
import wrapt
import re


def wrap():
    def wrapper(wrapped, instance, args, kwargs):
        result = wrapped(*args, **kwargs)
        print(result)
        return result

    return wrapper


def main():
    # no wrapping
    re.search("a", "abc")
    pattern = re.compile("a")
    pattern.search("abc")

    wrapt.wrap_function_wrapper(re, "search", wrap())
    re.search("a", "abc")

    # ill-advised, but fails for the same reason: wrapt.wrap_object_attribute(re, "Pattern.search", wrap())
    wrapt.wrap_function_wrapper(re, "Pattern.search", wrap())  # fails
    pattern = re.compile("a")
    pattern.search("abc")


if __name__ == "__main__":
    main()
