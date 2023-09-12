def vis_left():
    visible = []
    with open("input.txt") as f:
        for y, row in enumerate(f):
            highest_tree = -1
            for x, tree in enumerate(row.strip()):
                if int(tree) > highest_tree:
                    visible.append((x, y))
                    highest_tree = int(tree)
    return visible

def vis_right():
    visible = []
    with open("input.txt") as f:
        for y, row in enumerate(f):
            highest_tree = -1
            for x, tree in reversed(list(enumerate(row.strip()))):
                if int(tree) > highest_tree:
                    visible.append((x, y))
                    highest_tree = int(tree)
    return visible

def vis_top():
    visible = []
    with open("input.txt") as f:
        for x, _ in enumerate(f.readline().strip()):
            highest_tree = -1
            f.seek(0)
            for y, row in enumerate(f):
                tree = row[x]
                if int(tree) > highest_tree:
                    visible.append((x, y))
                    highest_tree = int(tree)
    return visible

def vis_bottom():
    visible = []
    with open("input.txt") as f:
        for x, _ in enumerate(f.readline().strip()):
            highest_tree = -1
            f.seek(0)
            for y, row in reversed(list(enumerate(f))):
                tree = row[x]
                if int(tree) > highest_tree:
                    visible.append((x, y))
                    highest_tree = int(tree)
    return visible

def part_one():
    return len(set(vis_left() + vis_right() + vis_top() + vis_bottom()))

if __name__ == "__main__":
    print(part_one())
