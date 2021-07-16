from string import ascii_lowercase

test_data = ["s1", "x3/4", "pe/b"]


def perm(input_list, number):
    return input_list[-number:] + input_list[:(-number)]


def process_data(data, length=16, times=1):
    programs = [letter for i, letter, in enumerate(ascii_lowercase) if i < length]
    # print(programs)
    for time in range(times):
        for d in data:
            if d[0] == "s":
                programs = perm(programs, int(d[1:]))
            elif d[0] == "x":
                i, j = d[1:].split("/")
                i = int(i)
                j = int(j)
                programs[i], programs[j] = programs[j], programs[i]
            elif d[0] == "p":
                A, B = d[1:].split("/")
                i = programs.index(A)
                j = programs.index(B)
                programs[i], programs[j] = programs[j], programs[i]

            else:
                raise TypeError("Don't know this dance!")
        # if the sequaence repeacts we don't have to keep running it, just run it 1 billion % times to repeat
        if programs == [
            letter for i, letter, in enumerate(ascii_lowercase) if i < length
        ]:

            repeat = time + 1
            print(
                f"The sequence repeats every {repeat} times so just run it {times%repeat} times not {10**9}"
            )
            return process_data(data, length=16, times=times % repeat)

    return "".join(programs)


print(test_data)
assert process_data(test_data, length=5) == "baedc"
assert process_data(test_data, length=5, times=2) == "ceadb"

if __name__ == "__main__":
    with open("day16.txt") as file:
        data = file.read().strip().split(",")

print("Part 1")
print(process_data(data, length=16, times=1))
"Part 2"
print(process_data(data, length=16, times=10 ** 9))

