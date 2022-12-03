from collections import Counter

with open("data.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    count = 0
    for line in lines:
        firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
        counterFirst = Counter(firstpart)
        counterSecond = Counter(secondpart)
        intersect = []
        for item in counterFirst.keys():
            if item in counterSecond.keys():
                intersect.append(item)
        print(intersect)
        for element in intersect:
            if element.islower():
                count += ord(element) - 96
            else:
                count += ord(element) - 64 + 26

    print(count)
    print()
    print()
    print("PART TWO")
    print()
    print()

    count = 0
    lineCount = 0
    for lineCount in range(0, len(lines), 3):
        print(lineCount)
        print(lines[lineCount])
        print(lines[lineCount+1])
        print(lines[lineCount+2])
        counterFirst = Counter(lines[lineCount])
        counterSecond = Counter(lines[lineCount+1])
        counterThird = Counter(lines[lineCount+2])
        intersect = []
        for item in counterFirst.keys():
            if item in counterSecond.keys() and item in counterThird.keys():
                intersect.append(item)
        print(intersect)
        for element in intersect:
            if element.islower():
                count += ord(element) - 96
            else:
                count += ord(element) - 64 + 26

    print(count)