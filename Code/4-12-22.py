import Utils


def part_one():
    overlaps = 0
    lines = Utils.read_file_as_lines("Input\\4-12-22.txt")
    for line in lines:
        sections = line.split(",")
        l_min = int(sections[0].split("-")[0])
        l_max = int(sections[0].split("-")[1])
        r_min = int(sections[1].split("-")[0])
        r_max = int(sections[1].split("-")[1])
        if (l_min >= r_min and l_max <= r_max) or \
            (r_min >= l_min and r_max <= l_max):
            overlaps += 1
    print(overlaps)


def part_two():
    overlaps = 0
    lines = Utils.read_file_as_lines("Input\\4-12-22.txt")
    for line in lines:
        sections = line.split(",")
        if not (int(sections[0].split("-")[0]) > int(sections[1].split("-")[1]) or \
            int(sections[1].split("-")[0]) > int(sections[0].split("-")[1])):
            overlaps += 1
    print(overlaps)
        

def main():
    part_one()
    part_two()


if __name__ == '__main__':
    main()
