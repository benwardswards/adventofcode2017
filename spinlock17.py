PUZZLE_INPUT = 329
TEST_INPUT = 3
STEPS_PART2 = 50000000


def spinlock(puzzle_input, steps=2017):
    current_position = 0
    buffer = [0]
    for i in range(1, steps + 1):

        current_position = (current_position + puzzle_input) % i
        buffer.insert(current_position + 1, i)
        current_position += 1
        if current_position == 1:
            print(i, "new_zero", buffer[:4])
    return buffer


def spinlock_fast(puzzle_input, steps=2017):
    """The number zero is always in the first position of the buffer so the number insert at 1 will always be the number after 0"""
    current_position = 0
    after_0 = 1
    for i in range(1, steps + 1):
        current_position = (current_position + puzzle_input) % i + 1
        if current_position == 1:
            after_0 = i
            print(i, current_position, "new after zero ", after_0)

    return after_0


buffer = spinlock(TEST_INPUT)
index2017 = buffer.index(2017)
assert buffer[(index2017 - 3) : (index2017 + 4)] == [
    1512,
    1134,
    151,
    2017,
    638,
    1513,
    851,
]

buffer = spinlock(PUZZLE_INPUT)
index2017 = buffer.index(2017)
print(f"The number after 2017 for the puzzle input is: {buffer[index2017+1]}")

print("now running spinlock_fast")
after_zero = spinlock_fast(PUZZLE_INPUT, steps=STEPS_PART2)
print(f"The number after 0 is: {after_zero}")
