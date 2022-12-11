import Utils

vis_map = {}
score_map = {}

def calculate_visibility(forest, row, tree):
    length = len(forest)
    width = len(forest[0])
    height = forest[row][tree]
    tree_id = length * row + tree

    if row == 0 or \
        tree == 0 or \
        row == length - 1 or \
        tree == width - 1:
        vis_map[tree_id] = True
    else:
        vis_n, vis_s, vis_e, vis_w = True, True, True, True

        for i in range(row, 0, -1):
            vis_n = vis_n and forest[row - i][tree] < height 

        for i in range(1, length - row):
            vis_s = vis_s and forest[row + i][tree] < height 

        for i in range(tree, 0, -1):
            vis_w = vis_w and forest[row][tree - i] < height

        for i in range(1, width - tree):
            vis_e = vis_e and forest[row][tree + i] < height
        
        vis_map[tree_id] = vis_n or vis_s or vis_e or vis_w


def calculate_visibility_score(forest, row, tree):
    length = len(forest)
    width = len(forest[0])
    height = forest[row][tree]
    tree_id = length * row + tree
    score_n, score_s, score_e, score_w = 0, 0, 0, 0

    for i in range(1, row + 1):
        score_n += 1
        
        if forest[row - i][tree] >= height:
            break

    for i in range(1, length - row):
        score_s += 1

        if forest[row + i][tree] >= height:
            break

    for i in range(1, tree + 1):
        score_w += 1
        if forest[row][tree - i] >= height:
            break

    for i in range(1, width - tree):
        score_e += 1
        if forest[row][tree + i] >= height:
            break

    score_map[tree_id] = score_n * score_s * score_e * score_w

# Comments
def part_one():
    lines = Utils.read_file_as_lines(("Input\\8-12-22.txt"))
    forest = []

    for line in lines:
        forest.append([int(n) for n in line])
    
    for row in range(0, len(forest)):
        for tree in range(0, len(forest[row])):
            calculate_visibility(forest, row, tree)
    
    print(list(vis_map.values()).count(True))
    

# Comments
def part_two():
    lines = Utils.read_file_as_lines(("Input\\8-12-22.txt"))
    forest = []

    for line in lines:
        forest.append([int(n) for n in line])
    
    for row in range(0, len(forest)):
        for tree in range(0, len(forest[row])):
            calculate_visibility_score(forest, row, tree)
    
    print(max(list(score_map.values())))
        

def main():
    part_one()
    part_two()


if __name__ == '__main__':
    main()
