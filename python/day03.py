def type_to_priority(item):
    if ord(item) >= 97:
        return ord(item) - 96
    return ord(item) - 38    

def part_one():
    acc = 0
    with open("input.txt") as f:
        for line in f:
            c1 = line[:len(line)//2]
            c2 = line[len(line)//2:]
            item_types = {}
            for c in c1:
                item_types[c] = None
            for c in c2:
                try:
                    item_types[c]
                except KeyError:
                    continue
                else:
                    acc += type_to_priority(c)
                    break
    return acc

def part_two():
    acc = 0
    with open("input.txt") as f:
        counter = 0
        item_types = {}
        for line in f:
            for c in line:
                try:
                    item_types[c][counter] = True
                except KeyError:
                    item_types[c] = [False, False, False]
                    item_types[c][counter] = True
                if not False in item_types[c]:
                    acc += type_to_priority(c)
                    break
            counter += 1
            if counter > 2:
                counter = 0
                item_types = {}
    return acc

if __name__ == "__main__":
    print(part_one())
    print(part_two())