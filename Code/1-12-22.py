import Utils


def part_one():
    lines = Utils.read_file_as_lines("Input\\1-12-22.txt")
    elf_calories = Utils.seek_until_blank_line(lines)
    sums = sorted([sum([int(n) for n in cals]) for cals in elf_calories], reverse=True)
    print(sums[:1])

def part_two():
    lines = Utils.read_file_as_lines("Input\\1-12-22.txt")
    elf_calories = Utils.seek_until_blank_line(lines)
    sums = sorted([sum([int(n) for n in cals]) for cals in elf_calories], reverse=True)
    print(sum(sums[:3]))
        

def main():
    part_one()
    part_two()


if __name__ == '__main__':
    main()
