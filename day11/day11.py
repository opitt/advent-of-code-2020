# https://adventofcode.com/2020/day/10

import os
import copy
from itertools import count

def main(day):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, f"input_day{day}.txt"), encoding="utf-8") as input:
    #with open(os.path.join(script_path, f"test.txt"), encoding="utf-8") as input:
        plan = input.readlines()

    #! add the walls as floor!
    #! so the seat plan starts with index 1 and ends with -2 #######
    wall = ["."]*(len(plan[0])+1)
    newplan = [wall]
    newplan.extend([["."]+[*row.rstrip()]+["."] for row in plan] )
    newplan.append(wall)
    plan = copy.deepcopy(newplan)
    newplan = []


    #PART 1
    def simseat(plan, r, c):
        seat = plan[r][c]
        count_adj = 0
        changed = False
        if  seat == ".":
            changed = False
        elif seat == "L":  #empty, and no other ajacent places occupied => #
            for ir in range(r - 1, r + 1 + 1):
                for ic in range(c - 1, c + 1 + 1):
                    if ir == r and ic == c:
                        continue
                    if plan[ir][ic] in [".", "L"]:
                        count_adj += 1
            if count_adj == 8:
                simplan[r][c] = "#"
                changed = True
        elif seat == "#":  #empty, and no other ajacent places occupied => #
            for ir in range(r - 1, r + 1 + 1):
                for ic in range(c - 1, c + 1 + 1):
                    if ir == r and ic == c:
                        continue
                    if plan[ir][ic] == "#":
                        count_adj += 1
            if count_adj >= 4:
                simplan[r][c] = "L"
                changed = True
        return changed
    
    empty = "L"
    full = "#"    

    simplan = copy.deepcopy(plan)
    newplan = copy.deepcopy(plan)
    rowmax = len(newplan)-1
    colmax = len(newplan[0]) - 1
    simcnt = 0
    while True:
        simcnt += 1
        changes = 0
        print("\n".join(["".join(row)[1:-1] for row in simplan[1:-1]]) + "\n")

        for r in range(1, rowmax):
            for c in range(1,colmax):
                if simseat(newplan, r, c):
                    changes += 1
        

        if changes>0:
            newplan = copy.deepcopy(simplan)
        else:
            break

    result_part1 = sum([row.count("#") for row in simplan ])
    print(f"Part 1: The occupied seats: {result_part1}") 
    

    def look(plan, lookfor, cell_r, cell_c, row_dir, col_dir):

        row = count(cell_r + row_dir, row_dir)
        ir = next(row)
        col = count(cell_c + col_dir, col_dir)
        ic = next(col)
        while ir > 0 and ir < len(plan) and ic > 0 and ic < len(plan[0]):
            if plan[ir][ic] == lookfor:
                return True
            elif plan[ir][ic] != ".":
                return False
            ic = next(col)
            ir = next(row)
        return False


    def simseat2(plan, r, c):
        seat = plan[r][c]
        count_vis = 0
        changed = False

        if  seat == ".":
            changed = False
        elif seat == empty:
            #top
            count_vis += look(plan, full, r, c, -1, 0)
            #top, right diagonal
            count_vis += look(plan, full, r, c, -1, 1)
            #right
            count_vis += look(plan, full, r, c, 0, 1)
            #bottom, right diagonal
            count_vis += look(plan, full, r, c, 1, 1)
            #bottom
            count_vis += look(plan, full, r, c, 1, 0)
            #bottom, left diagonal
            count_vis += look(plan, full, r, c, 1, -1)
            #left
            count_vis += look(plan, full, r, c, 0, -1)
            #top, left diagonal
            count_vis += look(plan, full, r, c, -1, -1)
        
            if count_vis == 0:
                simplan[r][c] = full
                changed = True

        elif seat == full:
            #top
            count_vis += look(plan, full, r, c, -1, 0)
            #top, right diagonal
            count_vis += look(plan, full, r, c, -1, 1)
            #right
            count_vis += look(plan, full, r, c, 0, 1)
            #bottom, right diagonal
            count_vis += look(plan, full, r, c, 1, 1)
            #bottom
            count_vis += look(plan, full, r, c, 1, 0)
            #bottom, left diagonal
            count_vis += look(plan, full, r, c, 1, -1)
            #left
            count_vis += look(plan, full, r, c, 0, -1)
            #top, left diagonal
            count_vis += look(plan, full, r, c, -1, -1)

            if count_vis >= 5:
                simplan[r][c] = empty
                changed = True
        
        return changed

    print("***** PART 2 *****")
    simplan = copy.deepcopy(plan)
    newplan = copy.deepcopy(plan)
    rowmax = len(newplan)-1
    colmax = len(newplan[0]) - 1
    simcnt = 0
    while True:
        simcnt += 1
        changes = 0
        print("\n".join(["".join(row)[1:-1] for row in simplan[1:-1]]) + "\n")

        for r in range(1, rowmax):
            for c in range(1,colmax):
                if simseat2(newplan, r, c):
                    changes += 1

        if changes>0:
            newplan = copy.deepcopy(simplan)
        else:
            break
    
    result_part2=sum([row.count("#") for row in simplan ])
    print(f"Part 2: The occupied seats: {result_part2}") #1973822685184

main(11)
