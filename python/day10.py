def read_signal(c, x):
    cycles = [20 + 40 * i for i in range(6)]
    if c in cycles:
        return c * x
    return 0

def part_one():
    x = 1
    cycle = 0
    signal_strengths = 0

    def tick():
        nonlocal cycle, signal_strengths
        cycle += 1
        signal_strengths += read_signal(cycle, x)

    with open("input.txt") as f:
        for line in f:
            match line.strip():
                case "noop":
                    tick()
                case _:
                    tick()
                    tick()
                    x += int(line.split(" ")[1])
    return signal_strengths

def part_two():
    x = 1
    cycle = 0
    output = ""

    def tick():
        nonlocal cycle
        cycle += 1
        position = (cycle - 1) % 40
        ret = "#" if abs(position - x) <= 1 else "."
        if cycle % 40 == 0:
            ret += "\n"
        return ret

    with open("input.txt") as f:
        for line in f:
            match line.strip():
                case "noop":
                    output += tick()
                case _:
                    output += tick()
                    output += tick()
                    x += int(line.split(" ")[1])
    return output

if __name__ == "__main__":
    print(part_one())
    print(part_two())
