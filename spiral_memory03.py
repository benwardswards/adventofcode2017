from typing import Tuple
from math import sqrt
from math import floor
import numpy as np


def perfect_odd_square_lower(number: int) -> int:
    square = floor(sqrt(number))
    if square % 2 == 0:
        return square - 1
    else:
        return square


assert perfect_odd_square_lower(49) == 7
assert perfect_odd_square_lower(50) == 7
assert perfect_odd_square_lower(16) == 3
assert perfect_odd_square_lower(17) == 3
assert perfect_odd_square_lower(1) == 1


def spiral_location(number: int) -> Tuple[int]:
    square = perfect_odd_square_lower(number)
    level = (square + 1) // 2
    remainder = number - square ** 2

    side_length = (level) * 2
    print(number, square, level, side_length, remainder)
    if square * square == number:
        # at the corner
        (x, y) = (level - 1, -level + 1)
        return (x, y)
    elif remainder <= side_length:
        # rgihtside
        return (level, -level + remainder)
    elif remainder <= 2 * side_length:
        # top
        return (level - (remainder - side_length), level)
    elif remainder <= 3 * side_length:
        # leftside
        return (-level, level - (remainder - 2 * side_length))
    elif remainder <= 4 * side_length:
        # bottom
        return (-level + (remainder - 3 * side_length), -level)
    else:
        raise ValueError("Algorithm broken remainder error")

    raise ValueError("broken")


assert spiral_location(2) == (1, 0)
assert spiral_location(9) == (1, -1)
assert spiral_location(1) == (0, 0)
assert spiral_location(25) == (2, -2)

assert spiral_location(3) == (1, 1)
assert spiral_location(4) == (0, 1)
assert spiral_location(5) == (-1, 1)
assert spiral_location(6) == (-1, 0)
assert spiral_location(7) == (-1, -1)
assert spiral_location(8) == (0, -1)
assert spiral_location(23) == (0, -2)


def manhatten_distance(x, y) -> int:
    return abs(x) + abs(y)


def memory_steps(number: int) -> int:
    return manhatten_distance(*spiral_location(number))


assert memory_steps(1) == 0
assert memory_steps(12) == 3
assert memory_steps(23) == 2
assert memory_steps(1024) == 31

puzzel_input = 325489
print(f"The number of steps is {memory_steps(puzzel_input)}")

# part 2
# puzzel_input = 133

length = 15

memory_matrix = np.zeros((2 * length + 1, 2 * length + 1), dtype=int)

xzero = length
zzero = length

numberwritten = 1
number = 1
memory_matrix[xzero, zzero] = 1


def sum_neighbors(m, x, z) -> int:
    # print(m.shape, x, z)
    return (
        m[x + 1, z]
        + m[x - 1, z]
        + m[x, z + 1]
        + m[x, z - 1]
        + m[x + 1, z + 1]
        + m[x + 1, z - 1]
        + m[x - 1, z + 1]
        + m[x - 1, z - 1]
    )


while numberwritten < puzzel_input:
    print(numberwritten)
    number += 1
    x, z = spiral_location(number)
    x += xzero
    z += zzero
    numberwritten = sum_neighbors(memory_matrix, x, z)
    memory_matrix[x, z] = numberwritten

print(numberwritten)

