import math
from queue import PriorityQueue


def get_neighbors(node, grid):
    x, y = node
    current = grid[x][y]
    neighbors = []
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if 0 <= x + dx <= len(grid) - 1 and 0 <= y + dy <= len(grid[0]) - 1:
            if 1 >= grid[x + dx][y + dy] - current:
                neighbors.append((x + dx, y + dy))
    return neighbors


def find_path_ucs(start, end, grid):
    queue = PriorityQueue()
    queue.put((0, start))

    distances = {start: 0}

    while not queue.empty():
        path_len, node = queue.get()
        if node == end:
            return distances[node]

        adj_nodes = get_neighbors(node, grid)
        for adj_node in adj_nodes:
            if adj_node not in distances:
                distances[adj_node] = math.inf
            if distances[node] + 1 < distances[adj_node]:
                queue.put((path_len + 1, adj_node))
                distances[adj_node] = path_len + 1

    return math.inf


with open("data.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    grid = []
    start = None
    end = None
    for line in lines:
        line_list = []
        count = 0
        for ch in line:
            ascii_val = ord(ch) - 97
            if ascii_val == -14:
                ascii_val = -1
                start = (lines.index(line), count)
            if ascii_val == -28:
                ascii_val = 26
                end = (lines.index(line), count)
            line_list.append(ascii_val)
            count += 1

        grid.append(line_list)

    # print(start, end)
    # print(get_neighbors(start, grid))
    print(find_path_ucs(start, end, grid))

    paths = []
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 0:
                paths.append(find_path_ucs((x, y), end, grid))

    print(min(paths))
