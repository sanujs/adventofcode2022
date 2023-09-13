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

def safe_seek(f, seek_position):
    try:
        f.seek(seek_position, 0)
        return True
    except ValueError:
        return False

def get_scenic_score(f, cur_tree, width):
    if not cur_tree.isdigit(): return 0
    cur_position = f.tell()
    offset_map = {
        'left': -2,
        'right': 0,
        'top': -width,
        'bottom': width,
    }
    scenic_score = 1
    for key in offset_map:
        f.seek(cur_position)
        counter = 0
        if not safe_seek(f, f.tell() + offset_map[key]):
            f.seek(cur_position)
            return 0
        tree = f.read(1)
        while tree.isdigit():
            counter += 1
            if int(tree) >= int(cur_tree) or not safe_seek(f, f.tell() + offset_map[key]):
                break
            tree = f.read(1)
        scenic_score *= counter
    f.seek(cur_position)
    return scenic_score

def part_two():
    largest_scenic_score = 0
    with open("input.txt") as f:
        width = len(f.readline().strip())
        print(width)
        f.seek(0, 2)
        eof = f.tell()
        f.seek(0)
        counter = 0
        while f.tell() < eof:
            cur_score = get_scenic_score(f, f.read(1), width)
            counter += 1
            if cur_score > largest_scenic_score:
                largest_scenic_score = cur_score

    return largest_scenic_score

if __name__ == "__main__":
    print(part_one())
    print(part_two())
