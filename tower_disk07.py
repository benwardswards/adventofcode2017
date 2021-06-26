import re
from collections import namedtuple

Disk = namedtuple("Disk", "name weight subdisks")
# with open("day07_test.txt") as file:
with open("day07.txt") as file:
    test_data = file.readlines()


test_string = "fwft (72) -> ktlj, cntj, xhth\n"
p = re.compile(r"\W+")
print(p.split(test_string))


def process_call(input_string: str) -> Disk:
    """converts a call(a string) in to a disk data strucutre"""

    p = re.compile(r"\W+")
    disk_l = p.split(input_string[:-1])  # remove \n from end of string
    # print(disk_l)
    if len(disk_l) > 3:
        subdisk = disk_l[2:]
    else:
        subdisk = None

    disk_out = Disk(disk_l[0], disk_l[1], subdisk)
    # print(disk_out)
    return disk_out


process_call(test_string)
process_call("fbrdpr (28)")  # have to make sure empty subnodes works

list_disks = [process_call(disk) for disk in test_data]

# for disk in list_disks:
#    print(disk)


class Node:
    def __init__(self, disk):
        self.name = disk.name
        self.weigth = int(disk.weight)
        self.subdisks = []

    def __repr__(self):
        return str(self.name) + " " + str(self.weigth)

    def pprint(self):
        subs = " ".join(str(disk.name) for disk in self.subdisks)
        print(str(self.name) + " " + str(self.weigth) + "->" + subs)
        for disk in self.subdisks:
            disk.pprint()

    def sum_check(self):
        """ all disks towers must be equal weight, finds the weights that are not equal and prints them out so you can figure out the off blance node, "lnpuarm is too heavy by 8"
        """
        weigth = self.weigth
        if self.subdisks:
            l_weights = [disk.sum_check() for disk in self.subdisks]
            weigth += sum(l_weights)

            for w in l_weights:
                if w != l_weights[0]:
                    print("weight of sub towers", l_weights)
                    print("with the correspnding disk:")
                    print(self.name, "->", self.subdisks, "\n")
                    break
        return weigth

    def find_up(self):
        """Looks throught the list a builds the tree out from the node"""
        print("calling find_up")
        # find self.name in list_disks:
        flag = 0
        for idx, disk in enumerate(list_disks):
            if disk.subdisks:  # checks not none
                if self.name in disk.subdisks:
                    thedisk = list_disks.pop(idx)
                    flag = 1
                    break

        if flag == 0:
            print("stop")
        print(f"To insert:{thedisk}")
        leaf = self
        self = Node(thedisk)
        self.subdisks.append(leaf)
        print("leaf is now", self.subdisks)
        print("root is now", self.name)
        thedisk.subdisks.remove(leaf.name)
        for disk in thedisk.subdisks:
            self.find_down(disk)
        print("after insertion")
        return self

    def find_down(self, disk_name):
        """Finds the leafs from the list and rescursively inserts there weights and subdisks"""
        print("calling find_down")
        # now search the list for a match
        for idx, disk in enumerate(list_disks):
            if disk_name in disk.name:
                disk_in_list = list_disks.pop(idx)
                break

        # need to creat the subdisks now
        leaf = Node(disk_in_list)
        # insert the leafs recursively
        if disk_in_list.subdisks:
            # checking if there are subdisks
            for disk_name in disk_in_list.subdisks:
                leaf = leaf.find_down(disk_name)

        # finally add the leafs into the node(rescursively)
        self.subdisks.append(leaf)
        return self


print()
root = Node(list_disks.pop(2))  # need to start with a leaf

while list_disks:
    root = root.find_up()

print()
root.pprint()
assert len(list_disks) == 0
print("the root:", root.name, "->", root.subdisks)

# print(root.sum_towers())
print("part2: finding misblance")
print()
print(root.sum_check())
