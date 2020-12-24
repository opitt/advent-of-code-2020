import os

def next_tile(tilepos,direction):
    xy_steps = {"n": (0, 1),
                "s": (0, -1),
                "e": (2, 0),
                "w": (-2, 0),
                "ne": (1, 1),
                "se": (1, -1),
                "nw": (-1, 1),
                "sw": (-1, -1),
    }
    return (tilepos[0] + xy_steps[direction][0], tilepos[1] + xy_steps[direction][1])

def next_direction(tilepath):
    #sesenwnenenewseeswwswswwnenewsewsw
    direction = tilepath[:2]
    if direction in ["se", "sw", "ne", "nw"]:        
        return direction, tilepath[2:]
    return tilepath[0], tilepath[1:]
    
def get_tilepos(tilepath):
    tilepos = (0,0)
    while tilepath:
        step, tilepath = next_direction(tilepath)
        print(tilepos, step)
        tilepos = next_tile(tilepos, step)
    print(tilepos)
    return tilepos

def main():
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, f"input_day24.txt"), encoding="utf-8") as input:
        tilepaths = input.read().splitlines()

    floorplan = {}
    for tilepath in tilepaths:
        tilepos = get_tilepos(tilepath)
        tilecolor_black = floorplan.get(tilepos, None)
        if tilecolor_black == None:
            # first time flipped. default: white, flip to black
            floorplan[tilepos] = True # means black
        else:
            floorplan[tilepos] = not tilecolor_black  # flip

    result = sum(floorplan.values())
    print(f"Black tiles: {result}")

main()
