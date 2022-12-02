with open("data.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    count = 0
    for line in lines:
        opt1 = line.split(" ")[0]
        opt2 = line.split(" ")[1]
        if opt2 == 'X':
            count += 1
            if opt1 == 'A':
                count += 3
            if opt1 == 'C':
                count += 6
        elif opt2 == 'Y':
            count += 2
            if opt1 == 'A':
                count += 6
            if opt1 == 'B':
                count += 3
        else:
            count += 3
            if opt1 == 'B':
                count += 6
            if opt1 == 'C':
                count += 3

    print(count)

    count = 0
    for line in lines:
        opt1 = line.split(" ")[0]
        opt2 = line.split(" ")[1]
        if opt2 == 'X':
            if opt1 == 'A':
                count += 3
            if opt1 == 'B':
                count += 1
            if opt1 == 'C':
                count += 2
        elif opt2 == 'Y':
            count += 3
            if opt1 == 'A':
                count += 1
            if opt1 == 'B':
                count += 2
            if opt1 == 'C':
                count += 3
        else:
            count += 6
            if opt1 == 'A':
                count += 2
            if opt1 == 'B':
                count += 3
            if opt1 == 'C':
                count += 1

    print(count)