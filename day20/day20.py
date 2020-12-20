# https://adventofcode.com/2020/day/20

import os
from copy import deepcopy

def read_input(split_lines_by, day, test_file=False):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    if test_file:
        #path = os.path.join(script_path, f"test.txt")
        path = os.path.join(script_path, f"test2.txt")
    else:
        path = os.path.join(script_path, f"input_day{day}.txt")
    with open(path, encoding="utf-8") as input:
        if split_lines_by == "\n":
            input_list = input.splitlines()
        else:
            input_list = input.read().split(split_lines_by)
    return input_list

#!  ############ MAIN ###############
def main(day):
    # remove empty line at the end
    tiles_file = [ line for line in read_input("\n\n", day, test_file=False) if line != ""]

    #! ################# PART 1 #################

    # READ FILE
    tiles = {}
    for line in tiles_file:
        title, tile = line.splitlines()[0].split(" ")[1][:-1], line.splitlines()[1:]
        tiles[title] = tile

    # BUILD TILES, all possible sides of a tile after rotating and flipping
    t_sides = {}
    for title, tile in tiles.items():
        image_rotate = ["".join(l) for l in list(map(list,zip(*tile)))] # get the sides lef/right
        s = [tile[0], image_rotate[-1], tile[-1], image_rotate[0]]
        s += ["".join(list(reversed(x))) for x in s]
        t_sides[title] = deepcopy(s)
        #  could convert the strings to binary and then to a number
        #  int( "#.#.".replace("#", "1").replace(".", "0"),2)

    def find_matching_tiles(tile, side):
        # find a tile in all other tilse, that matches to the side
        return [tile_name for tile_name, sides in t_sides.items() if tile_name != tile and side in sides]

    t_match = {}
    for title, tile in t_sides.items():
        t_match[title] = {}
        for side in tile:
            match_tiles = find_matching_tiles(title, side)
            if len(match_tiles) > 0: 
                t_match[title][side] = match_tiles

    result = 1
    for title, sides in t_match.items():
        if len(sides) == 4: # four means, two sides match in either way e.g. 1234 4321 and 5678 8765 
            print(title)
            result *= int(title)
    print(f"Result {result}") #17250897231301


main(20)
