with open("data.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    # Worst practices in action <3
    h = 0
    d = 0
    aim = 0
    for line in lines:
        a, b = line.split()
        b = int(b)
        # print(a, b)

        if a == "forward":
            h = h + b
            d = d + aim * b
        if a == "up":
            aim = aim - b
        if a == "down":
            aim = aim + b

    print(h * d)
