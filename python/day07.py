import pprint
    
def build_filesystem():
    with open("input.txt") as f:
        filesystem = {"/": {}}
        wd = []
        pointer = filesystem
        def navigate_to_wd(filesystem):
            pointer = filesystem
            for d in wd:
                pointer = pointer[d]
            return pointer

        for line in f:
            if line[0] == "$":
                match line[2:4]:
                    case "cd":
                        directory = line[5:].strip()
                        if directory == "..":
                            wd.pop()
                            pointer = navigate_to_wd(filesystem)
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
                    


def part_one():
    filesystem = build_filesystem()


if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(part_one())