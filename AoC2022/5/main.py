with open("data.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    lStacks = [['D','T','W','N','L'],
               ['H','P','C'],
               ['J','M','G','D','N','H','P','W'],
               ['L','Q','T','N','S','W','C'],
               ['N','C','H','P'],
               ['B','Q','W','M','D','N','H','T'],
               ['L','S','G','J','R','B','M'],
               ['T','R','B','V','G','W','N','Z'],
               ['L','P','N','D','G','W']]
    # DEMO
    # lStacks = [['N','Z'],['D','C','M'],['P']]
    # for line in lines[5:]:
    for line in lines[10:]:
        line = line.split("move ")[1]
        amount, line = line.split(" from ")
        amount = int(amount)
        source, to = line.split(" to ")
        source = int(source) - 1
        to = int(to) - 1
        # PART 1
        # for i in range(amount):
        #     lStacks[to].insert(0, lStacks[source].pop(0))

        # PART 2
        for i in range(amount, 0, -1):
            lStacks[to].insert(0, lStacks[source].pop(i - 1))

    for stack in lStacks:
        print(stack[0])
