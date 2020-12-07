# https://adventofcode.com/2020/day/7

import os

def main():
    
    def can_contain(bag, bag_of_color):
        #part1 function
        if bag_rules.get(bag, {}).get(bag_of_color, False):
            #found the bag_of_color directly, no need to go deeper inside other bags
            return 1
        for valid_bag_inside in bag_rules.get(bag,{}):
            found = can_contain(valid_bag_inside, bag_of_color)
            if found:
                return 1
        return 0

    def count_bags_inside(check_bag):
        #part2 function
        #for the  bag to check, look up, which bags it includes and how many
        #for each of the bags count how many bags they contain
        result = 0
        for bag, cnt in bag_rules.get(check_bag, {}).items():
            result += cnt + cnt*count_bags_inside(bag)
        return result

    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, "input_day7.txt"), encoding="utf-8") as input:
        rules = input.readlines()
    bag_rules = {}
    # BUILD DICTIONARY
    # example: "posh violet bags contain 2 dark violet bags, 4 striped olive bags, 1 pale silver bag."
    for rule in rules:
        s = rule.split(" contain ")
        #bag color as key for dict
        bag_key = s[0].replace(" bags","")
        bag_rules[bag_key] = {}
        #the bags with their count as dict for the values
        for bag_rule in s[1].split(", "):
            #2 dark violet bags
            el = bag_rule.split(" ")
            bag_count = 0 if el[0] == "no" else int(el[0]) #no other bag ...
            bag_color = " ".join(el[1:-1])
            bag_rules[bag_key][bag_color] = bag_count
        
    #CALCULATE 
    my_bag_color = "shiny gold"
    result_part1 = sum(list( can_contain(bag, my_bag_color) for bag in bag_rules.keys()))
        
    #FINISH
    print(f"{result_part1} bag colors can eventually contain at least one shiny gold bag.")

    result_part2 = count_bags_inside(my_bag_color)
    print(f"{result_part2} individual bags are required inside the single shiny gold bag.")

main()
