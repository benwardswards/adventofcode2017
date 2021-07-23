from collections import namedtuple
from os import name
from typing import NamedTuple
from string import ascii_uppercase

with open("day19_test.txt") as file:
    testdata = [list(line.strip("\n")) for line in file.readlines()]

lenz = len(testdata)
lenx = len(testdata[0])
print(lenx, lenz)

# print(len(testdata))
# print(testdata)

for line in testdata:
    print(line)

Point = namedtuple("Point", "x z")
start_loc_test = Point(5, 0)

print(testdata[start_loc_test.z][start_loc_test.x])

letters = set(list(ascii_uppercase))
print(letters)


class Tubes:
    def __init__(self, network, start_location: Point, direction):
        self.network = network
        self.start_location = start_location
        self.direction = direction
        self.loc = self.start_location
        self.visited = []
        self.steps = 0

    def next_loc(self):
        self.steps += 1
        if self.direction == "d" or self.direction == "u":
            if self.direction == "d":
                next_loc = Point(self.loc.x, self.loc.z + 1)
            else:
                next_loc = Point(self.loc.x, self.loc.z - 1)
            next_char = self.network[next_loc.z][next_loc.x]
            if next_char == " ":
                print("steps", self.steps)
                return False
            print(next_loc)
            if next_char in "+":
                if self.network[next_loc.z][next_loc.x + 1] == " ":
                    self.direction = "l"
                elif self.network[next_loc.z][next_loc.x - 1] == " ":
                    self.direction = "r"
                else:
                    raise TypeError("invalid direction find")
            else:
                if next_char in letters:
                    self.visited.append(next_char)
        else:
            if self.direction == "r":
                next_loc = Point(self.loc.x + 1, self.loc.z)
            else:
                next_loc = Point(self.loc.x - 1, self.loc.z)
            next_char = self.network[next_loc.z][next_loc.x]
            print(next_loc)
            if next_char == " ":
                print("steps", self.steps)

                return False
            if next_char in "+":
                if self.network[next_loc.z + 1][next_loc.x] == " ":
                    self.direction = "u"
                elif self.network[next_loc.z - 1][next_loc.x] == " ":
                    self.direction = "d"
                else:
                    raise TypeError("invalid direction find")
            else:
                if next_char in letters:
                    self.visited.append(next_char)
        self.loc = next_loc
        return True

    def path(self):
        while self.next_loc():
            print(test_tube)
        test_tube.print_state()

        return "".join(self.visited)

    def __repr__(self):
        return f"direction: {self.direction}, char = {self.network[self.loc.z][self.loc.x]} loc : {self.loc}, visited= {self.visited}"

    def print_state(self):

        for iline, line in enumerate(self.network):
            for ichar, char in enumerate(line):
                if iline == self.loc.z and ichar == self.loc.x:
                    print("*", end="")
                else:
                    print(char, end="")
            print()


test_tube = Tubes(testdata, start_loc_test, "d")
test_tube.print_state()
print(test_tube)

print(test_tube.path())


if __name__ == "__main__":

    with open("day19.txt") as file:
        data = [list(line.strip("\n")) for line in file.readlines()]

    lenz = len(data)
    lenx = len(data[0])
    print(lenx, lenz)

    start_loc = Point(19, 0)
    test_tube = Tubes(data, start_loc, "d")
    test_tube.print_state()

    print(test_tube.path())
