import collections.abc
import json
import math
import re


def split(str_arr):
    numbers = re.findall(r'\d+', str_arr)
    was_split = False
    for n in numbers:
        int_n = int(n)
        if int_n > 9:
            was_split = True
            str_arr = str_arr.replace(n, '[' + str(math.floor(int_n / 2)) + ', ' + str(math.ceil(int_n / 2)) + ']')
    return was_split, str_arr


def explode(str_arr):
    exploded = False
    brackets = 0
    for i in range(len(str_arr)):
        if not str_arr[i].isnumeric():
            if str_arr[i] == '[':
                brackets += 1
                if brackets > 4:
                    # print('str?', str_arr[i:i + 5])
                    if str_arr[i + 1].isnumeric() and str_arr[i + 2] == ',' and str_arr[i + 3] == ' ' and str_arr[
                        i + 4].isnumeric() and str_arr[i + 5] == ']':
                        # print("before: ", str_arr)
                        first_half = list(str_arr[:i])
                        for j in range(i, 0, -1):
                            if str_arr[j].isnumeric():
                                first_half[j] = str(int(int(str_arr[j]) + int(str_arr[i + 1])))
                                break

                        second_half = list(str_arr[i + 5:])
                        for j in range(len(second_half)):  # i+5 because arrOutOfBounds
                            if str_arr[i + 5 + j].isnumeric():
                                second_half[j] = str(int(int(str_arr[i + 5 + j]) + int(str_arr[i + 4])))
                                break
                        lst = first_half + second_half
                        str_arr = ''.join(lst)
                        # print("after : ", str_arr)
                        str_arr = str_arr.replace(' ]', ' 0')
                        str_arr = str_arr.replace(', [],', ', [0,')
                        str_arr = str_arr.replace('[], ', '[0, ')
                        # print("after : ", str_arr)
                        exploded = True
                        break
            elif str_arr[i] == ']':
                brackets -= 1
    return exploded, str_arr


def magnitude(arr):
    if isinstance(arr, list):
        return 3 * magnitude(arr[0]) + 2 * magnitude(arr[1])
    else:
        return arr


with open("data.in") as file:
    lines = file.read().strip().splitlines()

    arrs = []
    for line in lines:
        arrs.append(json.loads(line))
    print(arrs)
    print()
    arrLen = len(arrs)
    i = 0
    str_arr = None
    part1mag = None
    while arrLen > 1:
        str_arr = str([arrs[i], arrs[i + 1]])
        exploded = True
        was_split = True
        while exploded or was_split:
            exploded, str_arr = explode(str_arr)
            was_split, str_arr = split(str_arr)
            # print(exploded, was_split)
            # print("after_split:", str_arr)
        # dst = json.loads(str_arr)
        arrs[i] = json.loads(str_arr)
        arrs.remove(arrs[i + 1])
        arrLen -= 1
        # print()
        # print("str_arr", str_arr)

    part1mag = magnitude(arrs[i])

    arrs = []
    for line in lines:
        arrs.append(json.loads(line))
    magnitudes = []
    for a in arrs:
        for b in arrs:
            if a != b:
                str_arr = str([a, b])
                exploded = True
                was_split = True
                while exploded or was_split:
                    exploded, str_arr = explode(str_arr)
                    was_split, str_arr = split(str_arr)
                magnitudes.append(magnitude(json.loads(str_arr)))
    print("1: " + str(part1mag))
    print("2: " + str(max(magnitudes)))
