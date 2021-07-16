from typing import Generator
import copy

FACTOR_A = 16807
FACTOR_B = 48271
START_A = 722
START_B = 354
MAX = 40 * 10 ** 6
MAX2 = 5 * 10 ** 6

DIVIDE_BY = 2147483647


def next_gen(start: int, factor: int, divide_by):
    gen = copy.copy(start)
    while True:
        gen = (gen * factor) % divide_by
        yield bin(gen)[2:].zfill(32)[-16:]


def next_gen_A(start: int, factor: int, divide_by):
    gen = copy.copy(start)
    while True:
        gen = (gen * factor) % divide_by
        gen_str = bin(gen)[2:].zfill(32)[-16:]
        if gen_str[-2:] == "00":
            # print(gen)
            yield gen_str


def next_gen_B(start: int, factor: int, divide_by):
    gen = copy.copy(start)
    while True:
        gen = (gen * factor) % divide_by
        gen_str = bin(gen)[2:].zfill(32)[-16:]
        if gen_str[-3:] == "000":
            # print(gen)
            yield gen_str


gen_a = next_gen(65, FACTOR_A, DIVIDE_BY)
gen_b = next_gen(8921, FACTOR_B, DIVIDE_BY)

for _ in range(5):
    print(f"{next(gen_a):<15} {next(gen_b) :<15}")


def number_matches(
    start_a=START_A,
    start_b=START_B,
    factor_a=FACTOR_A,
    factor_b=FACTOR_B,
    divide_by=DIVIDE_BY,
    matches=MAX,
):

    gen_a = next_gen(start_a, factor_a, divide_by)
    gen_b = next_gen(start_b, factor_b, divide_by)

    MAX = 40 * 10 ** 6
    total = sum(1 if next(gen_a) == next(gen_b) else 0 for _ in range(MAX))

    return total


def number_matches_part2(
    start_a=START_A,
    start_b=START_B,
    factor_a=FACTOR_A,
    factor_b=FACTOR_B,
    divide_by=DIVIDE_BY,
    matches=MAX2,
):

    gen_a = next_gen_A(start_a, factor_a, divide_by)
    gen_b = next_gen_B(start_b, factor_b, divide_by)
    total = 0
    for i in range(matches):
        if next(gen_a) == next(gen_b):
            total += 1
            # print(i, total)
    return total


gen_a = next_gen_A(65, FACTOR_A, DIVIDE_BY)
gen_b = next_gen_B(8921, FACTOR_B, DIVIDE_BY)

print("part2 bits to check")
for _ in range(5):
    print(f"{next(gen_a):<15} {next(gen_b) :<15}")


if __name__ == "__main__":
    assert number_matches(start_a=65, start_b=8921) == 588
    print(f"The number of matches is: {number_matches()}")

    assert number_matches_part2(start_a=65, start_b=8921) == 309
    print(f"The number of matches for part 2 is:  {number_matches_part2()}")
