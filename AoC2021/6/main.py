with open("data.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    lines = lines[0].split(",")

    arr = []
    for ln in lines:
        arr.append(int(ln))

    for i in range(80):
        for j in range(0, len(arr)):
            if arr[j] <= 0:
                arr[j] = 6
                arr.append(8)
            else:
                arr[j] -= 1

    print("1: " + str(len(arr)))

    file.seek(0)
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    lines = lines[0].split(",")
    lines = list(map(int, lines))

    fish = [lines.count(i) for i in range(9)]

    for i in range(256):
        num = fish.pop(0)
        fish[6] += num
        fish.append(num)

    print("2: " + str(sum(fish)))