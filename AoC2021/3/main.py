from collections import Counter

with open("data.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    # Worst practices in action <3
    theta = ''
    epsilon = ''
    for i in range(0, len(lines[0])):
        common = Counter([line[i] for line in lines])
        if common['0'] > common['1']:
            theta = theta + '0'
            epsilon = epsilon + '1'
        else:
            theta = theta + '1'
            epsilon = epsilon + '0'

    print("1: " + str(int(theta, 2) * int(epsilon, 2)))

    for i in range(len(lines[0])):
        common = Counter([line[i] for line in lines])

        if common['0'] > common['1']:
            lines = [line for line in lines if line[i] == '0']
        else:
            lines = [line for line in lines if line[i] == '1']
        theta = lines[0]

    file.seek(0)
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    for i in range(len(lines[0])):
        common = Counter([line[i] for line in lines])

        if common['0'] > common['1']:
            lines = [line for line in lines if line[i] == '1']
        else:
            lines = [line for line in lines if line[i] == '0']
        if lines:
            epsilon = lines[0]
    print("2: " + str(int(theta, 2) * int(epsilon, 2)))
