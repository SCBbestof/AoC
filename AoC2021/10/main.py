matches = {'[': ']', '{': '}', '<': '>', '(': ')'}
costs = {']': 57, ')': 3, '}': 1197, '>': 25137}
costs2 = {']': 2, ')': 1, '}': 3, '>': 4}

with open("data.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    cost = 0
    cost2 = []
    for line in lines:
        stack = []
        valid = True
        for char in line:
            if char in matches.keys():
                stack.append(char)
            else:
                popped = stack.pop()
                for k, v in matches.items():
                    if popped == k and char != v:
                        cost += costs[char]
                        valid = False
                        break
                if not valid:
                    break
        # Part 2
        if valid:
            c = 0
            for char in reversed(stack):
                c *= 5
                c += costs2[matches[char]]
            cost2.append(c)

    print("1: " + str(cost))
    print("2: " + str(sorted(cost2)[len(cost2)//2]))

