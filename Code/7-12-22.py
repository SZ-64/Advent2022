import Utils
from Classes.FileNode import FileNode

root = FileNode("/", 0, None)
dirs = set()

def compute_dir_sizes(dir, limit):
    if len(dir.children) == 0:
        return 0
    else:
        dir_size = 0
        for child in dir.children:
            dir_size += child.get_dir_size()
        if dir_size < limit:
            dirs.add(dir)
        
        for child in dir.children:
            compute_dir_sizes(child, limit)

def compute_dir_sizes2(dir, limit):
    if len(dir.children) == 0:
        return 0
    else:
        dir_size = 0
        for child in dir.children:
            dir_size += child.get_dir_size()
        if dir_size > limit:
            dirs.add(dir)
        
        for child in dir.children:
            compute_dir_sizes2(child, limit)


# Comments
def part_one():
    cwd = root
    cur_files = []
    output = Utils.read_file_as_lines("Input\\7-12-22.txt")[1:]
    for index in range(len(output)):
        tokens = output[index].split(" ")
        if tokens[0] == "$":
            if tokens[1] == "cd":
                if tokens[2] == "..":
                    cwd = cwd.parent
                else:
                    cwd = cwd.find_by_name(tokens[2])
                print(f"CWD is now {cwd.name}")
            elif tokens[1] == "ls":
                print(f"Listing files for {cwd.name}")
        else:
            if tokens[0] == "dir":
                new_dir = FileNode(tokens[1], 0, cwd)
                cwd.add_child(new_dir)
                print(f"Adding dir {new_dir.name}, {new_dir.size}")
            else:
                new_file = FileNode(tokens[1], int(tokens[0]), cwd)
                cwd.add_child(new_file)
                print(f"Adding file {new_file.name}, {new_file.size}")

    print("Calculating file sizes...")
    compute_dir_sizes(root, 100000)
    print(dirs)
    print(sum([node.get_dir_size() for node in dirs]))


# Comments
def part_two():
    total_space = 70000000
    required_space = 30000000
    free_space = total_space - root.get_dir_size()
    print(f"Free space: {free_space}")
    print(f"Required space: {required_space}")
    print(f"Difference: {required_space - free_space}")

    dirs.clear()
    compute_dir_sizes2(root, required_space - free_space)
    print(dirs)
    print(sorted([node.get_dir_size() for node in dirs]))


def main():
    part_one()
    part_two()


if __name__ == '__main__':
    main()
