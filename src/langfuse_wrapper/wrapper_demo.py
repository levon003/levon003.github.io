from re_wrapper import re, modifier


def main():
    memory = modifier.initialize().memory
    assert len(memory) == 0
    match = re.search("a", "abcdef")
    assert len(memory) == 1
    assert memory[0]["result"] == match

    print(memory)


if __name__ == "__main__":
    main()
