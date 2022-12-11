import Utils
import math

cycle = 0
register = 1
signal_strength = 0
output = []
screen = []


def tick(cmd, val, part_two=False):
    global cycle, register, signal_strength

    cycle += 1
    signal_strength = cycle * register

    if part_two:
        row = math.floor((cycle - 1) / 40)
        pos = (cycle - 1) % 40
        if register - 1 == pos or register == pos or register + 1 == pos:
            screen[row][pos] = "#"

    if cycle in [20, 60, 100, 140, 180, 220]:
        output.append(signal_strength)    
    
    register += val

def part_one():
    lines = Utils.read_file_as_lines(("Input\\10-12-22.txt"))
    
    for cmd in lines:
        tokens = cmd.split(" ")
        match tokens[0]:
            case "noop":
                tick(cmd, 0)
            case "addx":
                tick(cmd, 0)
                tick(cmd, int(tokens[1]))
            case _:
                print("Invalid command.")
    
    print(sum(output))


def reset():
    global cycle, register, signal_strength
    cycle = 0
    register = 1
    signal_strength = 0
    output.clear()
    screen.clear()

    for i in range(6):
        screen.append([])
        for j in range(40):
            screen[i].append(".")


def part_two():
    lines = Utils.read_file_as_lines(("Input\\10-12-22.txt"))

    for cmd in lines:
        tokens = cmd.split(" ")
        match tokens[0]:
            case "noop":
                tick(cmd, 0, True)
            case "addx":
                tick(cmd, 0, True)
                tick(cmd, int(tokens[1]), True)
            case _:
                print("Invalid command.")
    
    for i in range(6):
        for j in range(40):
            print(screen[i][j], end="")
        print()


def main():
    reset()
    part_one()
    reset()
    part_two()


if __name__ == '__main__':
    main()
