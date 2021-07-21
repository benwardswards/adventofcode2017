from collections import defaultdict
from collections import deque

with open("day18_test.txt") as file:
    testdata_raw = file.readlines()

with open("day18.txt") as file:
    inputdata_raw = file.readlines()

with open("day18_test2.txt") as file:
    testdata_raw2 = file.readlines()


def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


testdata = [data.strip().split(" ") for data in testdata_raw]
testdata_2 = [data.strip().split(" ") for data in testdata_raw2]

inputdata = [data.strip().split(" ") for data in inputdata_raw]

print(testdata)
print(inputdata)


def duet(input_data):
    registers = defaultdict(int)
    output = []
    index_data = 0
    while True:
        data = input_data[index_data]
        instruction = data[0]
        op1 = data[1]

        if len(data) == 3:
            if is_digit(data[2]):
                Y = int(data[2])
            else:
                Y = registers[data[2]]

            if instruction == "set":
                registers[op1] = Y
            elif instruction == "add":
                registers[op1] += Y
            elif instruction == "mul":
                registers[op1] *= Y
            elif instruction == "mod":
                registers[op1] %= Y
            elif instruction == "jgz":
                if registers[op1] > 0:
                    index_data += Y - 1

        elif len(data) == 2:
            if instruction == "snd":
                output.append(registers[op1])
            elif instruction == "rcv":
                if registers[op1] != 0:
                    print(f"recovered :{output[-1]}")
                    recover = output[-1]
                    break
            else:
                raise TypeError(f"invalid instruction:{ instruction}")
        else:
            raise TypeError("invalid intruction length")
        index_data += 1
    return recover


assert duet(testdata) == 4

print(duet(inputdata))


def duet_part2(program_id, input_data, receive):
    sent = 0
    registers = defaultdict(int)
    registers["p"] = program_id
    index_data = 0
    print(input_data)
    while True:
        if index_data >= len(input_data):
            print("index out of range")
            break

        data = input_data[index_data]
        instruction = data[0]

        op1 = data[1]

        if len(data) == 3:
            if is_digit(data[2]):
                Y = int(data[2])
            else:
                Y = registers[data[2]]

            if instruction == "set":
                registers[op1] = Y
            elif instruction == "add":
                registers[op1] += Y
            elif instruction == "mul":
                registers[op1] *= Y
            elif instruction == "mod":
                registers[op1] %= Y
            elif instruction == "jgz":
                if is_digit(op1):
                    X = int(op1)
                else:
                    X = registers[op1]
                if X > 0:
                    print("jumped from", index_data, end=" ")
                    index_data += Y - 1
                    print("to", index_data)

        elif len(data) == 2:
            if instruction == "snd":
                if is_digit(data[1]):
                    op1 = int(data[1])
                else:
                    op1 = registers[data[1]]
                # print("program", program_id, "sends", op1)
                sent += 1
                yield op1
            elif instruction == "rcv":
                op1 = data[1]
                if receive:
                    print("program", program_id, "receives", op1)
                    registers[op1] = receive.popleft()
                else:
                    print("wait", program_id, registers)
                    print(program_id, "sent", sent)
                    index_data -= 1
                    yield "wait"
            else:
                raise TypeError(f"invalid instruction:{ instruction}")
        else:
            raise TypeError("invalid intruction length")
        index_data += 1


print("START part 2")
print(inputdata)
data = inputdata
# data = testdata_2
print(data)
recieve0 = deque()
recieve1 = deque()
program0 = duet_part2(0, data, recieve0)
program1 = duet_part2(1, data, recieve1)


while True:
    print(0, recieve0)
    print(1, recieve1)
    send0 = next(program0)
    send1 = next(program1)
    if send0 != "wait":
        recieve1.append(send0)
    if send1 != "wait":
        recieve0.append(send1)

    if send0 == "wait" and send1 == "wait":
        print("deadlock")
        break

