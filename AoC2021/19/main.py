import itertools


with open("data.in") as file:
    lines = file.read().strip().split('\n\n')

    scanners = []
    for line in lines:
        coords = []
        for ln in line.splitlines()[1:]:
            split_coords = ln.split(',')
            coord = (int(split_coords[0]), int(split_coords[1]), int(split_coords[2]))
            coords.append(coord)
        scanners.append(coords)

    matched = [False for scanner in scanners]
    matched[0] = True
    stack = [scanners[0]]
    part2_diffs = []
    while len(stack) > 0:
        first_scanner = stack.pop()
        for i, scanner in enumerate(scanners):
            if not matched[i]:
                possible_orientations = []
                for dir in itertools.product([1, -1], repeat=3):
                    for perm in itertools.permutations([0, 1, 2]):
                        coords_entry = []
                        for coord in scanner:
                            new_coords = (dir[0] * coord[perm[0]], dir[1] * coord[perm[1]], dir[2] * coord[perm[2]])
                            coords_entry.append(new_coords)
                        # print(coords_entry, perm, dir)
                        possible_orientations.append(coords_entry)
                # print(len(possible_orientations))
                # exit(0)
                for orientations in possible_orientations:
                    for scan in first_scanner:
                        for orientation in orientations:
                            diffs = (orientation[0] - scan[0], orientation[1] - scan[1], orientation[2] - scan[2])
                            translations = []
                            for o in orientations:
                                translations.append((o[0] - diffs[0], o[1] - diffs[1], o[2] - diffs[2]))
                            # print(translations)
                            if len(set(translations).intersection(set(first_scanner))) >= 12:
                                # print('Matched', diffs)
                                part2_diffs.append(diffs)
                                stack.append(scanners[i])
                                scanner[:] = translations
                                matched[i] = True
                                break
                        if matched[i]:
                            break

    beacons = set()
    for scanner in scanners:
        for scan in scanner:
            beacons.add(scan)
    print("1:", len(beacons))

    max_distance = 0
    for i, coord1 in enumerate(part2_diffs):
        for j in range(i + 1, len(part2_diffs)):
            distance = sum(abs(c1 - c2) for c1, c2 in zip(coord1, part2_diffs[j]))
            if max_distance < distance:
                max_distance = distance
    print("2:", max_distance)
