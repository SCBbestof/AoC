from collections import Counter

def isUniqueChars(string):
    freq = Counter(string)

    return len(freq) == len(string)


with open("data.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    line = lines[0]
    visited = set()
    marker = False
    count = 0
    for i in range(len(line)):
        print(line[i:i+14])
        if isUniqueChars(line[i:i+14]):
            print(i+14)
            break