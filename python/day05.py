def create_stacks(f):
    line = f.readline()
    numstacks = len(line)//4
    stacks = [[] for _ in range(numstacks)]
    while line != "\n":
        for i in range(numstacks):
            stacks[i].append(line[i*4:(i+1)*4].strip())
        line = f.readline()
    for i in range(numstacks):
        stacks[i].pop()
        stacks[i].reverse()
        while True:
            try:
                stacks[i].remove('')
            except ValueError:
                break
    return stacks

def part_one():
    with open("input.txt") as f:
        stacks = create_stacks(f)
        for line in f:
            line = line.split(" ")
            for _ in range(int(line[1])):
                stacks[int(line[5])-1].append(stacks[int(line[3])-1].pop())
    return ''.join([stacks[i].pop()[1] for i in range(len(stacks))])

def part_two():
    with open("input.txt") as f:
        stacks = create_stacks(f)
        for line in f:
            line = line.split(" ")
            stacks[int(line[5])-1].extend(stacks[int(line[3])-1][-1*int(line[1]):])
            del stacks[int(line[3])-1][-1*int(line[1]):]
    return ''.join([stacks[i].pop()[1] for i in range(len(stacks))])

if __name__ == "__main__":
    print(part_one())
    print(part_two())