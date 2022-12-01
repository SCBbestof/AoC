with open("data.in") as file:
    lines = file.readlines()
    # lines = [int(line.rstrip()) for line in lines]

    sumList = []
    sum = 0
    for line in lines:
        if line == "\n":
            sumList.append(sum)
            sum = 0
        else:
            sum = sum + int(line.rstrip())

    print(max(sumList))

    sumList = sorted(sumList)
    print(sumList[-1] + sumList[-2] + sumList[-3])