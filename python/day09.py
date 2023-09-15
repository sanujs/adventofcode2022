def move_head(direction, last_position):
    match direction:
        case "L":
            return (last_position[0] - 1, last_position[1])
        case "R":
            return (last_position[0] + 1, last_position[1])
        case "U":
            return (last_position[0], last_position[1] + 1)
        case "D":
            return (last_position[0], last_position[1] - 1)

def is_knot_too_far(next_knot, cur_knot):
    return abs(next_knot[0] - cur_knot[0]) > 1 or abs(next_knot[1] - cur_knot[1]) > 1

def move_knot(next_knot, cur_knot):
    new_x, new_y = cur_knot
    if next_knot[0] != cur_knot[0]:
        new_x += -1 if next_knot[0] < cur_knot[0] else 1
    if next_knot[1] != cur_knot[1]:
        new_y += -1 if next_knot[1] < cur_knot[1] else 1
    return (new_x, new_y)

def part_one():
    starting_position = (0, 0)
    head = [starting_position]
    tail = [starting_position]
    with open("input.txt") as f:
        for line in f:
            direction, frequency = line.strip().split(" ")
            for _ in range(int(frequency)):
                head.append(move_head(direction, head[-1]))
                if is_knot_too_far(head[-1], tail[-1]):
                    tail.append(head[-2])
    return len(set(tail))

def part_two():
    starting_position = (0, 0)
    head = [starting_position]
    # [H...T]
    current_rope = [starting_position for _ in range(10)]
    tail = [starting_position]
    with open("input.txt") as f:
        for line in f:
            direction, frequency = line.strip().split(" ")
            for _ in range(int(frequency)):
                head.append(move_head(direction, head[-1]))
                current_rope[0] = head[-1]
                for i in range(len(current_rope) - 1):
                    if is_knot_too_far(current_rope[i], current_rope[i+1]):
                        current_rope[i+1] = move_knot(current_rope[i], current_rope[i+1])
                    else:
                        break
                tail.append(current_rope[-1])
    return len(set(tail))

if __name__ == "__main__":
    print(part_one())
    print(part_two())
