import Utils

points_map = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}

outcome_map = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

input_map = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors',
    'X': 'Rock',
    'Y': 'Paper',
    'Z': 'Scissors'
}

def part_one():
    total_score = 0
    lines = Utils.read_file_as_lines("Input\\2-12-22.txt")
    for line in lines:
        tokens = line.split(' ')
        if input_map[tokens[0]] == input_map[tokens[1]]:
            total_score += (points_map[tokens[1]] + 3)
        elif input_map[tokens[0]] == 'Rock' and input_map[tokens[1]] == 'Paper':
            total_score += (points_map[tokens[1]] + 6)
        elif input_map[tokens[0]] == 'Paper' and input_map[tokens[1]] == 'Scissors':
            total_score += (points_map[tokens[1]] + 6)
        elif input_map[tokens[0]] == 'Scissors' and input_map[tokens[1]] == 'Rock':
            total_score += (points_map[tokens[1]] + 6)
        else:
            total_score += points_map[tokens[1]]
    print(total_score)


def part_two():
    total_score = 0
    lines = Utils.read_file_as_lines("Input\\2-12-22.txt")
    for line in lines:
        tokens = line.split(' ')
        if outcome_map[tokens[1]] == 0:
            total_score += ((points_map[tokens[0]] - 1 - 1) % 3) + 1
        if outcome_map[tokens[1]] == 3:
            total_score += points_map[tokens[0]] + outcome_map[tokens[1]]
        if outcome_map[tokens[1]] == 6:
            total_score += (points_map[tokens[0]] % 3) + 1 + outcome_map[tokens[1]]
    print(total_score)


def main():
    part_one()
    part_two()


if __name__ == '__main__':
    main()
