import math


def process_binary(bin_stream):
    global sum_of_versions
    version = int(bin_stream[:3], 2)
    type = int(bin_stream[3:6], 2)
    bin_stream = bin_stream[6:]

    sum_of_versions += version
    print("V: " + str(version) + "; T: " + str(type) + "; bin_str: " + bin_stream)
    val = 0
    if type == 4:
        val, bin_stream = parse4(bin_stream)
    elif bin_stream[0] == '0':
        val, bin_stream = parse0(type, bin_stream[1:])
    else:
        val, bin_stream = parse1(type, bin_stream[1:])
    return val, bin_stream


def parse1(type, bin_stream):
    print("type 1")
    binary = bin_stream[:11]
    bin_stream = bin_stream[11:]
    vals = []
    for i in range(int(binary, 2)):
        print("i = " + str(i))
        val, bin_stream = process_binary(bin_stream)
        vals.append(val)
    return calculate_value(type, vals), bin_stream


def parse0(type, bin_stream):
    print("type 0")
    binary = int(bin_stream[:15], 2)
    bin_stream = bin_stream[15:]

    vals = []
    while binary:
        stream_len = len(bin_stream)
        val, bin_stream = process_binary(bin_stream)
        vals.append(val)
        binary -= (stream_len - len(bin_stream))
        if binary < 0:
            print("ERR")
    return calculate_value(type, vals), bin_stream


def parse4(bin_stream):
    print("type 4")
    result = ''
    while True:
        binary = bin_stream[:5]
        result += binary[1:]
        bin_stream = bin_stream[5:]
        if binary[0] == '0':
            break
    return int(result, 2), bin_stream


def calculate_value(type, vals):
    switch = {
        0: sum(vals),
        1: math.prod(vals),
        2: min(vals),
        3: max(vals),
        5: 1 if len(vals) == 2 and vals[0] > vals[1] else 0,
        6: 1 if len(vals) == 2 and vals[0] < vals[1] else 0,
        7: 1 if len(vals) == 2 and vals[0] == vals[1] else 0,
    }
    return switch.get(type)


with open("data.in") as file:
    line = file.read().strip()
    binary_stream = bin(int(line, 16))[2:]

    print(binary_stream)

    sum_of_versions = 0
    val, bin_str = process_binary(binary_stream)

    print(bin_str)
    print()
    print("1: " + str(sum_of_versions))
    print("2: " + str(val))
