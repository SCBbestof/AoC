filename = 'data.in'

def draw(rocks, sands, part2 = False):
    print()
    # print(min_x, max_x)
    for y in range(max_y + 3):
        range_min_x = min_x - 10
        range_max_x = max_x + 10
        if filename == 'data.in' and part2:
            range_min_x = min_x - 150
            range_max_x = max_x + 150
        for x in range(range_min_x, range_max_x + 1):
            if (x, y) == (500, 0):
                print("+", end=" ")
            elif (x, y) in rocks and (x, y) not in sands:
                print("#", end=" ")
            elif (x, y) in sands:
                print("o", end=" ")
            elif y == max_y + 2:
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()
    print()


with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    pairs = []
    for line in lines:
        line = line.split(" -> ")
        line_pair = []
        for pair in line:
            x, y = pair.split(",")
            x, y = int(x), int(y)
            line_pair.append((x, y))
        pairs.append(line_pair)

    rocks = set()
    max_y = 0
    min_x, max_x = 9999, 0
    for line_pair in pairs:
        for i in range(len(line_pair) - 1):
            x, y = line_pair[i]
            next_x, next_y = line_pair[i + 1]
            if y > max_y:
                max_y = y
            if next_y > max_y:
                max_y = next_y
            # drawing :)
            if x > max_x:
                max_x = x
            if next_x > max_x:
                max_x = next_x
            if x < min_x:
                min_x = x
            if next_x < min_x:
                min_x = next_x

            if x == next_x:
                if y < next_y:
                    for k in range(y, next_y + 1):
                        rocks.add((x, k))
                else:
                    for k in range(next_y, y + 1):
                        rocks.add((x, k))
            else:
                if x < next_x:
                    for k in range(x, next_x + 1):
                        rocks.add((k, y))
                else:
                    for k in range(next_x, x + 1):
                        rocks.add((k, y))

    draw(rocks, set())

    part1_done = False
    part2_done = False
    count = 0
    part1 = 0
    sand_drawing = set()
    while not (part1_done and part2_done):
        if (500, 0) in rocks:
            part2_done = True
            break
        sand_x, sand_y = 500, 0
        while True:
            if sand_y == max_y + 1:
                if not part1_done:
                    draw(rocks, sand_drawing)
                    part1 = count
                part1_done = True
                rocks.add((sand_x, sand_y))
                sand_drawing.add((sand_x, sand_y))
                count += 1
                break
            elif (sand_x, sand_y + 1) not in rocks:
                sand_y += 1
            elif (sand_x - 1, sand_y + 1) not in rocks:
                sand_y += 1
                sand_x -= 1
            elif (sand_x + 1, sand_y + 1) not in rocks:
                sand_y += 1
                sand_x += 1
            else:
                rocks.add((sand_x, sand_y))
                sand_drawing.add((sand_x, sand_y))
                count += 1
                break

    draw(rocks, sand_drawing, True)

    print(part1)
    print(count)
