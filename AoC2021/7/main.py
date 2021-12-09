import sys

with open("data.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    positions = lines[0].split(",")
    positions = [int(position) for position in positions]
    min_pos = min(positions)
    max_pos = max(positions)

    best = sys.maxsize

    for i in range(min_pos, max_pos + 1):
        cost = 0
        for pos in positions:
            cost += abs(i - pos)

        if cost < best:
            best = cost

    print("1: " + str(best))

    best = sys.maxsize

    for i in range(min_pos, max_pos + 1):
        cost = 0
        for pos in positions:
            diff = abs(i - pos)
            cost += (diff * (diff + 1)) // 2

        if cost < best:
            best = cost

    print("2: " + str(best))
