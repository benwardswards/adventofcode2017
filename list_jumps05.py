from typing import List


class Jumpmachine:
    def __init__(self, instructions):
        self.length = len(instructions)
        self.instructions = instructions
        self.location = 0
        self.steps = 0

    def new_state(self):
        new_location = self.location + self.instructions[self.location]
        self.instructions[self.location] += 1
        self.location = new_location

    def jump_list(self):
        while 0 <= self.location < self.length:
            self.new_state()
            self.steps += 1
            # print(self.location)
            # print(self.instructions)
        return self.steps

    def new_state_part2(self):
        new_location = self.location + self.instructions[self.location]
        if self.instructions[self.location] <= 2:
            self.instructions[self.location] += 1
        else:
            self.instructions[self.location] += -1
        self.location = new_location

    def jump_list_part2(self):
        while 0 <= self.location < self.length:
            self.new_state_part2()
            self.steps += 1
            # print(self.location)
            # print(self.instructions)
        return self.steps

    def current_state(self):
        print(self.location, self.steps)
        print(self.instructions)


instructions_test = [0, 3, 0, 1, -3]

my_test_machine = Jumpmachine(instructions_test)
my_test_machine.current_state()


print(f"The number of steps to process the test was {my_test_machine.jump_list()}")


with open("day05.txt", "r") as file:
    instructions = [int(str_num) for str_num in file.readlines()]


my_machine = Jumpmachine(instructions)
print(f"The number of steps to process the instructions was {my_machine.jump_list()}")

instructions_test = [0, 3, 0, 1, -3]
my_test_machine = Jumpmachine(instructions_test)


print(
    f"The number of steps to process the test for part 2 is {my_test_machine.jump_list_part2()}"
)

with open("day05.txt", "r") as file:
    instructions = [int(str_num) for str_num in file.readlines()]

my_machine = Jumpmachine(instructions)


print(f"The number of steps for part 2 to process is  {my_machine.jump_list_part2()}")

