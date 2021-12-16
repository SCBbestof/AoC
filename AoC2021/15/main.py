import collections
import sys


# https://en.wikipedia.org/wiki/Dijkstra's_algorithm#Pseudocode
# Could have been done with heap queues, to not waste 40 minutes running it, but it is what it is :)
def dijkstra():
    global target, distances, i, j
    target = (len(board) - 1, len(board[0]) - 1)
    vertices = set()
    previous = collections.defaultdict(int)
    distances = collections.defaultdict(int)
    for i in range(len(board)):
        for j in range(len(board[0])):
            distances[(i, j)] = sys.maxsize
            previous[(i, j)] = None
            vertices.add((i, j))

    distances[start_pos] = 0
    while len(vertices) > 0:
        print(len(vertices))
        minim = sys.maxsize
        u = None
        for vertex, distance in distances.items():
            if distance < minim and vertex in vertices:
                u = vertex
                minim = distance

        vertices.remove(u)

        neighbours = [(u[0] - 1, u[1]), (u[0] + 1, u[1]), (u[0], u[1] - 1), (u[0], u[1] + 1)]
        for vertex in neighbours:
            if vertex in vertices:
                alt = distances[u] + board[vertex[0]][vertex[1]]
                if alt < distances[vertex]:
                    distances[vertex] = alt
                    previous[vertex] = u


with open("data.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    # lowest path --> Dijkstra?

    board = [[0 for _ in range(len(lines[0]))] for _ in range(len(lines))]
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            board[i][j] = int(lines[i][j])

    start_pos = (0, 0)
    dijkstra()

    # print(distances)
    # print(previous)
    print("1: " + str(distances[target[0], target[1]]))

    # PART 2
    print(len(board))
    print(len(lines))
    board = [[0 for _ in range(488)] for _ in range(488)]
    for row_count in range(5):
        for col_count in range(5):
            for i in range(len(lines)):
                for j in range(len(lines[i])):
                    board[i + (len(lines) - row_count + 1) * row_count][
                        j + (len(lines[i]) - col_count + 1) * col_count] = (int(
                        lines[i][j]) + row_count + col_count) % 10

    print(target)
    target = (len(board) - 1, len(board[0]) - 1)
    # target = (487, 487)
    print(target)
    print(board[100][105])
    print(board[100][100])
    print(board[101][101])
    print(board[target[0]][target[1]])

    start_pos = (0, 0)
    dijkstra()
    print("2: " + str(distances[target[0], target[1]]))
    # print("2: " + str(minimum_path(487, 487, seen)))
