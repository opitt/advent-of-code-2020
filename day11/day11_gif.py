# extends https://adventofcode.com/2020/day/11
# visualisation of simulated seating
# creates an animated gif for all ascii stored simulation results

import os
from PIL import Image


def load_file_to_list(file_name):
    # READ INPUT FILE
    with open(file_name, mode="r", encoding="utf-8") as input:
        plan = input.readlines()
    plan = [row.rstrip() for row in plan]
    return plan

def load_next_file_gen(srcpath):
    # a generator functions, that scans files in a folder and returns their content and file name
    # sorted by file name
    sorted_filenames = []
    with os.scandir(srcpath) as entries:
        for entry in entries:
            if entry.is_file() and entry.name.startswith("sim_") and entry.name.endswith(".txt"):
                sorted_filenames.append((os.path.join(srcpath, entry.name), entry.name.split(".")[0]))
    sorted_filenames = sorted(sorted_filenames, key=lambda s: s[1])
    for file_name in sorted_filenames:
        yield (load_file_to_list(file_name[0]), file_name[1])


def main():
    save_as_type = ".png" 
    EMPTY = "L"
    FULL = "#"    
    FLOOR = "."
    # color picker: https://coolors.co/002626-0e4749-95c623-e55812-efe7da
    pixel_colors = {FULL: (14, 71, 73),
                    FLOOR: (229, 88, 18),
                    EMPTY: (149,198,35)
                   }

    # source of the simulation text files
    script_path = os.path.dirname(os.path.realpath(__file__))
    sim_data_path = os.path.join(script_path, "sim_data")
    next_plan = load_next_file_gen(sim_data_path) # generator for all sim file names in the directory
    
    #LOAD files, color code the image and store the images
    img_list = []
    # load the first file
    plan, name = next(next_plan)
    width = len(plan[0])
    height = len(plan)
    while True:
        im = Image.new("RGB", (width, height), "#FFFFFF")
        pixels = im.load()
        for y in range(0, height):
            for x in range(0, width):
                pixels[x,y] = pixel_colors.get(plan[y][x],(255,0,0)) #putpixel((x,y), (color))
        #im.show()
        # store the generated image
        #im.save(os.path.join(sim_data_path, name + save_as_type))
        img_list.append(im)
        try:
            plan, name = next(next_plan)
        except StopIteration:
            break
    
    #duration
    #The display duration of each frame of the multiframe gif, in milliseconds. Pass a single integer for a constant duration, or a list or tuple to set the duration for each frame separately.
    im.save(os.path.join(sim_data_path, name + ".gif"),
        save_all=True, append_images=img_list, optimize=False, duration=50, loop=0)
    
    return

main()
