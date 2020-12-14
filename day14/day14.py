# https://adventofcode.com/2020/day/14

import os

def main(day):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, f"input_day{day}.txt"), encoding="utf-8") as input:
    #with open(os.path.join(script_path, f"test.txt"), encoding="utf-8") as input:
        instructions = input.read().splitlines()

    # a block starts with a mask
    # the mask applies to all memory value settings
    blocks = []
    for line in instructions:
        fields = line.split(" = ")
        if fields[0] == "mask": # a mask starts a new block
            blocks.append([fields[1]]) # add the mask to the block
        else:
            m = fields[0].split("[") # memory address
            blocks[-1].append((int(m[1][:-1]), int(fields[1])))  # tupel (mem address, value)
    #print(blocks)

    #! PART 1
    # *> blocks = [['01111X0011X11110XX11X110111001X00001', (26252, 2785), (5529, 156), ...], ...]
    memory = {} # address: value
    for block in blocks:
        mask = block[0]
        for mem, val in [*block[1:]]: # tupel (mem, value)
            val_bin = f"{val:036b}"  # convert the value to a 36 digit binary
            # apply the rule: X -> keep the value bit; otherwise the mask value 0 or 1
            val_masked = "".join([v if m == "X" else m for m, v in [*zip(mask, val_bin)]])
            memory[mem] = int(val_masked,2) # convert the memory binary value to integer
            #print( "\n".join( ["*** mask, val, value masked", mask, val_bin, val_masked, str(int(val_masked, 2))]))

    #print(memory)
    result_part1 = sum([v for k, v in memory.items()])
    print(f"Part 1: The sum of all values left in memory after it completes is {result_part1}") #13496669152158
    
    #! PART 2 starts here
    #!
    # reuse blocks = 
    # *> [['01111X0011X11110XX11X110111001X00001', (26252, 2785), (5529, 156), ...], ...]

    memory = {} # address: [value]]

    for block in blocks:
        mask = block[0]
        for mem, val in [*block[1:]]:
            mem_bin = f"{mem:036b}" # convert the address to binary and apply the mask
            mem_msk = "".join([mem if msk == "0" else msk for msk, mem in [*zip(mask, mem_bin)]])
            #print("\n".join(["*** membin, mask, mem mask", mem_bin, mask, mem_msk]))
            # replace all X with versions 0 and 1
            floating_mem = [mem_msk] # start with the masked address
            for _ in range(mem_msk.count("X")): 
                #replace reach X with 0 and 1
                new_floating_mem = [] # temporary list, to store the 0 and 1 versions
                i = floating_mem[0].index("X")
                for mem in floating_mem: # replace all addresses with a 0 and 1 version 
                    m0 = mem[:i] + "0" + mem[i + 1:]
                    m1 = mem[:i] + "1" + mem[i + 1:]
                    #print("\n".join(["*** memory floating ...",mem, m0,m1]))
                    new_floating_mem.append(m0)
                    new_floating_mem.append(m1)
                floating_mem = new_floating_mem
            for m in floating_mem:
                memory[int(m,2)] = val

    result_part2 =  sum(memory.values())
    print(f"Part 2: The sum of all values left in memory after it completes is {result_part2}") #

main(14)
