with open("data.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    registry = 1
    signal_str = 0
    instr_count = 0

    operations_queue = [0, 0]
    crt = ["."]*40*6
    for line in lines:
        instr_count_mod_40 = instr_count % 40
        if instr_count_mod_40 == registry or instr_count_mod_40 == registry - 1 or instr_count_mod_40 == registry + 1:
            crt[instr_count] = "#"

        instr_count += 1

        if instr_count % 20 == 0 and instr_count % 40 != 0:
            # print(instr_count)
            signal_str += registry * instr_count

        op = line.split()[0]
        if op == "noop":
            continue
        elif op == "addx":
            instr_count_mod_40 = instr_count % 40
            if instr_count_mod_40 == registry or instr_count_mod_40 == registry - 1 or instr_count_mod_40 == registry + 1:
                crt[instr_count] = "#"

            instr_count += 1
            if instr_count % 20 == 0 and instr_count % 40 != 0:
                # print(instr_count)
                signal_str += registry * instr_count
            registry += int(line.split()[1])


    # print(registry)
    print(signal_str)
    print(crt[0:40])
    print(crt[40:80])
    print(crt[80:120])
    print(crt[120:160])
    print(crt[160:200])
    print(crt[200:240])