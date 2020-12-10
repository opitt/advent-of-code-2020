# https://adventofcode.com/2020/day/10

import os
import copy

def main(day):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, f"input_day{day}.txt"), encoding="utf-8") as input:
#    with open(os.path.join(script_path, f"test.txt"), encoding="utf-8") as input:
        adapters = input.readlines()
    adapters = sorted([int(n.rstrip()) for n in adapters])
    adapters2 = copy.deepcopy(adapters)
    
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
    def combine(adapter_chain):
        print(adapter_chain)
        l = len(adapter_chain)
        #could be more than 5!
        # [23] or [23, 24] 
        if l == 1 or l==2:
            return 1
        gap = l - 2
        valid_combo = 0
        for possible in range(2**gap):
            bin_opt = f"{possible:>0{gap}b}"
            valid_combo += bin_opt.find("000") == -1 #check if the gap is bigger than 3 jolts 
            #print (bin_opt, bin_opt.find("000"))
        return valid_combo

    jolt3splits = [[0]]  #add the first outlet to the 
    result_part2, combos = 1, 0
    print(adapters2)
    for i in range(len(adapters2)): 
        if jolt3splits[-1][-1] + 1 == adapters2[i]:
            jolt3splits[-1].append(adapters2[i])
            if i == len(adapters2) - 1:
                combos = combine(jolt3splits[-1])
                print(combos)
                result_part2 *= combos
                jolt3splits.append([adapters2[i]])
        else:
            combos = combine(jolt3splits[-1])
            print(combos)
            result_part2 *= combos
            jolt3splits.append([adapters2[i]])
        
    19208
    2744

    #493455671296 too low
    print(f"{result_part2} solution part 2.")

main(10)
