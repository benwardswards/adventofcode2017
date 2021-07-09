import numpy as np
from collections import Counter

dict_dir = {
    "n": np.array([0, 2]),
    "ne": np.array([1, 1]),
    "se": np.array([1, -1]),
    "s": np.array([0, -2]),
    "sw": np.array([-1, -1]),
    "nw": np.array([-1, 1]),
}

assert all(dict_dir["n"] + dict_dir["ne"] == np.array([1, 3]))


def hex_dist(dist) -> int:
    """if abs(x) > abs (z) you have to zigzag back to the start."""
    x, z = dist
    if abs(x) > abs(z):
        moves = abs(x)
    else:
        moves = int((abs(x) + abs(z)) / 2)
    return moves


assert hex_dist((0, 0)) == 0
assert hex_dist((81, -33)) == 81
assert hex_dist((-1, -5)) == 3


def moves_to_start(list_of_directions):
    """Sums up the directions then caculates the number of moves back to start"""
    print("number of directions", len(list_of_directions))
    total_direction = np.array([0, 0])
    list_of_max_dirs = []
    for dir in list_of_directions:
        total_direction += dict_dir[dir]
        list_of_max_dirs.append(hex_dist(total_direction))
    max_away = max(list_of_max_dirs)
    print("The furthest distance away:", max_away)

    return hex_dist(total_direction)


assert moves_to_start("ne ne ne".split()) == 3
assert moves_to_start("ne ne sw sw".split()) == 0
assert moves_to_start("ne ne s s".strip().split()) == 2
assert moves_to_start("se sw se sw sw".split()) == 3
assert moves_to_start("sw nw".split()) == 2

with open("day11.txt") as f:
    dir_list = f.read().strip().split(",")

print(Counter(dir_list))

print(
    "The number of steps to take to get back to the start is:", moves_to_start(dir_list)
)

