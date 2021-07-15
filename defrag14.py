from os import name
from knothash10 import hash_hash
import numpy as np
from collections import namedtuple
from copy import deepcopy

print("done importing")
puzzle_input = "xlqgujun"
key_string = "flqrgnkx"

print("f in hex is:", bin(int("f", 16)))


def hex_to_bin(str):
    return bin(int(str, 16))[2:].zfill(128)


hash_of_test = hash_hash("flqrgnkx-0")
print("""hash_hash("flqrgnkx-0"):""", hash_of_test)
firstrow = hex_to_bin(hash_of_test)
print("The len of a row including 0b is ", len(list(firstrow)))
print("in binary: ", firstrow)

print("check this looks the same as example")
for i in range(8):
    output = hex_to_bin(hash_hash("flqrgnkx-" + str(i)))
    print(output[:8])


def memory_used(input_string):
    total = 0
    for i in range(128):
        output = hex_to_bin(hash_hash(input_string + "-" + str(i)))
        total += sum([int(d) for d in output])
    return total


def matrix_make(input_string):
    mat = []
    for i in range(128):
        binary_string = hex_to_bin(hash_hash(input_string + "-" + str(i)))

        row = [int(d) for d in binary_string]
        mat.append(row)
    return np.matrix(mat)


Point = namedtuple("Point", "x z")


def num_regions(matrix_input):
    mat = deepcopy(matrix_input)
    regions = 0
    for i in range(128):
        for j in range(128):
            if mat[i, j] == 1:
                mat[i, j] = 0
                to_visit = [Point(i, j)]
                while to_visit:
                    # print(to_visit)
                    next_point = to_visit.pop(0)
                    # up
                    point = Point(next_point.x, next_point.z - 1)
                    if point.z > -1:
                        if mat[point.x, point.z] == 1:
                            to_visit.append(point)
                            mat[point.x, point.z] = 0
                    # down
                    point = Point(next_point.x, next_point.z + 1)
                    if point.z < 128:
                        if mat[point.x, point.z] == 1:
                            to_visit.append(point)
                            mat[point.x, point.z] = 0
                    # right
                    point = Point(next_point.x + 1, next_point.z)
                    if point.x < 128:
                        if mat[point.x, point.z] == 1:
                            to_visit.append(point)
                            mat[point.x, point.z] = 0
                    # left
                    point = Point(next_point.x - 1, next_point.z)
                    if point.x > -1:
                        if mat[point.x, point.z] == 1:
                            to_visit.append(point)
                            mat[point.x, point.z] = 0
                regions += 1

    return regions


if __name__ == "__main__":

    TEST_INPUT = "flqrgnkx"
    assert memory_used(TEST_INPUT) == 8108

    assert num_regions(matrix_make(TEST_INPUT)) == 1242

    DATA_INPUT = "xlqgujun"

    print("memory used for the input is: ", memory_used(DATA_INPUT))

    print("number of regions in memeory", num_regions(matrix_make(DATA_INPUT)))
