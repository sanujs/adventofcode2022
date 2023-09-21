class Monkey:
    def __init__(self, label, items, op_str, throw_divisor, throw_true, throw_false):
        self.label = label
        self.items = [int(item) for item in items]
        self.throw_divisor = throw_divisor
        self.throw_true = throw_true
        self.throw_false = throw_false
        self.inspect_count = 0
        program = f"def op(old): return {op_str}"
        d = {}
        exec(program, d)
        self.inspect = d['op']
        # print(f"Monkey {label} has items {self.items}\n{self.inspect}\nif divisible by {throw_divisor}\ntrue {throw_true} false {throw_false}\n")

    def receive(self, item):
        self.items.append(item)

    def turn(self, part):
        if part == 1:
            new_items = [self.inspect(item)//3 for item in self.items]
        else:
            new_items = [self.inspect(item) for item in self.items]
        item_throws = [(item, self.throw_true if item % self.throw_divisor == 0 else self.throw_false) for item in new_items]
        self.inspect_count += len(new_items)
        self.items = []
        return item_throws

def round(monkeys, part):
    for monkey in monkeys:
        item_throws = monkey.turn(part)
        for item, rec_monkey in item_throws:
            monkeys[rec_monkey].receive(item)

def parse_input():
    monkeys = []
    with open("input.txt") as f:
        line = f.readline()
        while line != "":
            label = int(line.removeprefix("Monkey ").removesuffix(":\n"))
            items = f.readline().strip().removeprefix("Starting items: ").split(", ")
            op_str = f.readline().strip().removeprefix("Operation: new = ")
            throw_divisor = int(f.readline().strip().split(" ")[-1])
            throw_true = int(f.readline().strip().split(" ")[-1])
            throw_false = int(f.readline().strip().split(" ")[-1])
            monkeys.append(Monkey(label, items, op_str, throw_divisor, throw_true, throw_false))
            f.readline()
            line = f.readline()

    return monkeys

def part_one():
    monkeys = parse_input()
    for _ in range(20):
        round(monkeys, 1)
    counts = [monkey.inspect_count for monkey in monkeys]
    i = max(counts)
    counts.remove(i)
    return i * max(counts)

def part_two():
    monkeys = parse_input()
    for _ in range(100):
        round(monkeys, 2)
    for monkey in monkeys:
        print(monkey.items)
    counts = [monkey.inspect_count for monkey in monkeys]
    print(counts)
    i = max(counts)
    counts.remove(i)
    return i * max(counts)

if __name__=="__main__":
    print(part_one())
    print(part_two())
