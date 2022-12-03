from collections import Counter

with open("data.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    count = 0
    for line in lines:
        first_part, second_part = line[:len(line) // 2], line[len(line) // 2:]
        counter_first = Counter(first_part)
        counter_second = Counter(second_part)
        intersect = []
        for item in counter_first.keys():
            if item in counter_second.keys():
                intersect.append(item)
        for element in intersect:
            if element.islower():
                count += ord(element) - 96
            else:
                count += ord(element) - 38

    print(count)

    count = 0
    for lineCount in range(0, len(lines), 3):
        counter_first = Counter(lines[lineCount])
        counter_second = Counter(lines[lineCount + 1])
        counter_third = Counter(lines[lineCount + 2])
        intersect = []
        for item in counter_first.keys():
            if item in counter_second.keys() and item in counter_third.keys():
                intersect.append(item)
        for element in intersect:
            if element.islower():
                count += ord(element) - 96
            else:
                count += ord(element) - 38

    print(count)