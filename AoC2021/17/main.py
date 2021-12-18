with open("data.in") as file:
    lines = file.read().strip()
    lines = lines.split(": ")[1]
    print(lines)
    x = lines.split(", ")[0].split("=")[1]
    y = lines.split(", ")[1].split("=")[1]
    print(x)
    print(y)
    x1 = int(x.split("..")[0])
    x2 = int(x.split("..")[1])
    print(x1, x2)
    y1 = int(y.split("..")[0])
    y2 = int(y.split("..")[1])
    print(y1, y2)
    print()

    highest_y = 0
    count = 0
    ys_found = []
    for new_y in range(-500, 500):
        start_y = new_y
        current_y = 0
        max_y = 0

        found = False
        steps = []
        for step in range(500):
            current_y += new_y
            new_y -= 1
            max_y = max(current_y, max_y)
            if current_y < y1:
                break
            if y1 <= current_y <= y2:
                found = True
                steps.append(step)
        if found:
            count += 1
            ys_found.append((start_y, steps))
            highest_y = max(highest_y, max_y)

    print("1: " + str(highest_y))

    xs_found = []
    for new_x in range(500):
        start_x = new_x
        current_x = 0
        max_x = 0

        found = False
        steps = []
        for step in range(500):
            current_x += new_x
            if new_x:
                new_x -= 1
            max_x = max(current_x, max_x)
            if current_x > x2:
                break
            if x1 <= current_x <= x2:
                found = True
                steps.append(step)
        if found:
            count += 1
            xs_found.append((start_x, steps))

    final_count = 0
    for x, steps_x in xs_found:
        for y, steps_y in ys_found:
            if set(steps_x).intersection(set(steps_y)):
                # print(x, y)
                final_count += 1

    print("2: " + str(final_count))
