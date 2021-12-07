from collections import defaultdict

with open("data.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    count1 = 0
    count2 = 0
    board1 = defaultdict(int)
    board2 = defaultdict(int)

    for line in lines:
        start, end = line.split(' -> ')

        xStart = int(str(start.split(',')[0]).strip())
        yStart = int(str(start.split(',')[1]).strip())
        xEnd = int(str(end.split(',')[0]).strip())
        yEnd = int(str(end.split(',')[1]).strip())

        diffX = xEnd - xStart
        diffY = yEnd - yStart

        for i in range(max(abs(diffX), abs(diffY))):
            x = 0
            if diffX > 0:
                x = 1
            elif diffX < 0:
                x = -1
            x = xStart + x * i

            y = 0
            if diffY > 0:
                y = 1
            elif diffY < 0:
                y = -1
            y = yStart + y * i

            if diffX == 0 or diffY == 0:
                board1[(x, y)] += 1
            board2[(x, y)] += 1

    for val in board1.values():
        if val > 1:
            count1 += 1

    for val in board2.values():
        if val > 1:
            count2 += 1

    print("1: " + str(count1))
    print("2: " + str(count2))
