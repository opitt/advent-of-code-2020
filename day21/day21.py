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
    al_ing = {}  # allergens possibly contained in: ingredients
    ings = set()  # all ingrediens
    ings_cnt = defaultdict(int) # count ingredients across all food
    for food in food_list:
        food_ings = set(food.split(" (contains ")[0].split(" "))
        for ing in food_ings:
            ings_cnt[ing] += 1
        ings = ings.union(food_ings)  # ab = a | b
    
        food_al = food.split(" (contains ")[1].split(", ")
        for allergen in food_al:
            if al_ing.get(allergen, None) == None:
                al_ing[allergen] = food_ings
            else:
                #! THIS IS THE CRITICAL LOGIC
                # soy: A B
                # soy: B C D
                # soy = B ... probably
                al_ing[allergen] = al_ing[allergen].intersection(food_ings)
            
    ing_without_al = deepcopy(ings)
    for ing in al_ing.values():
        ing_without_al = ing_without_al.difference(ing) # a - b
    
    result = sum([cnt for ing, cnt in ings_cnt.items() if ing in ing_without_al])
    print(f"Result {result}") #

    #! ################ PART 2 #################
       
    pass

main(21)
