# https://adventofcode.com/2020/day/8

import os

def execute (code):
    #code: list of [commands, parameter] 
    #valid commands: nop, acc, jmp
    line_history = []
    line, acc  = 0, 0
    is_looping = False
    last_line = len(code) - 1
    while line != last_line:
        cmd, parm = code[line][0], code[line][1]
        if cmd in ["nop", "acc"]:
            line += 1
            acc = acc+parm if cmd == "acc" else acc
        else: #jmp
            next_line = line + parm
            #if next line is already in he history, we have a loop identified
            is_looping = next_line in line_history
            if is_looping:
                break
            line = next_line
            line_history.append(line)
    return is_looping, acc


def main():
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, "input_day8.txt"), encoding="utf-8") as input:
        code = input.readlines()
    code = [[cmd_list[0], int(cmd_list[1])] for cmd_list in [line.rstrip().split(" ") for line in code]]
    
    
    #part 1
    _, result_part1 = execute(code)
    print(f"{result_part1} is the acc before loop starts again.")
    
    #part 2
    was_a_loop = True
    result_part2 = None
    for i in range(len(code)):
        #modify the code and execute it. See if it loops or if it ends. 
        cmd = code[i][0]
        if cmd in ["nop", "jmp"]:
            code[i][0] = "nop" if cmd == "jmp" else "jmp"
            was_a_loop, result_part2 = execute(code)
            code[i][0] = cmd           
        if not was_a_loop:
            #print(f"fix line {i} from {code[i]}")
            break
    print(f"{result_part2} is the acc after fixing the loop.")

main()
