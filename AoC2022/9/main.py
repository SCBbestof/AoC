def is_touching(head, tail):
    return \
       (head[0] + 1 == tail[0] and head[1] + 1 == tail[1]) or \
       (head[0] - 1 == tail[0] and head[1] - 1 == tail[1]) or \
       (head[0] - 1 == tail[0] and head[1] + 1 == tail[1]) or \
       (head[0] + 1 == tail[0] and head[1] - 1 == tail[1]) or \
       (head[0] + 1 == tail[0] and head[1] == tail[1]) or \
       (head[0] - 1 == tail[0] and head[1] == tail[1]) or \
       (head[1] + 1 == tail[1] and head[0] == tail[0]) or \
       (head[1] - 1 == tail[1] and head[0] == tail[0]) or \
       (head == tail)


with open("data.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    head_pos = [0, 0]
    tail_pos = [-1, 0]
    # tail_pos_postions = set(tuple())
    tail_pos_postions = []

    for line in lines:
        direction, count = line.split()
        count = int(count)
        # print(direction, count)
        for i in range(count):
            if direction == 'D':
                head_pos[1] -= 1
                if not is_touching(head_pos, tail_pos) and head_pos[1] != tail_pos[1]:
                    tail_pos[0] = head_pos[0]
                    tail_pos[1] = head_pos[1] + 1
            elif direction == 'U':
                head_pos[1] += 1
                if not is_touching(head_pos, tail_pos) and head_pos[1] != tail_pos[1]:
                    tail_pos[0] = head_pos[0]
                    tail_pos[1] = head_pos[1] - 1
            elif direction == 'L':
                head_pos[0] -= 1
                if not is_touching(head_pos, tail_pos) and head_pos[0] != tail_pos[0]:
                    tail_pos[1] = head_pos[1]
                    tail_pos[0] = head_pos[0] + 1
            else:  # R
                head_pos[0] += 1
                if not is_touching(head_pos, tail_pos) and head_pos[0] != tail_pos[0]:
                    tail_pos[1] = head_pos[1]
                    tail_pos[0] = head_pos[0] - 1

            if not (tail_pos[0], tail_pos[1]) in tail_pos_postions:
                tail_pos_postions.append((tail_pos[0], tail_pos[1]))
            # print(tail_pos_postions)

    print(tail_pos_postions)
    print(len(tail_pos_postions))

    print()
    print("PART 2")
    print()

    rope = [[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0]]

    print(rope)
    # tail_pos_postions = set(tuple())
    tail_pos_postions = []

    for line in lines:
        direction, count = line.split()
        count = int(count)
        # print(direction, count)
        for _ in range(count):
            for i in range(1, 10):
                head_pos = rope[i-1]
                tail_pos = rope[i]
                if i == 1:
                    if direction == 'D':
                        head_pos[1] -= 1
                    elif direction == 'U':
                        head_pos[1] += 1
                    elif direction == 'L':
                        head_pos[0] -= 1
                    else:  # R
                        head_pos[0] += 1
                if not is_touching(head_pos, tail_pos):
                    if head_pos[0] == tail_pos[0]:
                        if head_pos[1] > tail_pos[1]:
                            tail_pos[1] += 1
                        else:
                            tail_pos[1] -= 1
                    elif head_pos[1] == tail_pos[1]:
                        if head_pos[0] > tail_pos[0]:
                            tail_pos[0] += 1
                        else:
                            tail_pos[0] -= 1
                    else:
                        if head_pos[0] < tail_pos[0] and head_pos[1] > tail_pos[1]:
                            tail_pos[0] -= 1
                            tail_pos[1] += 1
                        elif head_pos[0] < tail_pos[0] and head_pos[1] < tail_pos[1]:
                            tail_pos[0] -= 1
                            tail_pos[1] -= 1
                        elif head_pos[0] > tail_pos[0] and head_pos[1] > tail_pos[1]:
                            tail_pos[0] += 1
                            tail_pos[1] += 1
                        else:
                            tail_pos[0] += 1
                            tail_pos[1] -= 1

                rope[i-1] = head_pos
                rope[i] = tail_pos
                if not (rope[-1][0], rope[-1][1]) in tail_pos_postions:
                    tail_pos_postions.append((rope[-1][0], rope[-1][1]))
                # print(head_pos, tail_pos, rope[i-1], rope[i], i)
            # print(rope)
            if not (rope[-1][0], rope[-1][1]) in tail_pos_postions:
                tail_pos_postions.append((rope[-1][0], rope[-1][1]))
                # print(tail_pos_postions)

    # print(tail_pos_postions)
    print(len(tail_pos_postions))
