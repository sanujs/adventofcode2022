def part_one():
    with open("input.txt") as f:
        maximum = -1
        tmp = 0
        for line in f:
            if line == "\n":
                if tmp > maximum :
                    maximum  = tmp
                tmp = 0
            else:
                tmp += int(line)
        return maximum 

def part_two():
    with open("input.txt") as f:
        maxes = [-1, -1, -1]
        tmp = 0
        for line in f:
            if line == "\n":
                for i in range(3):
                    if tmp > maxes[i]:
                        maxes.insert(i, tmp)
                        maxes.pop()
                        break
                tmp = 0
            else:
                tmp += int(line)
        return sum(maxes) 
            
if __name__ == "__main__":
    print(part_one())
    print(part_two())