from collections import Counter

with open("data.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    count = 0
    count2 = 0
    for line in lines:
        first, second = line.split(",")
        first1, first2 = first.split("-")
        second1, second2 = second.split("-")
        first1 = int(first1)
        first2 = int(first2)
        second1 = int(second1)
        second2 = int(second2)
        if (first1 <= second1 and first2 >= second2) or (second1 <= first1 and second2 >= first2):
            count += 1

        if (first2 >= second1 >= first1) or (second2 >= first1 >= second1):
            count2 += 1

    print(count)
    print(count2)
