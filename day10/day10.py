# https://adventofcode.com/2020/day/10

import os


def main(day):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, f"input_day{day}.txt"), encoding="utf-8") as input:
        adapters = input.readlines()
    adapters = sorted([int(n.rstrip()) for n in adapters])
    
    #part 1
    #differences between the charging outlet, the adapters, and your device
    jolt_diffs={1:0, 2:0, 3:0} #
    chain = [0]  # the outlet
    while True:
        #check, which adapters fit into the connected adapter
        if chain[-1] + 1 in adapters:
            adapters.remove(chain[-1] + 1)
            chain.append(chain[-1] + 1)
            jolt_diffs[1] += 1      #this covers the outlot to first adapter caseas well: 0 -> 1
        elif chain[-1] + 2 in adapters:
            adapters.remove(chain[-1] + 2)
            chain.append(chain[-1] + 2)
            jolt_diffs[2] +=1
        elif chain[-1] + 3 in adapters:
            adapters.remove(chain[-1] + 3)
            chain.append(chain[-1] + 3)
            jolt_diffs[3] +=1
        else:
            #no adapter can be connected
            print("No adapter fits left")
            jolt_diffs[3] +=1       #this covers the adapter -> device case: +3
            break

    result_part1=jolt_diffs[1]*jolt_diffs[3]
    print(f"{result_part1} solution part 1.")
    
    #part 2
    result_part2 = 0
    print(f"{result_part2} solution part 2.")

main(10)
