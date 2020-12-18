# https://adventofcode.com/2020/day/18

import os

def main(day):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, f"input_day{day}.txt"), encoding="utf-8") as input:
    #with open(os.path.join(script_path, f"test.txt"), encoding="utf-8") as input:
        calculations = input.read().splitlines()
    
    def calculate(e):
        #e.g. (4 * (5 + 9 + 8) + 7) * 6    
        
        while "(" in e:
            p1 = e.rfind("(")
            p2 = e.find(")", p1)
            calc = e[p1+1:p2]
            val = calculate(calc)
            e = e[:p1] + str(val) + e[p2+1:]
        ops = e.split(" ")

        result = int(ops[0])
        ops = ops[1:] 
        while len(ops):
            if ops[0] == "+":
                result += int(ops[1])
            else:
                result *= int(ops[1])
            ops = ops[2:]
        return result
                

    #! PART 1
    #!
    result = 0
    for expression in calculations:
        result += calculate(expression)
    print(result)

main(18)
