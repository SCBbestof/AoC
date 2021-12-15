import collections
import time

start_time = time.time()
processed = {}


def part2(key, step_nr):
    final = collections.defaultdict(int)
    if step_nr == 0:
        for ch in key:
            final[ch] += 1
        return final

    processed_key = (key, step_nr)
    if processed_key in processed:
        return processed[processed_key]

    mid = insertions[key]
    final1 = part2(key[0] + mid, step_nr - 1)
    final2 = part2(mid + key[1], step_nr - 1)

    for ch, idx in final1.items():
        final[ch] += idx
    for ch, idx in final2.items():
        final[ch] += idx
    final[mid] -= 1

    processed[processed_key] = final
    return final


with open("data.in") as file:
    lines = file.read().strip()
    poly, insertion = lines.split('\n\n')

    insertions = {}
    for line in insertion.splitlines():
        a, b = line.split(' -> ')
        insertions[a] = b

    for step in range(10):
        new = ''
        for i in range(len(poly) - 1):
            key = poly[i:i+2]
            new = new + poly[i] + insertions[key]
        poly = new + poly[-1]

    counter = collections.Counter(poly)
    print("1: " + str(max(counter.values()) - min(counter.values())))

    poly, _ = lines.split('\n\n')
    counter = collections.Counter()
    for i in range(len(poly) - 1):
        key = poly[i:i+2]
        count = part2(key, 40)
        counter = counter + collections.Counter(count)

    print("2: " + str(max(counter.values()) - min(counter.values()) - 1))

print("--- %s seconds ---" % (time.time() - start_time))