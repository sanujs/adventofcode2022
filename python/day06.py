def dup_chars(marker):
    for i in range(len(marker)):
        if marker[i] in marker[i+1:]:
            return True
    return False

def marker_finder(length):
    with open("input.txt") as f:
        counter = length-1
        marker = f.read(length-1)
        for char in f.read():
            counter += 1 
            if not dup_chars(marker[-1*(length-1):] + char):
                return counter
            marker = marker[-1*(length-1):] + char
    return counter
    

def part_one():
    return marker_finder(4)

def part_two():
    return marker_finder(14)

if __name__ == "__main__":
    print(part_one())
    print(part_two())
