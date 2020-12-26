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
    #TODO ------------------------------------------------------------------------- True for test file
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
                # the ingredients are marked with the allergen, not clear which ingredient contains it though
                al_ing[allergen] = food_ings
            else:
                #! THIS IS THE CRITICAL LOGIC
                # the ingredients are marked with the allergen
                # we found them in another food marked with the allergen already
                # we keep the ingredients, that are in all foods, marked with the allergen 
                al_ing[allergen] = al_ing[allergen].intersection(food_ings)
    
    ing_without_al = deepcopy(ings)
    for ing in al_ing.values():
        ing_without_al = ing_without_al.difference(ing) # a - b
    
    result = sum([cnt for ing, cnt in ings_cnt.items() if ing in ing_without_al])
    print(f"Dangerous ingredients show up in food: {result} times.") #

    #! ################ PART 2 #################
    #TODO figure out which ingredient contains which allergen
    #print(al_ing)
    while len(al_ing) != sum([len(v) for v in al_ing.values()]):
        for ing in [ v for k, v in al_ing.items() if len(v) == 1]:
            for al2, ing2 in [ (k, v) for k, v in al_ing.items() if len(v) > 1]:
                al_ing[al2] = al_ing[al2] - ing
    # Arrange the ingredients alphabetically by their allergen and separate them by commas 
    # to produce your canonical dangerous ingredient list.
    # In the above example, this would be: mxmxvkd,sqjhc,fvjkl
    al_ing = {k: list(v)[0] for k, v in al_ing.items()}
    #print(sorted(al_ing.items(), key=lambda item: item[0]))
    result = ",".join([v for k, v in sorted(al_ing.items(), key=lambda item:item[0])])
    print(f"canonical dangerous ingredient list: {result}")
    #print(sorted(al_ing.items(), key=lambda k,v: list(v)[0]))
    pass

main(21)
