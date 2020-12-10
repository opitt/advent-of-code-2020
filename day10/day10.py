# https://adventofcode.com/2020/day/10

import os

def main(day):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, f"input_day{day}.txt"), encoding="utf-8") as input:
#    with open(os.path.join(script_path, f"test.txt"), encoding="utf-8") as input:
        adapters = input.readlines()
    adapters = sorted([int(n.rstrip()) for n in adapters])
    
    #PART 1
    #calculate the joltage difference between the adapters
    jolt_diffs = [adapter[1] - adapter[0] for adapter in zip(adapters[:-1], adapters[1:])]
    jolt_diffs.append(adapters[0] - 0) #add the difference between outlet (0) and the first adapter
    jolt_diffs.append(3) #add the difference between the last adapter and the device
    jolt_diffs_count = {dif: jolt_diffs.count(dif) for dif in range(1, 4)}

    result_part1 = jolt_diffs_count[1]*jolt_diffs_count[3]
    print(f"The number of 1-jolt differences multiplied by the number of 3-jolt differences is {result_part1}.") #2470
    
    #part 2
    def combine(adapter_chain):
        # e.g. [23] or [23, 24] or [23,24,25,26,27] 
        gap = max(0,len(adapter_chain) - 2) # the first and the last stay in place!
        # find all possible binary combinations for the gap
        #valid combinations have not more than 3 zeros i.e. not more than 3 jolts difference 
        valid_combos = sum([f"{b:>0{gap}b}".find("000") == -1 for b in range(2**gap)])
        return valid_combos

    # idea: split the set of adapters in groups
    # [1,2,3,6,7,8,9,12,15,16]
    # split criteria: a joltage gap of 3
    # [1,2,3]---[6,7,8,9]---[12]---[15,16]
    # the first and the last adapter in such a group needs to stay in position (otherwise the criteria of a max gap 3 is broken)
    # so we only need to find valid combinations within the first and last adapter in a group
    # valid combinations: binary counting: 00 01 10 00 ... all combinations that contain more than 3 zeros in the binary string violate the max gap 3 rule and are not valid 
    group = [0]  #add the outlet to the first group
    result_part2, combos = 1, 0
    #print(adapters2)
    for i in range(len(adapters)):
        #does the adapter has a gap of 1?
        if group[-1] + 1 == adapters[i]:
            # attach the adapter
            group.append(adapters[i])
            if i == len(adapters) - 1:
                #this adapter is the last one, need to asses the last group
                combos = combine(group)
                result_part2 *= combos
                group = [adapters[i]] # start a new group
        else:
            # gap is bigger than 1, find combinations for the group and start a new group 
            combos = combine(group)
            result_part2 *= combos
            group = [adapters[i]]
        
    print(f"The total number of distinct ways you can arrange the adapters to connect the charging outlet to your device is {result_part2}.") #1973822685184

main(10)
