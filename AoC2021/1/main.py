with open("data.in") as file:
    lines = file.readlines()
    lines = [int(line.rstrip()) for line in lines]

    # Worst practices in action <3
    prev1 = 99999
    prev2 = 99999
    prev3 = 99999
    count = 0
    for line in lines:
        if line + prev1 + prev2 > prev1 + prev2 + prev3:
            count = count + 1
        prev3 = prev2
        prev2 = prev1
        prev1 = line
    print(count)
