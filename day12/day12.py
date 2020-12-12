# https://adventofcode.com/2020/day/12

import os

def main(day):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, f"input_day{day}.txt"), encoding="utf-8") as input:
    #with open(os.path.join(script_path, f"test.txt"), encoding="utf-8") as input:
        directions = input.readlines()
    cmds = [(row[0], int(row[1:-1])) for row in directions] # list of tupels with cmd and par
    cmd_inc_or_decr = {"N": 1,
                        "S": -1,
                        "E": 1,
                        "W": -1,
                        "L": -1,
                        "R": 1,
                        }

    #! PART 1
    #!
    ship = [0,0]
    facing = 0  # 0° => facing EAST; left
    facing_inc_or_decr = {0: (1, 0), #EAST - change x,y   
                      90: (0, -1), #SOUTH 
                      180: (-1, 0), #WEST
                      270: (0, 1) #NORTH
                    } 

    for cmd, par in cmds:
        if cmd in ["E", "W"]: #x coordinate
            ship[0] += cmd_inc_or_decr[cmd]*par
        elif cmd in ["N", "S"]: #y coordinate
            ship[1] += cmd_inc_or_decr[cmd]*par
        elif cmd in ["L", "R"]: # rotate/facing
            facing += cmd_inc_or_decr[cmd]*par
            facing = 360 + facing if facing<0 else facing
            facing = facing % 360
        elif cmd == "F": # move ship in facing direction
            ship[0] += facing_inc_or_decr[facing][0]*par
            ship[1] += facing_inc_or_decr[facing][1]*par

    result_part1 = sum(map(abs,ship))
    print(f"Part 1: The distance is: {result_part1}") #439
    
    #! PART 2 starts here
    #!
    #PART 1
    ship = [0, 0] #x,y
    wp = [10,1] # relative postion to ship!
    
    def rotwp90(n, rotright):
        for _ in range(n):
            wp[0], wp[1] = (wp[1], wp[0] * -1) if rotright else (wp[1] * -1, wp[0])
        
    for cmd, par in cmds:
        if cmd in ["E", "W"]:
            wp[0] += cmd_inc_or_decr[cmd] * par
        elif cmd in ["N", "S"]:
            wp[1] += cmd_inc_or_decr[cmd] * par
        elif cmd in ["L", "R"]:
            rotwp90(par//90,cmd=="R")
        elif cmd == "F":
            ship[0] += par * wp[0]
            ship[1] += par * wp[1]            
    
    result_part2 = sum(map(abs,ship))
    print(f"Part 2: The distance is: {result_part2}") #12385

main(12)
