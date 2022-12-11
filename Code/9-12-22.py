import Utils
from Classes.Node import Node


rope_knots = 10
visited_set = set()

def tick(head_ref, tail_ref, direction):
    if head_ref.id == "Head":
        move_rope(head_ref, direction)
    
    if abs(head_ref.x - tail_ref.x) > 1:
        if head_ref.y > tail_ref.y:
            move_rope(tail_ref, "U")
        elif head_ref.y < tail_ref.y:
            move_rope(tail_ref, "D")
        if head_ref.x > tail_ref.x:
            move_rope(tail_ref, "R")
        elif head_ref.x < tail_ref.x:
            move_rope(tail_ref, "L")
    elif abs(head_ref.y - tail_ref.y) > 1:
        if head_ref.y > tail_ref.y:
            move_rope(tail_ref, "U")
        elif head_ref.y < tail_ref.y:
            move_rope(tail_ref, "D")
        if head_ref.x > tail_ref.x:
            move_rope(tail_ref, "R")
        elif head_ref.x < tail_ref.x:
            move_rope(tail_ref, "L")

    #print(f"Move {head_ref.id} to ({head_ref.x}, {head_ref.y}), {tail_ref.id} to ({tail_ref.x}, {tail_ref.y})")
    if tail_ref.id == "Tail":
        visited_set.add(f"({tail_ref.x}, {tail_ref.y})")


def move_rope(ref, direction):
    match direction:
        case "U":
            ref.y += 1
        case "D":
            ref.y -= 1
        case "L":
            ref.x -= 1
        case "R":
            ref.x += 1
        case _:
            print(f"Invalid direction: {direction}")


def part_one():
    lines = Utils.read_file_as_lines(("Input\\9-12-22.txt"))

    rope_head = Node("Head", 0, 0)
    rope_tail = Node("Tail", 0, 0)

    for move in lines:
        tokens = move.split(" ")
        direction = tokens[0]
        steps = int(tokens[1])

        for _ in range(steps):
            tick(rope_head, rope_tail, direction)
    
    print(len(visited_set))


def part_two():
    lines = Utils.read_file_as_lines(("Input\\9-12-22.txt"))

    print(visited_set)
    rope = []
    rope.append(Node("Head", 0, 0))
    for knot in range(rope_knots - 2):
        rope.append(Node(f"Knot{knot + 2}", 0, 0))
    rope.append(Node("Tail", 0, 0))

    for move in lines:
        tokens = move.split(" ")
        direction = tokens[0]
        steps = int(tokens[1])

        for _ in range(steps):
            for knot in range(1, len(rope)):
                tick(rope[knot - 1], rope[knot], direction)
    
    print(visited_set)
    print(len(visited_set))
        

def main():
    part_one()
    visited_set.clear()
    part_two()


if __name__ == '__main__':
    main()
