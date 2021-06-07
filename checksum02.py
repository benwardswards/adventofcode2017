from typing import List

spreadsheet_test = [
    [5, 1, 9, 5,],
    [7, 5, 3,],
    [2, 4, 6, 8,],
]

spreadsheet_test2 = [
    [5, 9, 2, 8,],
    [9, 4, 7, 3,],
    [3, 8, 6, 5,],
]

print(spreadsheet_test)

with open("day02.txt", "r") as file:
    spreadsheet = []
    spreadsheet = [[int(item) for item in line.split()] for line in file]


def checksum(spreadsheet: List[List[int]]) -> int:
    diffs = [max(line) - min(line) for line in spreadsheet]
    return sum(diffs)


print(f"The check sum is {checksum(spreadsheet_test)}")
print(f"The check sum is {checksum(spreadsheet)}")


# part 2


def evenly_divide(row: List[int]) -> int:
    for r in row:
        for w in row:
            if r < w:
                if w % r == 0:
                    return w // r

    raise ValueError("no pair found")


assert evenly_divide([31, 5, 10, 7]) == 2


def checksum_divide(spreadsheet: List[List[int]]) -> int:
    diffs = [evenly_divide(line) for line in spreadsheet]
    return sum(diffs)


print(f"The check sum divisir is {checksum_divide(spreadsheet_test2)}")
print(f"The check sum divisor is {checksum_divide(spreadsheet)}")
