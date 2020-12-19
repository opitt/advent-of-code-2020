# https://adventofcode.com/2020/day/19

import os
import re

def main(day):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, f"input_day{day}.txt"), encoding="utf-8") as input:
    #with open(os.path.join(script_path, f"test.txt"), encoding="utf-8") as input:
    #with open(os.path.join(script_path, f"test2.txt"), encoding="utf-8") as input:
        rules_msgs = input.read().split("\n\n")  #.splitlines()
    ''' example rules ...
    0: 4 1 5
    1: 2 3 | 3 2
    2: 4 4 | 5 5
    3: 4 5 | 5 4
    4: "a"
    5: "b"
    '''

    #! ################# PART 1 #################
    #!
    # building a rule dict 
    rules = {}
    for line in rules_msgs[0].splitlines():
        k, v = line.split(": ")[0], line.split(": ")[1]
        v = v.replace('"', '')  # skip the " chars for a or b values
        if "|" in v:
            # add parenthesis to the rules. Keep the space - otherwise I dont find the rule numbers
            v = "( " + v + " )"
        rules[k] = " " + v + " "   

    def build_regex1():
        # start with rule 0
        regex = rules['0']
        # as long as there are numbers that should be replaced ...
        while re.search(r"\d+ | \d+", regex) != None:
            # e.g. 2 3 | 3 2
            regex = "".join([rules.get(rule_num, rule_num) for rule_num in regex.split(" ")])
        regex = regex.replace(" ", "")
        return "^" + regex + "$"

    messages = rules_msgs[1].splitlines()
    regex = build_regex1()
    result = sum([re.fullmatch(regex, message) != None for message in messages])
    print(result) #208
    
    #! ########### part 2 ###########
    #! 
    rules = {}
    for line in rules_msgs[0].splitlines():
        k, v = line.split(": ")[0], line.split(": ")[1]
        if k == "8":
            #this is the org logic:      v = "42 | 42 8"
            v = "(?: 42 )+"  # this is the improved/simplified rule ( 
            # (?:xx) can be used for uncaptured groups -  helps testing at regex101 - and could be faster)
        elif k == "11":
            ## this is the org logic:    v = "42 31 | 42 11 31" 
            #v = "(?P<AA>(?: 42 )+)(?P<BB>(?: 31 )+)"
            v = "|".join([f"(?: 42 ){{{i}}}(?: 31 ){{{i}}}" for i in range(1, 11)])
            # works only until 10
        v = v.replace('"', '')  # skip the " chars for a or b values
        v = " (?: " + v + " ) "
        rules[k] = v

    def build_regex2():
        regex = rules['0']
        while re.search(r"\d+ | \d+", regex) != None:
            # replace with rule or keep the org value
            regex = "".join([rules.get(c, c) for c in regex.split(" ")])
        regex = regex.replace(" ", "") # removed all spaces
        return "^" + regex + "$" # match start and end of line, i.e. full match

    result = 0
    regex = build_regex2()
    #the regex can be simplified
    #while regex.find("(?:a)") >= 0 or regex.find("(?:b)") >= 0:
    #    regex = regex.replace("(?:a)", "a")
    #    regex = regex.replace("(?:b)", "b")
    for message in messages:
        match = re.fullmatch(regex, message)
        if match != None:
            result += 1
    print (result) #316

main(19)
