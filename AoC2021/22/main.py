def intersect(coord_min, coord_max, reactor_coord_min, reactor_coord_max):
    if reactor_coord_min <= coord_min < reactor_coord_max:
        return coord_min, min(coord_max, reactor_coord_max)
    if reactor_coord_min < coord_max <= reactor_coord_max:
        return max(reactor_coord_min, coord_min), coord_max
    if coord_min <= reactor_coord_max < coord_max:
        return reactor_coord_min, min(coord_max, reactor_coord_max)
    if coord_min < reactor_coord_max <= coord_max:
        return max(coord_min, reactor_coord_min), reactor_coord_max
    return None, None


def intersect_reactors(reactor1, reactor2):
    x1, x2 = intersect(reactor1[0][0], reactor1[0][1], reactor2[0][0], reactor2[0][1])
    y1, y2 = intersect(reactor1[1][0], reactor1[1][1], reactor2[1][0], reactor2[1][1])
    z1, z2 = intersect(reactor1[2][0], reactor1[2][1], reactor2[2][0], reactor2[2][1])
    if (None, None) not in [(x1, x2), (y1, y2), (z1, z2)]:
        return True, ((x1, x2), (y1, y2), (z1, z2))
    else:
        return False, ((x1, x2), (y1, y2), (z1, z2))


def process_intersection(reactor, intersection):
    list_x = [reactor[0][0], reactor[0][1], intersection[0][0], intersection[0][1]]
    list_y = [reactor[1][0], reactor[1][1], intersection[1][0], intersection[1][1]]
    list_z = [reactor[2][0], reactor[2][1], intersection[2][0], intersection[2][1]]
    list_x = sorted(list(set(list_x)))
    list_y = sorted(list(set(list_y)))
    list_z = sorted(list(set(list_z)))

    processed = set()
    for i in range(len(list_x) - 1):
        for j in range(len(list_y) - 1):
            for k in range(len(list_z) - 1):
                processed.add(((list_x[i], list_x[i+1]), (list_y[j], list_y[j+1]), (list_z[k], list_z[k+1])))
    processed.remove((intersection[0], intersection[1], intersection[2]))
    return processed


with open("data.in") as file:
    lines = file.read().strip().splitlines()

    coords_arr = []
    for line in lines:
        first_split = line.split(' ')
        status = first_split[0]
        line = first_split[1]

        coords = [status]
        for l in line.split(','):
            l1 = l[2:]
            inner_split = l1.split('..')
            coord_min = int(inner_split[0])
            coord_max = int(inner_split[1])
            coords.append((coord_min, coord_max))
        coords_arr.append(coords)
    # print(coords_arr)

    online_reactors = set()
    for coords in coords_arr:
        status = coords[0]
        min_x = max(coords[1][0], -100)
        min_y = max(coords[2][0], -100)
        min_z = max(coords[3][0], -100)
        max_x = min(coords[1][1], 100)
        max_y = min(coords[2][1], 100)
        max_z = min(coords[3][1], 100)
        # print(status, min_x, max_x, min_y, max_y, min_z,max_z, coords[2])
        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                for z in range(min_z, max_z + 1):
                    if status == 'on':
                        online_reactors.add((x, y, z))
                    elif (x, y, z) in online_reactors:
                        online_reactors.remove((x, y, z))

    print('1:', len(online_reactors))

    online_reactors = set()
    for coords in coords_arr:
        status = coords[0]
        min_x = coords[1][0]
        min_y = coords[2][0]
        min_z = coords[3][0]
        max_x = coords[1][1]
        max_y = coords[2][1]
        max_z = coords[3][1]
        cur_reactor = tuple(coords[1:])
        if online_reactors:
            next_online = set()
            for reactor in online_reactors:
                intersected, intersection = intersect_reactors(cur_reactor, reactor)
                if intersected:
                    next_online = next_online.union(process_intersection(reactor, intersection))
                else:
                    next_online.add(reactor)
                if status == 'on':
                    next_online.add(cur_reactor)
            online_reactors = next_online
        elif status == 'on':
            online_reactors.add(cur_reactor)
    # print("2", online_reactors)
    # print(len(online_reactors))

    online_reactors_count = 0
    for reactor in online_reactors:
        online_reactors_count += (reactor[0][1] - reactor[0][0]) * \
                                 (reactor[1][1] - reactor[1][0]) * \
                                 (reactor[2][1] - reactor[2][0])

    print("2:", online_reactors_count)
