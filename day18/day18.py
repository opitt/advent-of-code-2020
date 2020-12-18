# https://adventofcode.com/2020/day/18
from functools import reduce
import os

def main(day):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, f"input_day{day}.txt"), encoding="utf-8") as input:
    #with open(os.path.join(script_path, f"test.txt"), encoding="utf-8") as input:
        calculations = input.read().splitlines()
    
    def calculate(e):
        #e.g. (4 * (5 + 9 + 8) + 7) * 6    
        #find parenthesis and recursively calculate the expression
        while "(" in e:
            p1, p2  = e.rfind("("), e.find(")", p1)
            val = calculate(e[p1+1:p2])
            #replace the parenthesis with the calculated value
            e = e[:p1] + str(val) + e[p2+1:]
        
        # now only numbers and + and * are in the string, separated by space
        ops = e.split(" ")
        result, ops = int(ops[0]), ops[1:] 
        while len(ops):
            if ops[0] == "+":
                result += int(ops[1])
            else:
                result *= int(ops[1])
            ops = ops[2:]
        return result

    def calculate2(e):
        #e.g. (4 * (5 + 9 + 8) + 7) * 6    
        while "(" in e:
            p1, p2 = e.rfind("("), e.find(")", p1)
            val = calculate2(e[p1+1:p2])
            e = e[:p1] + str(val) + e[p2+1:]

        # split by * to calculated first the + operations
        ops = e.split(" * ")
        for i, op in enumerate(ops):
            ops[i] = sum([int(o) for o in op.split(" + ")])
        # multiply the result
        result = reduce(lambda x,y: x*y, ops)
        return result

    #! PART 1
    #!
    result = 0
    for expression in calculations:
        result += calculate(expression)
    print(result)

    #! PART 2
    #!
    result = 0
    for expression in calculations:
        #expression = "1 + 2 * 3 + 4 * 5 + 6"  #231
        #expression = "1 + (2 * 3) + (4 * (5 + 6))"
        #expression = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"
        result += calculate2(expression)
    print(result)

main(18)
