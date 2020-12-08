# https://adventofcode.com/2020/day/8

import os

def main():
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, "input_day8.txt"), encoding="utf-8") as input:
        code = input.readlines()
    
    def execute (code):
        line_history = []
        #nop, acc, jmp
        line = 0
        acc = 0
        was_a_loop = False
        last_line = len(code) - 1

        while line != last_line:
            s = code[line].split(" ")
            cmd, parm = s[0], s[1].rstrip()
            if cmd == "nop":
                line += 1
            elif cmd == "acc":
                line += 1
                acc += int(parm)
            else: #jmp
                next_line = line + int(parm)
                if next_line in line_history:
                    was_a_loop = True
                    break
                else:
                    line = next_line
                    line_history.append(line)

        return was_a_loop, acc
    
    #part 1
    _, result_part1 = execute(code)
    
    #part 2
    for i in range(len(code)):
        #modify the code and execute it. See if it loops or if it ends. 
        code_fixed = code.copy()
        if "nop" in code[i]:
            code_fixed[i] = code[i].replace("nop", "jmp")
        elif "jmp" in code[i]:
            code_fixed[i] = code[i].replace("jmp", "nop")
        else:
            continue
        was_a_loop, result_part2 = execute(code_fixed)
        if not was_a_loop:
            #print(f"fixed line {i} from {code[i]} to {code_fixed[i]}")
            break

    #FINISH
    print(f"{result_part1} is the acc before loop starts again.")
    print(f"{result_part2} is the acc after fixing the loop.")

main()
