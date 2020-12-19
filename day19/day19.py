# https://adventofcode.com/2020/day/19

import os
import re

def main(day):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    #with open(os.path.join(script_path, f"input_day{day}.txt"), encoding="utf-8") as input:
    #with open(os.path.join(script_path, f"test.txt"), encoding="utf-8") as input:
    with open(os.path.join(script_path, f"test2.txt"), encoding="utf-8") as input:
        rules_msgs = input.read().split("\n\n")  #.splitlines()
    
    '''
    0: 4 1 5
    1: 2 3 | 3 2
    2: 4 4 | 5 5
    3: 4 5 | 5 4
    4: "a"
    5: "b"
    '''
    rules = {}
    for line in rules_msgs[0].splitlines():
        k, v = line.split(": ")[0], line.split(": ")[1]
        v = v.replace('"', '')  # skip the " chars for a or b values
        if "|" in v:
            v = "( " + v + " )"
        rules[k] = " " + v + " "
    
    messages = rules_msgs[1].splitlines()

    #! PART 1
    #!

    def build_regex():
        regex = rules['0']
        while re.search(r"\d", regex) != None:
            # 2 3 | 3 2
            new_regex = ""
            for c in regex.split(" "):
                new_regex += rules.get(c, c) # replace with rule or keep the org value
            regex = new_regex
        regex = regex.replace(" ", "")
        return "^" + regex + "$"

    result = 0
    regex = build_regex()
    for message in messages:
        result += re.fullmatch(regex, message) != None

    print(result)  #
    
    #! part 2    
    #! 
    result = 0
    print (result)
                
            
main(19)


