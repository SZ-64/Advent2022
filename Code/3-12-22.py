import Utils


def part_one():
    errors = []
    total_priority = 0
    lines = Utils.read_file_as_lines("Input\\3-12-22.txt")
    for line in lines:
        comp_one = set(line[:int(len(line)/2)])
        comp_two = set(line[int(len(line)/2):])
        errors.append(comp_one.intersection(comp_two).pop())
    for error in errors:
        total_priority += (ord(error) - 38) if error.isupper() else (ord(error) - 96)
    print(total_priority)


def part_two():
    total_priority = 0
    lines = Utils.read_file_as_lines("Input\\3-12-22.txt")
    groups = [lines[i:i+3] for i in range(0, len(lines), 3)]
    for group in groups:
        badge = set(group[0]).intersection(set(group[1])).intersection(set(group[2])).pop()
        total_priority += (ord(badge) - 38) if badge.isupper() else (ord(badge) - 96)
    print(total_priority)
        

def main():
    part_one()
    part_two()


if __name__ == '__main__':
    main()
