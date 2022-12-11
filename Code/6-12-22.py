import Utils


def part_one():
    window = []
    line = Utils.read_file_as_lines("Input\\6-12-22.txt")[0]
    for index in range(len(line)):
        window.append(line[index])

        if len(window) < 4:
            continue

        window_set = set(window)

        if len(window_set) == 4:
            print(index + 1)
            return

        window.pop(0)


def part_two():
    window = []
    line = Utils.read_file_as_lines("Input\\6-12-22.txt")[0]
    for index in range(len(line)):
        window.append(line[index])

        if len(window) < 14:
            continue

        window_set = set(window)

        if len(window_set) == 14:
            print(index + 1)
            return

        window.pop(0)
        

def main():
    part_one()
    part_two()


if __name__ == '__main__':
    main()
