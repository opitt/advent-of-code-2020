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
    plan = [row.rstrip() for row in plan]
    EMPTY = "L"
    FULL = "#"    
    FLOOR = "."

    #! add walls as floor ".""
    #! so the seat plan starts with index 1 and ends with -2
    wall = [FLOOR]*(len(plan[0])+1)
    newplan = [wall] # the top wall
    newplan.extend( [[FLOOR]+[*row]+[FLOOR] for row in plan] ) #build the left and right wall
    newplan.append(wall) # the bottom wall
    plan = copy.deepcopy(newplan) # replace the org plan with the wall plan


    #PART 1
    def look1(plan, lookfor, r, c):
        count_adj = 0
        for ir in range(r - 1, r + 1 + 1): # rows above, same, and one below the seat
            for ic in range(c - 1, c + 1 + 1): # columns left, same, and one right the seat
                if ir == r and ic == c:  # ignore the seat itself
                    continue
                count_adj += plan[ir][ic] == lookfor  # count the seats
        return count_adj

    def simseating1(plan, r, c):
        seat = plan[r][c]
        count_adj = 0
        changed = False
        if  seat == FLOOR: # do nothing if there is not seat
            changed = False
        elif seat == EMPTY:  #seat is empty; if there is no full seat around, sit down i.e. fill the seat
            count_adj = look1(plan, FULL, r, c)  # count the full seats
            if count_adj == 0: # if no seat is taken around the seat, sit down
                simplan[r][c] = FULL
                changed = True
        elif seat == FULL:  #seat is full, if there are more than 4+ seats around also full, leave the seat, i.e. empty the seat
            count_adj = look1(plan, FULL, r, c)  # count the full seats
            if count_adj >= 4:
                simplan[r][c] = EMPTY
                changed = True
        return changed
    
    simplan = copy.deepcopy(plan)
    newplan = copy.deepcopy(plan)
    simcnt = count(1)
    while True:
        changes = 0
        print(f">> Simulation {next(simcnt)}\n", "\n".join(["".join(row)[1:-1] for row in simplan[1:-1]]) + "\n")

        for row in range(1, len(newplan) - 1):
            for col in range(1, len(newplan[0]) - 1):
                if simseating1(newplan, row, col): # this function simulates seatig based on newplan and updates the outcome in simplan
                    changes += 1

        if changes>0: # if the seating changed, take the new seating and simulate again
            newplan = copy.deepcopy(simplan)
        else:
            break

    result_part1 = sum([row.count(FULL) for row in simplan ])
    print(f"Part 1: The occupied seats: {result_part1}") 
    
    #! PART 2 starts here
    #!
    def look2(plan, lookfor, cell_r, cell_c, row_dir, col_dir):
        #this function looks for lookfor in the direction given by row_dir, col_dir (-1,0,1)
        row = count(cell_r + row_dir, row_dir)
        ir = next(row)
        col = count(cell_c + col_dir, col_dir)
        ic = next(col)
        while ir > 0 and ir < len(plan) and ic > 0 and ic < len(plan[0]):
            if plan[ir][ic] == lookfor:
                return True
            elif plan[ir][ic] != FLOOR:
                return False
            ic = next(col)
            ir = next(row)
        return False

    def simseating2(plan, r, c):
        seat = plan[r][c]
        count_vis = 0
        changed = False
        if  seat == FLOOR:
            changed = False
        else:
            count_vis += look2(plan, FULL, r, c, -1, 0) #top
            count_vis += look2(plan, FULL, r, c, -1, 1) #top, right diagonal
            count_vis += look2(plan, FULL, r, c, 0, 1) #right
            count_vis += look2(plan, FULL, r, c, 1, 1) #bottom, right diagonal
            count_vis += look2(plan, FULL, r, c, 1, 0) #bottom
            count_vis += look2(plan, FULL, r, c, 1, -1) #bottom, left diagonal
            count_vis += look2(plan, FULL, r, c, 0, -1) #left
            count_vis += look2(plan, FULL, r, c, -1, -1) #top, left diagonal
            if seat == EMPTY and count_vis == 0:
                simplan[r][c] = FULL
                changed = True
            if seat == FULL and count_vis >= 5:
                simplan[r][c] = EMPTY
                changed = True        
        return changed

    print("***** PART 2 *****")
    simplan = copy.deepcopy(plan)
    newplan = copy.deepcopy(plan)
    simcnt = count(1)
    while True:
        changes = 0
        print(f">> Simulation {next(simcnt)}\n", "\n".join(["".join(row)[1:-1] for row in simplan[1:-1]]) + "\n")
        for r in range(1, len(newplan)-1):
            for c in range(1,len(newplan[0]) - 1):
                if simseating2(newplan, r, c):
                    changes += 1

        if changes>0:
            newplan = copy.deepcopy(simplan)
        else:
            break
    
    result_part2=sum([row.count(FULL) for row in simplan ])
    print(f"Part 2: The occupied seats: {result_part2}") #1973822685184

main(11)
