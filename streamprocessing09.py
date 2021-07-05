from typing import List


def remove_exclamation(stream: str) -> List[str]:
    output = []
    delete_next = False
    for char in list(stream):
        # print(char)
        if delete_next == False:
            if char == "!":
                delete_next = True
            else:
                output.append(char)
        else:  # we delete by not appending to output
            delete_next = False

    return output


def remove_garbage(streams: List[str]) -> List[str]:
    output: List[str] = []
    delete_next: bool = False
    deleted_chars: int = 0
    for char in streams:
        if delete_next:  # in deleting mode, looking for ">" to end delete mode.
            if char == ">":
                delete_next = False
            else:
                deleted_chars += 1
        else:  # not in deleted mode, looking for "<" to start delete mode
            if char == "<":
                delete_next = True
            else:
                output.append(char)  # keep char by appending to output
    print("deleted chars", deleted_chars)
    return output


assert remove_garbage(remove_exclamation("<>")) == []
assert remove_garbage(remove_exclamation("<random characters>")) == []
assert remove_garbage(remove_exclamation("<<<<>")) == []
assert remove_garbage(remove_exclamation("<{!>}>")) == []
assert remove_garbage(remove_exclamation("<!!>")) == []
assert remove_garbage(remove_exclamation("<!!!>>")) == []
assert remove_garbage(remove_exclamation("""<{o"i!a,<{i<a>""")) == []


def print_list(str_list: List[str]):
    print("".join(str_list))


def score(str_list: List[str]) -> int:
    count = 0
    depth = 1
    for char in str_list:
        if char == "{":
            count += depth
            depth += 1
        elif char == ",":
            pass
        elif char == "}":
            depth -= 1
        elif char == "\n":
            pass
        else:
            print("char is:", char)
            raise TypeError("should be {,} or ,")
    return count


L1 = "<{!>}>"
L2 = "{{<!>},{<!>},{<!>},{<a>}}"
L3 = "{{<!!>},{<!!>},{<!!>},{<!!>}}"
L4 = "{{<ab>},{<ab>},{<ab>},{<ab>}}"
L5 = "{{<a!>},{<a!>},{<a!>},{<ab>}}"
L6 = "{{{},{},{{}}}}"


def stream_process(stream: str) -> int:
    print(stream)
    str_list = remove_exclamation(stream)
    print_list(str_list)
    str_list = remove_garbage(str_list)
    print_list(str_list)
    return score(str_list)


print("score is ", stream_process(L1))
print("score is ", stream_process(L2))
print("score is ", stream_process(L3))
print("score is ", stream_process(L4))
print("score is ", stream_process(L5))
print("score is ", stream_process(L6))


if __name__ == "__main__":
    with open("day09.txt") as file:
        data = file.read()

    print("score is ", stream_process(data))
