import Utils

stacks = {
    1: ['J', 'H', 'G', 'M', 'Z', 'N', 'T', 'F'],
    2: ['V', 'W', 'J'],
    3: ['G', 'V', 'L', 'J', 'B', 'T', 'H'],
    4: ['B', 'P', 'J', 'N', 'C', 'D', 'V', 'L'],
    5: ['F', 'W', 'S', 'M', 'P', 'R', 'G'],
    6: ['G', 'H', 'C', 'F', 'B', 'N', 'V', 'M'],
    7: ['D', 'H', 'G', 'M', 'R'],
    8: ['H', 'N', 'M', 'V', 'Z', 'D'],
    9: ['G', 'N', 'F', 'H'],
}

def part_one():
    lines = Utils.read_file_as_lines("Input\\5-12-22.txt")[10:]
    for line in lines:
        tokens = line.split(" ")
        moves = int(tokens[1])
        start = int(tokens[3])
        end = int(tokens[5])

        for move in range(moves):
            container = stacks[start].pop()
            stacks[end].append(container)
    print(stacks)


def part_two():
    lines = Utils.read_file_as_lines("Input\\5-12-22.txt")[10:]
    for line in lines:
        tokens = line.split(" ")
        moves = int(tokens[1])
        start = int(tokens[3])
        end = int(tokens[5])

        container = []
        for move in range(moves):
            if len(stacks[start]) > 0:
                container.append(stacks[start].pop())
        for move in range(moves):
            if len(container) > 0:
                stacks[end].append(container.pop())
    print(stacks)
        

def main():
    part_one()
    part_two()


if __name__ == '__main__':
    main()
