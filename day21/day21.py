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
    # My first idea: take a food with only one allergene - since only those ingredients can have that allergene; 
    # if the allergene then shows up in another food, with different ingredients, 
    # it could only be the earlier found ones...but that is only partly true.
    # What if a new ingredient also includes the same allergene? Now I have two ingredients with soy...
    # ==> In the end I got a tip - keep the ingredients, 
    # that show up in all food with the same allergene.Those are then the candidates to contain the allergen.)
    
    # READ FILE
    al_ing_candidates = {}  # allergens possibly contained in: ingredients
    ings = set()  # all ingrediens
    ings_cnt = defaultdict(int) # count ingredients across all food
    for food in food_list:
        food_ings = set(food.split(" (contains ")[0].split(" "))
        for ing in food_ings:
            ings_cnt[ing] += 1
        ings = ings.union(food_ings)  # ab = a | b
    
        food_al = food.split(" (contains ")[1].split(", ")
        for allergen in food_al:
            if al_ing_candidates.get(allergen, None) == None:
                # the ingredients are marked with the allergen, not clear which ingredient contains it though
                al_ing_candidates[allergen] = food_ings
            else:
                #! THIS IS THE CRITICAL LOGIC
                al_ing_candidates[allergen] = al_ing_candidates[allergen].intersection(food_ings)
    
    # find the ingredients, which are not candidate for allergens
    ing_without_al = deepcopy(ings)
    for ing in al_ing_candidates.values():
        ing_without_al = ing_without_al.difference(ing) # a - b
    result = sum([cnt for ing, cnt in ings_cnt.items() if ing in ing_without_al])
    print(f"Dangerous ingredients show up in food: {result} times.") #

    #! ################ PART 2 #################
    while len(al_ing_candidates) != sum([len(v) for v in al_ing_candidates.values()]):
        for ing in [ v for k, v in al_ing_candidates.items() if len(v) == 1]:
            for al2, ing2 in [ (k, v) for k, v in al_ing_candidates.items() if len(v) > 1]:
                al_ing_candidates[al2] = al_ing_candidates[al2] - ing
    # Arrange the ingredients alphabetically by their allergen and separate them by commas 
    # to produce your canonical dangerous ingredient list.
    # In the above example, this would be: mxmxvkd,sqjhc,fvjkl
    al_ing_candidates = {k: list(v)[0] for k, v in al_ing_candidates.items()}
    #print(sorted(al_ing.items(), key=lambda item: item[0]))
    result = ",".join([v for k, v in sorted(al_ing_candidates.items(), key=lambda item:item[0])])
    print(f"canonical dangerous ingredient list: {result}")
    #print(sorted(al_ing.items(), key=lambda k,v: list(v)[0]))
    pass

main(21)
