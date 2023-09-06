def string_to_range(elf):
    start, stop = [int(i) for i in elf.split("-")]
    return range(start, stop+1)

def part_one():
    with open("input.txt") as f:
        acc = 0
        for line in f:
            elf1, elf2 = [string_to_range(i) for i in line.split(",")]
            if elf1.start in elf2 and elf1.stop - 1 in elf2 or \
                elf2.start in elf1 and elf2.stop - 1 in elf1:
                acc+=1
    return acc

def part_two():
    with open("input.txt") as f:
        acc = 0
        for line in f:
            elf1, elf2 = [string_to_range(i) for i in line.split(",")]
            # start of one is contained in the other or the end of one is contained in the other
            if elf1.start in elf2 or elf1.stop - 1 in elf2 or elf2.start in elf1 or elf2.stop - 1 in elf1:
                acc += 1 
    return acc
if __name__ == "__main__":
    print(part_one())
    print(part_two())