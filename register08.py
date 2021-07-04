from typing import List, DefaultDict
from collections import namedtuple, defaultdict


with open("day08.txt") as file:
    instruction_list = file.readlines()


for data in instruction_list:
    print(data.split())

Instruction = namedtuple(
    "Instruction",
    "register action increase_by if_ register_compare comparison compare_value",
)


def process_input(instructions: List[str]) -> List[Instruction]:
    output = []
    for instruction in instructions:
        list_ops = instruction.split()
        print(list_ops)
        output.append(
            Instruction(
                list_ops[0],
                list_ops[1],
                int(list_ops[2]),
                list_ops[3],
                list_ops[4],
                list_ops[5],
                int(list_ops[6]),
            )
        )
    return output


def comparison(oparand: str, v1: int, v2: int) -> bool:
    # print(oparand, v1, v2)

    if oparand == ">":
        return v1 > v2
    if oparand == "<":
        return v1 < v2
    if oparand == ">=":
        return v1 >= v2
    if oparand == "<=":
        return v1 <= v2
    if oparand == "==":
        return v1 == v2
    if oparand == "!=":
        return v1 != v2
    raise TypeError("comparison not supported")


assert comparison("==", 2, 2)
assert comparison("<=", 2, 3)
assert comparison("<", 2, 2) == False

insturctions_tuple = process_input(instruction_list)

registers_dict: DefaultDict[str, int] = defaultdict(int)


# register action increase_by if_ register_compare comparison compare_value"
max_per_step = []
for instruction in insturctions_tuple:
    if comparison(
        instruction.comparison,
        registers_dict[instruction.register_compare],
        instruction.compare_value,
    ):
        increase = instruction.increase_by
        if instruction.action == "dec":
            increase *= -1
        registers_dict[instruction.register] += increase

        max_per_step.append(max(registers_dict.values()))


print(registers_dict)

print("the maximum register value is", max(registers_dict.values()))

print("the maximum register value at any step is", max(max_per_step))

