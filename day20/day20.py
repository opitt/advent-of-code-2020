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
        # find a tile in all other tiles, that matches to the side
        matches = [tile_name for tile_name, sides in t_sides.items() if tile_name != tile and side in sides]
        if len(matches) > 1:
            raise RuntimeWarning
        return "" if len(matches) == 0 else matches[0]

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

    #! ################ PART 2 #################
    t_match_t = {} # tiles and what tiles they match with
    for tile, matches in t_match.items():
        t_match_t[tile] = list(set(matches.values()))
    
    def get_tile_with_x(tile,x):
        for connected_tile in t_match_t[tile].values():
            if len(t_match_t[connected_tile].values()) == x:
                return connected_tile
        return None

    def find_tile_matching(criteria):
        # criteria ["1212","",""] means
        # find a tile, that has 3 connections and one of them is 1212
        for tile, connected_tiles in t_match_t.items():
            #  "2381": ['1543', '2837', '3761']
            if len(connected_tiles) == len(criteria):
                check = [c for c in criteria if c != ""]
                s = sum([crit in connected_tiles for crit in check])
                if s == len(check):
                    return tile
        return None

    image_tiles = [[]]
    for y in range(12):
        for x in range(12):
            image_tiles[y].append("")
        image_tiles.append([])

    for y in range(12):
        for x in range(12):
            criteria = [] # what tile to look for
            if x-1 >= 0:
                criteria.append(image_tiles[y][x - 1]) # need to connect with x-1 tile
            if y - 1 >= 0:
                criteria.append(image_tiles[y - 1][x]) # need to connect with y-1 tile
            if x + 1 < 12:
                criteria.append(image_tiles[y][x + 1]) # need to connect with x+1 tile
            if y + 1 < 12:
                criteria.append(image_tiles[y + 1][x])
            next_tile = find_tile_matching(criteria)
            image_tiles[y][x] = next_tile
            for tile in criteria:
                if tile != "":
                    # remove connection wit me from the other tile
                    t_match_t[tile].remove(next_tile)
                    t_match_t[tile].append("")
                    # remove the connection to other tile from myself
                    t_match_t[next_tile].remove(tile)
                    t_match_t[next_tile].append("")        
    


    #TODO rotate/flip the tiles, so they match to their neighbours
    def rotate_tile90(tile):
        rotated = ["".join(l) for l in list(map(list,zip(*reversed(tile))))] 
        return rotated

    def flip_tile(tile, leftright = True):
        if leftright:
            flipped = ["".join(reversed(l)) for l in tile]
        else:
            flipped = [l for l in reversed(tile)] 
        return flipped

    def print_image():
        for y in range(2):
            zipped = list(map(list, zip(*image[y][:2])))
            for z in zipped:
                print("".join(z))

    def side_match_tiles(tile1, tile2, where):
        #where: 0 - top, 1 - right, 2 - bottom, 3 - left
        if where == 0:
            return tile1[0] == tile2[-1]
        if where == 2:
            return tile1[-1] == tile2[0]
        if where == 1:
            t1 = ["".join(l) for l in list(map(list, zip(*tile1)))][-1]
            t2 = ["".join(l) for l in list(map(list, zip(*tile2)))][0]
            return t1 == t2
        if where == 3:
            t1 = ["".join(l) for l in list(map(list, zip(*tile1)))][0]
            t2 = ["".join(l) for l in list(map(list, zip(*tile2)))][-1]
            return t1 == t2
        raise RuntimeWarning
            

    image = deepcopy(image_tiles)
    for y in range(12):
        for x in range(12):
            image[y][x] = tiles[image_tiles[y][x]]
    #TODO it sees, that this logic does not work. 
    #TODO maybe the whole logic is wrong?
    for y in range(12):
        for x in range(11):
            if y > 0 and x == 0:
                #first tile in a row needs to match above tile
                while True:
                    # try to change the tile
                    match = side_match_tiles(image[y][x], image[y-1][x], where=0)
                    if match:
                        break
                    image[y][x] = rotate_tile90(image[y][x])
                    match = side_match_tiles(image[y][x], image[y-1][x], where=0)
                    if match:
                        break
                    image[y][x] = flip_tile(image[y][x],leftright=True)
                    match = side_match_tiles(image[y][x], image[y-1][x], where=0)
                    if match:
                        break
                    image[y][x] = flip_tile(image[y][x], leftright=True)
            else:
                while True:
                    # try to change the next tile
                    match = side_match_tiles(image[y][x], image[y][x+1], where=1)
                    if match:
                        break
                    image[y][x+1] = rotate_tile90(image[y][x + 1])
                    match = side_match_tiles(image[y][x], image[y][x+1], where=1)
                    if match:
                        break
                    image[y][x + 1] = flip_tile(image[y][x + 1],leftright=False)
                    match = side_match_tiles(image[y][x], image[y][x+1], where=1)
                    if match:
                        break
                    image[y][x + 1] = flip_tile(image[y][x + 1], leftright=False)
            pass
                
            
    
    #TODO TEST MY FUNCTIONS
    #print("\norg\n", "\n".join(image[0][0]), sep="")
    #print("\nrot\n", "\n".join(rotate_tile90(image[0][0])), sep="")
    #print("\nflip\n", "\n".join(flip_tile(image[0][0], leftright=True)), sep="")
    #print("\nflip\n", "\n".join(flip_tile(image[0][0], leftright=False)), sep="")
    #print(side_match_tiles(image[0][0], image[0][1], where=1) )
    #print_image()

    pass

main(20)
