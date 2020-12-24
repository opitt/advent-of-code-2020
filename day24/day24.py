import os
from copy import deepcopy

# Here, tiles immediately adjacent means the six tiles directly touching the tile in question.
# draw a coordinate system with hexagons. Each hexagons centerpoint has a unique on (x,y) position
steps_xy = {"e": (2, 0),
         "w": (-2, 0),
        "ne": (1, 1),
        "se": (1, -1),
        "nw": (-1, 1),
        "sw": (-1, -1),
}

def get_neighbour(tilepos, direction):
    return (tilepos[0] + steps_xy[direction][0],
            tilepos[1] + steps_xy[direction][1])

def get_all_neighbours(tilepos):
    return [get_neighbour(tilepos, direction) for direction in steps_xy.keys()]

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

def count_adjacent_black(fp, tilepos):
    return sum([is_black(fp, tile) for tile in get_all_neighbours(tilepos)])

def next_direction(directions):
    #sesenwnenenewseeswwswswwnenewsewsw
    next_dir = directions[:2]
    return (next_dir, directions[2:]) if next_dir in ["se", "sw", "ne", "nw"] else (directions[0], directions[1:])
    
def calc_tilepos(tilepath):
    tilepos = (0,0)
    while tilepath:
        next_dir, tilepath = next_direction(tilepath)
        tilepos = get_neighbour(tilepos, next_dir)
    return tilepos

def main():
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, f"input_day24.txt"), encoding="utf-8") as input:
    #with open(os.path.join(script_path, f"test.txt"), encoding="utf-8") as input:
        tilepaths = input.read().splitlines()
    
    # floorplan only contains black tiles, I dont store white tiles 
    floorplan_blacktiles = {}  # (x,y): True 
    
    ########### PART 1 #############
    for tilepath in tilepaths:
        tilepos = calc_tilepos(tilepath)
        flip_tile(floorplan_blacktiles, tilepos)

    result = sum(floorplan_blacktiles.values())
    print(f"Black tiles: {result}")

    ########### PART 2 #############
    fp_next = deepcopy(floorplan_blacktiles)
    for day in range(1, 101):
        for blacktile in floorplan_blacktiles.keys():
            # BLACK
            black = count_adjacent_black(floorplan_blacktiles, blacktile)
            if black == 0 or black > 2:
                #Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
                set_tile_white(fp_next, blacktile)
            # WHITE
            neighbours = get_all_neighbours(blacktile)
            for neighbour in neighbours:
                if not is_black(floorplan_blacktiles, neighbour):
                    black = count_adjacent_black(floorplan_blacktiles, neighbour)
                    #Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.
                    if black == 2:
                        set_tile_black(fp_next, neighbour)
        floorplan_blacktiles = deepcopy(fp_next)
        result = sum(floorplan_blacktiles.values())
        print(f"Day {day}: {result}") #3636


main()
