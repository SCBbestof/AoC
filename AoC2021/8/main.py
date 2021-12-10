import itertools

digits = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9,
}

with open("data.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    firstHalf = []
    secondHalf = []
    for line in lines:
        firstHalf.append(line.split(" | ")[0])
        secondHalf.append(line.split(" | ")[1])
    count = 0
    for item in secondHalf:
        for subitem in item.split(" "):
            if len(subitem) == 2 or len(subitem) == 3 or len(subitem) == 4 or len(subitem) == 7:
                count += 1
    print("1: " + str(count))

    sum = 0
    for i in range(len(lines)):
        for permutation in itertools.permutations("abcdefg"):
            permutations_map = {'a': permutation[0], 'b': permutation[1], 'c': permutation[2], 'd': permutation[3],
                                'e': permutation[4], 'f': permutation[5], 'g': permutation[6]}

            found = True

            for word in firstHalf[i].split():
                lst = []
                for element in word:
                    lst.append(permutations_map[element])

                lst = sorted(lst)
                new_word = ""
                for item in lst:
                    new_word += item
                if new_word not in digits.keys():
                    found = False
                    break

            if found:
                digits_found = ""
                for word in secondHalf[i].split():
                    lst = []
                    for element in word:
                        lst.append(permutations_map[element])

                    lst = sorted(lst)
                    new_word = ""
                    for item in lst:
                        new_word += item

                    digits_found += str(digits[new_word])

                sum += int(digits_found)
                break
    print("2: " + str(sum))
