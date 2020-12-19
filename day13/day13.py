# https://adventofcode.com/2020/day/13

import os

def main(day):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, f"input_day{day}.txt"), encoding="utf-8") as input:
        notes = input.read().splitlines()
    # ***** test cases
    #notes = ["0", "17,x,13,19"] #The earliest timestamp that matches the list 17,x,13,19 is 3417.
    #notes = ["0", "67,x,7,59,61"] #first occurs at timestamp 779210.
    #notes = ["0", "1789,37,47,1889"] #first occurs at timestamp 1202161486.
    # *************************
    buses = [int(bus) for bus in notes[1].split(",") if bus != "x"]
    buses_sorted = sorted([int(bus) for bus in notes[1].split(",") if bus != "x"])
    bus_offset = {bus: [*notes[1].split(",")].index(str(bus)) for bus in buses_sorted}

    #! PART 1
    #!
    wished_start = int(notes[0])
    print("\n############### PART 1 #############")
    bus_stops_before = [(bus, wished_start - wished_start % bus) for bus in buses_sorted]
    bus_stops_after = [(bus, stop + bus) for (bus,stop) in bus_stops_before]
    next_arrivals = sorted(bus_stops_after, key=lambda stop: stop[1])
    waiting_time = next_arrivals[0][1] - wished_start
    next_bus = next_arrivals[0][0]

    #print(bus_stops_before)
    #print(bus_stops_after)       
    #print(next_arrivals)

    result_part1 = waiting_time * next_bus
    print(f"Part 1: Your wished departure: {wished_start}. Next bus {next_bus} arrives in {waiting_time} min. Solution: {result_part1}") #2935
    
    #! PART 2 starts here
    #!
    bus_max = buses_sorted[-1]
    t = 200000000000000 // bus_max
    t = t * bus_max - bus_offset[bus_max]
    
    #chek = [(bus, offset) for bus, offset in bus_offset.items() if bus != bus_max]
    #while sum([(t + offset) % bus for bus, offset in chek]) != 0:
        #next_arrival = next_arrivals_fct(buses, t)
        #for bus, offset in bus_offset[:-1].items(): # the last one is already valid, as we add it to the star t
        #    valid_t &= (t + offset ) % bus == 0  #
        #if valid_t:
        #    break
    #    t += bus_max

    t_matches = 1
    while True:
        if t % buses_sorted[-1 * t_matches] == 0:
            t_matches = 0
    diff = t - t_match
    if t
        t_matches += 1
    t += diff


    result_part2 = t
    print(f"Part 2: start time is: {result_part2}") #


main(13)
