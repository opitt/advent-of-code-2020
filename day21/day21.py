# https://adventofcode.com/2020/day/20

import os
from copy import deepcopy
from collections import defaultdict

def read_input(split_lines_by, day, test_file=False):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    if test_file:
        path = os.path.join(script_path, f"test.txt")
        #path = os.path.join(script_path, f"test2.txt")
    else:
        path = os.path.join(script_path, f"input_day{day}.txt")
    with open(path, encoding="utf-8") as input:
        if split_lines_by == "\n":
            input_list = input.read().splitlines()
        else:
            input_list = input.read().split(split_lines_by)
    return input_list

#!  ############ MAIN ###############
def main(day):
    # remove empty line at the end and remove the trailing ")"
    food_list = [ line.replace(")", "") for line in read_input("\n", day, test_file=False) if line != ""]

    #! ################# PART 1 #################
    # READ FILE
    al_ing = defaultdict(set)      # allergens: ingredients
    ings = set()  # all ingrediens
    ing_cnt = defaultdict(int)
    for f_idx, food in enumerate(food_list):
        ingredients = set(food.split(" (contains ")[0].split(" "))
        for ing in ingredients:
            ing_cnt[ing] += 1
        ings = ings.union(ingredients)  # ab = a | b
    
        allergens = food.split(" (contains ")[1].split(", ")
        for allergen in allergens:
            if al_ing.get(allergen, None) == None:
                al_ing[allergen] = ingredients
            else:
                al_ing[allergen] = al_ing[allergen].intersection(ingredients)
            
    ing_withno_a = deepcopy(ings)
    for ing in al_ing.values():
        ing_withno_a = ing_withno_a.difference(ing) # a - b
    
    result = sum([cnt for ing, cnt in ing_cnt.items() if ing in ing_withno_a])
    print(f"Result {result}") #

    #! ################ PART 2 #################
       
    pass

main(21)
