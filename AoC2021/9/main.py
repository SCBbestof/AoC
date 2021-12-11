with open("data.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    board = [[0 for _ in range(len(lines[0]))] for _ in range(len(lines))]

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            board[i][j] = int(lines[i][j])

    sum = 0
    counts = 0
    mins = []
    basins = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            dir = []
            for row in range(i - 1, i + 2):
                for col in range(j - 1, j + 2):
                    if i == row and j == col:
                        continue
                    if (row == i or col == j) and 0 <= row < len(board) and 0 <= col < len(board[0]):
                        dir.append(board[row][col])

            if board[i][j] < min(dir):
                mins.append(board[i][j])

                # Part 2
                basin = [(i, j)]  # Because dumb sets can't be changed while looped over and don't keep insertion order
                for tp in basin:
                    for row in range(tp[0] - 1, tp[0] + 2):
                        for col in range(tp[1] - 1, tp[1] + 2):
                            if (row, col) in basin:
                                continue
                            if (row == tp[0] or col == tp[1]) and 0 <= row < len(board) and 0 <= col < len(board[0]) \
                                    and board[row][col] < 9:
                                basin.append((row, col))
                basins.append(len(basin))

    for min in mins:
        sum += min
        counts += 1

    sum += counts
    print("1: " + str(sum))
    basins.sort()
    basins.reverse()
    print("2: " + str(basins[0] * basins[1] * basins[2]))
