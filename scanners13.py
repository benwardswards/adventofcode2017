from collections import namedtuple
from os import name
from collections import namedtuple
from typing import List


def caught(delay: int, indexs: List[int], lengths: List[int]) -> bool:
    for ind, length in zip(indexs, lengths):
        if ((delay + ind) % (2 * (length - 1))) == 0:
            return True
    return False


def min_delay(indexs: List[int], lengths: List[int]):
    """finds the first time when you can avoid getting caught by the scanner"""
    delay: int = 0
    while caught(delay, indexs, lengths):
        delay = delay + 1
    return delay


def severity(indexs: List[int], lengths: List[int]) -> int:
    total: int = 0
    for ind, length in zip(indexs, lengths):
        # the scanner returns to the top every 2 * (length-1) time steps
        if ind % (2 * (length - 1)) == 0:
            total += ind * length  # if your caught this is the penalty
    return total


##test set
indexs = [0, 1, 4, 6]
lengths = [3, 2, 4, 4]
assert severity(indexs, lengths) == 24
assert min_delay(indexs, lengths) == 10

with open("day13.txt") as file:
    data_str = file.readlines()

data = [d.strip().split(": ") for d in data_str]

indexs = [int(d[0]) for d in data]
lengths = [int(d[1]) for d in data]

print("The severity is", severity(indexs, lengths))

print("min delay not to get caught is", min_delay(indexs, lengths))
