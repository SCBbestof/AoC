def get_path(pwd, dir):
    if pwd != '/':
        return pwd + '/' + dir
    else:
        return pwd + dir


with open("data.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    dir_stack = []
    dir_sizes = dict()
    files = {}
    pwd = "/"
    total_size = 0
    dir_size = 0
    visited_files = []
    visited_dirs = []
    for line in lines:
        print(dir_stack, pwd, dir_sizes, line, sep=" - ")
        if line.startswith("$"):
            line = line[2:]
            if line.startswith("cd"):
                dir = line[3:]
                print(pwd, dir_size, sep=" + ")
                dir_sizes[pwd] = dir_size
                dir_size = 0
                visited_files = []
                if dir.startswith(".."):
                    pwd = dir_stack.pop()
                    if pwd in dir_sizes:
                        dir_size = dir_sizes[pwd]
                elif dir.startswith("/"):
                    dir_stack = []
                    pwd = "/"
                else:
                    dir_stack.append(pwd)
                    pwd = get_path(pwd,dir)
                    if pwd in dir_sizes:
                        dir_size = dir_sizes[pwd]
        else:
            if line.startswith("dir"):
                dir = get_path(pwd, line.split(" ")[1])
                if dir in dir_sizes.keys():
                    total_size += dir_sizes[dir]
            else:
                size = int(line.split(" ")[0])
                file = line.split(" ")[1]
                if file not in visited_files:
                    dir_size += size
                    visited_files.append(file)

    dir_sizes[pwd] = dir_size
    print(dir_stack, pwd, dir_sizes, line, sep=" - ")

    for dir1 in dir_sizes.keys():
        for dir2 in dir_sizes.keys():
            if dir1 != dir2 and dir2.startswith(dir1):
                dir_sizes[dir1] += dir_sizes[dir2]

    print(dir_stack, pwd, dir_sizes, line, sep=" - ")

    total_size = 0
    added = []
    for dir in dir_sizes.keys():
        if dir not in added:
            added.append(dir)
            if dir_sizes[dir] <= 100000:
                total_size += dir_sizes[dir]
    print(total_size)

    root_size = dir_sizes["/"]
    free = 70000000 - root_size
    min = 70000000
    for dir in dir_sizes.keys():
        if free + dir_sizes[dir] >= 30000000 and min > dir_sizes[dir]:
            min = dir_sizes[dir]

    print(min)