# https://adventofcode.com/2020/day/16
from copy import deepcopy

def count_neighbours(cubeZYX, z, y, x, state):
    state_count = {".": 0, "#": 0}
    for zn in range(z - 1, z + 2):
        #print(cubeZYX[zn])
        for yn in range(y - 1, y + 2):
            for xn in range(x - 1, x + 2):
                if yn == y and xn == x and zn == z:
                    continue
                try:
                    s = cubeZYX[zn][yn][xn]
                except IndexError:
                    s = "."
                state_count[s] += 1
    return state_count[state]


def count_active(cubeZYX):
    cnt = 0
    for z in cubeZYX:
        for y in z:
            for x in y:
                cnt += x.count("#")
    return cnt

def add_dimension(cubeZYX):
    # add a layer to each dimenion
    ly = len(cubeZYX[0]) # how many vertically
    lx = len(cubeZYX[0][0]) # e.g. how many ... horizontally 
    cubeZYX.insert(0, ["." * lx]*ly)
    cubeZYX.append(["." * lx]*ly)

    for z in cubeZYX: #z = [list of strings]
        z.insert(0, "." * lx)
        z.append("." * lx)
        for i, y in enumerate(z): #y=string
            z[i] = "." + y + "."
    return deepcopy(cubeZYX)

def sim_cube(cubeZYX):
    # create the after simulation cube
    cubeZYX_after = deepcopy(cubeZYX)
    
    for z in range(len(cubeZYX)):
        for y in range(len(cubeZYX[0])):
            for x in range(len(cubeZYX[0][0])):
                s = cubeZYX[z][y][x]
                s_cnt = count_neighbours(cubeZYX, z, y, x, "#")
                if s == "#":
                    if s_cnt in (2, 3):
                        s = "#"
                        #cubeZYX_after[z][y] = cubeZYX_after[z][y][:x] + "#" + cubeZYX_after[z][y][x + 1:]
                    else:
                        s = "."
                        #cubeZYX_after[z][y] =  cubeZYX_after[z][y][:x] + "." +  cubeZYX_after[z][y][x+1:]
                else:
                    if s_cnt == 3:
                        s = "#"
                        #cubeZYX_after[z][y] =  cubeZYX_after[z][y][:x] + "#" +  cubeZYX_after[z][y][x+1:]
                cubeZYX_after[z][y] = cubeZYX_after[z][y][:x] + s + cubeZYX_after[z][y][x + 1:]
                
    return cubeZYX_after

def print_cube(cube):
    for z in cube:
        print(f"\n")
        for y in z:
            print(y)
    
def main():
    initial ="""#####...
.#..##..
##.##.##
...####.
#.#...##
.##...#.
.#.#.###
#.#.#..#"""
    cubeZYX = [initial.split("\n")]
    cubeZYX = add_dimension(cubeZYX)

    print("start")
    print_cube(cubeZYX)

    for sim in range(1,7):
        print(f"simulation {sim}")
        cubeZYX = sim_cube(cubeZYX)
        print_cube(cubeZYX)
        print(f"active = {count_active(cubeZYX)}")
        cubeZYX = add_dimension(cubeZYX)
    pass



main()
