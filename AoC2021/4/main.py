from collections import Counter

with open("data.in") as file:
    lines = file.readlines()

    numbers = [int(nr) for nr in lines[0].split(",")]
    boards = []

    for board_index in range(2, len(lines), 6):
        board = []
        for i in range(5):
            board.append([int(nr) for nr in lines[board_index + i].split(" ") if nr != ""])
        boards.append(board)

    board_hits = [[[False for _ in range(5)] for _ in range(5)] for board in boards]
    board_finished = [False for board in boards]

    for number in numbers:
        for index, board in enumerate(boards):
            for i in range(5):
                for j in range(5):
                    if board[i][j] == number:
                        board_hits[index][i][j] = True
        for index, boards_hit in enumerate(board_hits):
            if board_finished[index]:
                continue
            finished = False
            for row in range(5):
                counter_row = Counter(boards_hit[row])
                if counter_row[True] == 5:
                    finished = True
            for col in range(5):
                count = 0
                for row in range(5):
                    if boards_hit[row][col]:
                        count = count + 1
                if count == 5:
                    finished = True
            if finished:
                hit_sum = 0
                for i in range(5):
                    for j in range(5):
                        if not boards_hit[i][j]:
                            hit_sum += boards[index][i][j]
                print(hit_sum * number)
                board_finished[index] = True
