import numpy as np

with open("day06.txt") as file:
    memory1 = [int(bank) for bank in file.readline().split("\t")]

print(memory1)

test_memory = [0, 2, 7, 0]


class Memory_reallocation:
    def __init__(self, memory):
        self.memory = memory
        self.length = len(memory)
        self.visited_states = set()

    def next_state(self):
        idx_max = np.argmax(self.memory)
        redistributions = self.memory[idx_max]
        self.memory[idx_max] = 0
        index_to_add = (idx_max + 1) % self.length

        for _ in range(redistributions):
            self.memory[index_to_add] += 1
            index_to_add = (index_to_add + 1) % self.length

    def run(self):
        cycles = 0
        while tuple(self.memory) not in self.visited_states:
            cycles += 1
            self.visited_states.add(tuple(self.memory))
            self.next_state()

        return cycles

    def next_repeat(self):
        cycles = 1
        initial_state = self.memory.copy()
        self.next_state()
        while self.memory != initial_state:
            cycles += 1
            self.next_state()

        return cycles


my_test_bank = Memory_reallocation(test_memory)
print(f"The number of cylces for the test data is :", my_test_bank.run())
print(f"we see the memory again at :", my_test_bank.next_repeat())

my_bank = Memory_reallocation(memory1)
print(f"The number of cylces for the data is :", my_bank.run())
print(f"we see the memory again at :", my_bank.next_repeat())

