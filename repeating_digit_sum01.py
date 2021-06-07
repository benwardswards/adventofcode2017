def repeat_digit_sum(digits: int) -> int:
    digit_list = list(str(digits))
    digit_list_next = digit_list[:-1]
    digit_list_next.insert(0, digit_list[-1])

    total: int = 0
    for digit, nextdigit in zip(digit_list, digit_list_next):

        if digit == nextdigit:
            total += int(digit)
    return total


assert repeat_digit_sum(1234) == 0
assert repeat_digit_sum(1122) == 3
assert repeat_digit_sum(1111) == 4
assert repeat_digit_sum(91212129) == 9

with open("day01.txt", "r") as file:
    bignumber = int(file.read())

print(f"The sum of the repeated digits is {repeat_digit_sum(bignumber)}.")


def halfwaypair(index: int, digit_length) -> int:
    return (digit_length // 2 + index) % digit_length


assert halfwaypair(0, 10) == 5
assert halfwaypair(9, 10) == 4
assert halfwaypair(0, 2) == 1


def halfway_digit_sum(digits: int) -> int:
    digit_list = list(str(digits))
    number_digits = len(digit_list)

    total: int = 0
    for index, digit, in enumerate(digit_list):

        if digit == digit_list[halfwaypair(index, number_digits)]:
            total += int(digit)
    return total


assert halfway_digit_sum(1212) == 6
assert halfway_digit_sum(1221) == 0
assert halfway_digit_sum(123123) == 12
assert halfway_digit_sum(123425) == 4

print(f"The sum of the repeated halfway digits is {halfway_digit_sum(bignumber)}.")
