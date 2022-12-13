import ast
import functools


def cmp_pkt(packet1, packet2):
    if type(packet1) is type(packet2):
        if isinstance(packet1, list):
            i = 0
            while i < len(packet1) and i < len(packet2):
                order = cmp_pkt(packet1[i], packet2[i])
                i += 1
                if order == 0:
                    continue
                else:
                    return order
            if len(packet1) == len(packet2):
                return 0
            elif len(packet1) < len(packet2):
                return -1
            else:
                return 1
        else:
            if packet1 == packet2:
                return 0
            elif packet1 < packet2:
                return -1
            else:
                return 1
    elif type(packet1) == int:
        return cmp_pkt([packet1], packet2)
    else:
        return cmp_pkt(packet1, [packet2])


with open("data.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    packets = []
    packet1 = None
    packet2 = None
    pair_sum = 0
    pair_count = 0
    for line in lines:
        if line == "":
            if cmp_pkt(packet1, packet2) == -1:
                pair_sum += 1 + pair_count
            pair_count += 1
            packet1 = None
            packet2 = None
            continue
        packet = ast.literal_eval(line)
        if packet1 is None:
            packet1 = packet
        else:
            packet2 = packet
        packets.append(packet)
        # print(packets)
    print(pair_sum)

packets.append([[2]])
packets.append([[6]])

packets = sorted(packets, key=functools.cmp_to_key(lambda p1, p2: cmp_pkt(p1, p2)))
pair_sum = 1
pair_count = 0
for packet in packets:
    pair_count += 1
    if packet == [[2]] or packet == [[6]]:
        pair_sum *= pair_count
print(pair_sum)
