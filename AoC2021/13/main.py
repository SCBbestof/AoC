def fold(dir, value, coords):
    folded_coords = set()
    for coord in coords:
        if dir == 'x':
            if coord[0] < value:
                folded_coords.add((coord[0], coord[1]))
            else:
                folded_coords.add((value - (coord[0] - value), coord[1]))
        else:
            if coord[1] < value:
                folded_coords.add((coord[0], coord[1]))
            else:
                folded_coords.add((coord[0], value - (coord[1] - value)))
    return folded_coords


with open("data.in") as file:
    lines = file.read().strip()

    first_part, second_part = lines.split('\n\n')

    coords = set()
    for line in first_part.splitlines():
        x, y = line.split(',')
        x = int(x)
        y = int(y)
        coords.add((x, y))

    print("Part 1")

    for instructions in second_part.splitlines():
        axis, value = instructions.split('=')
        coords = fold(axis[-1], int(value), coords)

        print((len(coords)))

    print("\nPart 2")

    x, y = zip(*coords)
    for row in range(max(y) + 1):
        draw_row = []
        for col in range(max(x) + 1):
            if (col, row) in coords:
                draw_row.append('#')
            else:
                draw_row.append(' ')
        print(draw_row)
