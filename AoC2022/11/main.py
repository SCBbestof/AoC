with open("data.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    monkeys = {}
    current_monkey = []
    monkeyCounter = -1
    for line in lines:
        split = line.split()
        if len(split) == 0:
            monkeys[current_monkey[0]] = current_monkey[1:]
            current_monkey = []
            continue
        # print(split)
        if split[0].startswith("Monkey"):
            monkeyCounter += 1
            current_monkey.append(monkeyCounter)
        elif split[0].startswith("Starting"):
            items = []
            for i in range(2, len(split)):
                items.append(int(split[i].replace(",", "")))
            current_monkey.append(items)
        elif split[0].startswith("Operation"):
            op = split[4]
            if split[5] != "old":
                value = int(split[5])
            else:
                value = -1
            current_monkey.append([op, value])
        elif split[0].startswith("Test"):
            divisible_by = int(split[3])
            current_monkey.append(divisible_by)
        elif len(split) > 1:
            if split[1].startswith("true"):
                throw_to_true = int(split[5])
                current_monkey.append(throw_to_true)
            elif split[1].startswith("false"):
                throw_to_false = int(split[5])
                current_monkey.append(throw_to_false)

    monkeys[current_monkey[0]] = current_monkey[1:]
    inspections = [0] * len(monkeys)

    div = 1
    for m in monkeys:
        print(m, monkeys[m])
        div *= monkeys[m][2]

    # part 1
    # for i in range(20):
    for i in range(10000):
        # print(i)
        for monkey in monkeys:
            current_monkey = monkeys[monkey]
            while len(current_monkey[0]) > 0:
                worry = current_monkey[0].pop()
                if current_monkey[1][0] == "*":
                    if current_monkey[1][1] == -1:
                        worry *= worry
                    else:
                        worry *= current_monkey[1][1]
                else:  # +
                    if current_monkey[1][1] == -1:
                        worry += worry
                    else:
                        worry += current_monkey[1][1]

                # part 1
                # worry = worry // 3
                worry = worry % div

                if worry % current_monkey[2] == 0:
                    monkeys[current_monkey[3]][0].append(worry)
                else:
                    monkeys[current_monkey[4]][0].append(worry)
                inspections[monkey] += 1

    inspections.sort()
    print(inspections)
    print(inspections[-1] * inspections[-2])
