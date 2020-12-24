import os
from copy import deepcopy

xy_go = {"e": (2, 0),
            "w": (-2, 0),
            "ne": (1, 1),
            "se": (1, -1),
            "nw": (-1, 1),
            "sw": (-1, -1),
}

def next_tile(tilepos, direction):
    return (tilepos[0] + xy_go[direction][0],
            tilepos[1] + xy_go[direction][1])

def get_neighbours(tilepos):
    return [next_tile(tilepos, direction) for direction in xy_go.keys()]

def is_black(fp, tilepos):
    return fp.get(tilepos, False) == True

def set_tile_white(fp, tilepos):
    if fp.get(tilepos, None) != None:
        del fp[tilepos] 

def set_tile_black(fp, tilepos):
    fp[tilepos] = True

def flip_tile(fp, tilepos):
    if is_black(fp, tilepos):
        set_tile_white(fp, tilepos)
    else:
        set_tile_black(fp,tilepos)

def count_black_adjacent(fp, tilepos):
    #TODO use comprehension
    black = 0
    for tile in get_neighbours(tilepos): 
        black += is_black(fp, tile)
    return black

def next_direction(tilepath):
    #sesenwnenenewseeswwswswwnenewsewsw
    direction = tilepath[:2]
    if direction in ["se", "sw", "ne", "nw"]:        
        return direction, tilepath[2:]
    return tilepath[0], tilepath[1:]
    
def calc_tilepos(tilepath):
    tilepos = (0,0)
    while tilepath:
        step, tilepath = next_direction(tilepath)
        #print(tilepos, step)
        tilepos = next_tile(tilepos, step)
    #print(tilepos)
    return tilepos

def main():
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, f"input_day24.txt"), encoding="utf-8") as input:
    #with open(os.path.join(script_path, f"test.txt"), encoding="utf-8") as input:
        tilepaths = input.read().splitlines()
    
    floorplan = {}
    for tilepath in tilepaths:
        tilepos = calc_tilepos(tilepath)
        flip_tile(floorplan, tilepos)

    result = sum(floorplan.values())
    print(f"Black tiles: {result}")

    #floorplan = {(0, 0): True,
    #             (1, 1): True,
    #            }
    result = sum(floorplan.values())
    print(f"Day 0: {result}")   
    #get_tile_neighbours_pos((0,0))
    # Every day, the tiles are all flipped according to the following rules:
    for day in range(1, 101):
        fp_next = deepcopy(floorplan)
        # floorplan only contains black tiles, since white tiles are not stored 
        # Here, tiles immediately adjacent means the six tiles directly touching the tile in question.
        for blacktile in floorplan.keys():
            # BLACK
            black = count_black_adjacent(floorplan, blacktile)
            if black == 0 or black > 2:
                #Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
                set_tile_white(fp_next, blacktile)
            # WHITE
            neighbours = get_neighbours(blacktile)
            for neighbour in neighbours:
                if not is_black(floorplan, neighbour):
                    black = count_black_adjacent(floorplan, neighbour)
                    #Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.
                    if black == 2:
                        set_tile_black(fp_next, neighbour)

        floorplan = deepcopy(fp_next)
        result = sum(floorplan.values())
        print(f"Day {day}: {result}")


main()
