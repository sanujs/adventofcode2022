def navigate_to_wd(filesystem, wd):
    pointer = filesystem
    for d in wd:
        pointer = pointer[d]
    return pointer

def build_filesystem():
    with open("input.txt") as f:
        filesystem = {"/": {}}
        wd = []
        pointer = filesystem
        for line in f:
            if line[0] == "$":
                match line[2:4]:
                    case "cd":
                        directory = line[5:].strip()
                        if directory == "..":
                            wd.pop()
                            pointer = navigate_to_wd(filesystem, wd)
                        else:
                            wd.append(directory)
                            pointer = pointer[directory]
                    case "ls":
                        continue
            elif line[:3] == "dir":
                directory = line[4:].strip()
                try:
                    pointer[directory]
                except KeyError:
                    pointer[directory] = {}
            else:
                file_size, file_name = line.split(" ")
                pointer[file_name.strip()] = int(file_size)
                
        return filesystem

def get_directory_sizes(filesystem):
    pointer = filesystem
    wd = []
    directory_sizes = {}

    def recursive_accumulator(pointer):
        acc = 0
        for key in pointer:
            if type(pointer[key]) == type({}):
                wd.append(key)
                tmp = recursive_accumulator(pointer[key])
                # handles multiple directories with the same name
                directory_sizes['/'.join(wd)] = tmp
                wd.pop()
                acc += tmp
            else:
                acc += pointer[key]
        return acc

    recursive_accumulator(pointer)
    return directory_sizes


def part_one(directory_sizes):
    final_sum = 0
    for directory in directory_sizes:
        if directory_sizes[directory] <= 100000:
            final_sum += directory_sizes[directory]
    return final_sum

def part_two(directory_sizes):
    TOTAL_DISK_SPACE = 70000000
    NEEDED_SPACE = 30000000
    unused_space = TOTAL_DISK_SPACE - directory_sizes["/"]
    min_deleted_file_size = NEEDED_SPACE - unused_space
    smallest_dir = directory_sizes["/"]
    for directory in directory_sizes:
        if directory_sizes[directory] >= min_deleted_file_size and directory_sizes[directory] < smallest_dir:
            smallest_dir = directory_sizes[directory]

    return smallest_dir


if __name__ == "__main__":
    directory_sizes = get_directory_sizes(build_filesystem())
    print(part_one(directory_sizes))
    print(part_two(directory_sizes))
