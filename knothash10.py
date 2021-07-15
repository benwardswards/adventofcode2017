"""https://adventofcode.com/2017/day/10"""


from typing import Hashable, List


input_list_test = [3, 4, 1, 5]
print(input_list_test)


class Hash_knot:
    def __init__(self, skip_sizes, list_length=256):
        self.list_length = list_length
        self.skip_sizes = skip_sizes
        self.position = 0
        self.circle = [i for i in range(list_length)]
        self.skip = 0

    def __repr__(self):
        return f"position {self.position} skip {self.skip} list {self.circle}"

    def fold(self, length):
        output = self.circle.copy()
        for i in range(length):
            in_loc = (i + self.position) % self.list_length
            out_loc = self.out_index(length, i)
            # print(i, in_loc, out_loc)
            output[out_loc] = self.circle[in_loc]
        self.circle = output

        self.position = (self.position + self.skip + length) % self.list_length
        self.skip += 1
        # print(self)

    def out_index(self, length, location):
        out = (length - 1 - location + self.position) % self.list_length
        return out

    def process_list(self):
        # print("to start")
        # print(self)
        for size in self.skip_sizes:
            self.fold(size)

        return self.circle[0] * self.circle[1]


hash_knot_test = Hash_knot(input_list_test, list_length=5)
print(hash_knot_test)


assert hash_knot_test.process_list() == 12

input_list = [97, 167, 54, 178, 2, 11, 209, 174, 119, 248, 254, 0, 255, 1, 64, 190]

hash_knot = Hash_knot(input_list)

print("The check product is:", hash_knot.process_list())

input_str_test = "1,2,3"
input_str = "97,167,54,178,2,11,209,174,119,248,254,0,255,1,64,190"


def to_ascii_end(string):
    """map to asscii for each elment in the string. Then at a special ending"""
    temp = [ord(char) for char in string]
    end_edit = [17, 31, 73, 47, 23]
    for char in end_edit:
        temp.append(char)
    return temp


def sparse_to_dense(list_ints):
    temp = list_ints[0]
    output = []
    for i, num in enumerate(list_ints):
        if i % 16 == 0:
            if i != 0:

                output.append(hex(temp))
                temp = num
        else:
            temp ^= num
    output.append(hex(temp))
    out_str = ""
    for hex_digits in output:
        a = str(hex_digits)[2:]
        # print(a)
        if len(a) < 2:
            a = "0" + a
        out_str += a
    return out_str


def hash_hash(input_string):
    hash_knot = Hash_knot(to_ascii_end(input_string))

    for _ in range(64):
        hash_knot.process_list()

    dense_hash = sparse_to_dense(hash_knot.circle)
    assert len(dense_hashls) == 32, "invalid hash length"
    return dense_hash


if __name__ == "__main__":
    print("to asscii:", to_ascii_end(""))
    assert (
        sparse_to_dense(
            [
                65,
                27,
                9,
                1,
                4,
                3,
                40,
                50,
                91,
                7,
                6,
                0,
                2,
                5,
                68,
                22,
                65,
                27,
                9,
                1,
                4,
                3,
                40,
                50,
                91,
                7,
                6,
                0,
                2,
                5,
                68,
                22,
            ]
        )
        == "4040"
    )

    assert hash_hash("") == "a2582a3a0e66e6e86e3812dcb672a272"
    assert hash_hash("AoC 2017") == "33efeb34ea91902bb2f59c9920caa6cd"
    assert hash_hash("1,2,3") == "3efbe78a8d82f29979031a4aa0b16a9d"
    assert hash_hash("1,2,4") == "63960835bcdc130f0b66d7ff4f6a5a8e"

    print("hash of input string is:", hash_hash(input_str))
    print([chr(i) for i in [17, 31, 73, 47, 23]])
