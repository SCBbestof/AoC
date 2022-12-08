with open("data.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    map = []
    visibility_map = []
    score = []

    for line in lines:
        line_map = []
        visibility_row = []

        for ch in line:
            val = int(ch)
            if len(line_map) > 0 and len(map) > 0 and max(line_map) >= val:
                visibility_row.append(False)
            else:
                visibility_row.append(True)
            line_map.append(val)

        visibility_row[len(visibility_row) - 1] = True
        for i in range(len(line_map) - 1):
            if line_map[i] > max(line_map[i+1:]):
                visibility_row[i] = True

        map.append(line_map)
        visibility_map.append(visibility_row)

    visibility_map[len(visibility_map) - 1] = [True]*len(visibility_map[0])

    for i in range(len(map)):
        for j in range(len(map[i])):
            max_val = 0
            for k in range(i):
                if map[k][j] > max_val:
                    max_val = map[k][j]
            if max_val < map[i][j]:
                visibility_map[i][j] = True
                continue
            max_val = 0
            for k in range(i+1, len(map)):
                if map[k][j] > max_val:
                    max_val = map[k][j]
            if max_val < map[i][j]:
                visibility_map[i][j] = True

    max_score = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            x = i
            score_down = 0
            while x > 0:
                x -= 1
                score_down += 1
                if map[i][j] <= map[x][j]:
                    break

            x = i
            score_up = 0
            while x < len(map) - 1:
                x += 1
                score_up += 1
                if map[i][j] <= map[x][j]:
                    break

            y = j
            score_left = 0
            while y > 0:
                y -= 1
                score_left += 1
                if map[i][j] <= map[i][y]:
                    break

            y = j
            score_right = 0
            while y < len(map[0]) - 1:
                y += 1
                score_right += 1
                if map[i][j] <= map[i][y]:
                    break

            score = score_down * score_up * score_left * score_right
            if score > max_score:
                max_score = score

    count = 0
    for line in visibility_map:
        for el in line:
            if el:
                count += 1

    print(count)
    print(max_score)
