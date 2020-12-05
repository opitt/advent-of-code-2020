# https://adventofcode.com/2020/day/3

# part 1
with open("input_day3.txt", encoding="utf-8") as input:
    forest = input.readlines()
forest = [row.strip() for row in forest]    

def count_trees_for_slope(right, down):
    trees, pos_x, width = 0, 1, len(forest[0])

    for pos_y in range(0,len(forest),down):
        trees += forest[pos_y][pos_x-1] == "#"
        #print(pos_y, forest[pos_y], pos_x)
        #print(pos_y, "^".rjust(pos_x), pos_x, f"(#{trees})")
        pos_x = (pos_x+right-width) if (pos_x+right>width) else pos_x+right
    return trees

trees = count_trees_for_slope(3,1)
print(f"I encountered {trees} trees.")

# part 2
trees_product = 1
for r,d in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
    trees_product *= count_trees_for_slope(r,d)
print(f"All trees encountered on slopes multiplied with each other result in {trees_product}.")
