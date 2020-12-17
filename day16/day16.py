# https://adventofcode.com/2020/day/16

import os

def main(day):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, f"input_day{day}.txt"), encoding="utf-8") as input:
    #with open(os.path.join(script_path, f"test.txt"), encoding="utf-8") as input:
        notes = input.read().split("\n\n")  #.splitlines()
    
    field_rules = {}
    for lines in notes[0].split("\n"):
        line_parts = lines.split(": ")
        field_rules[line_parts[0]] = []
        minmax_parts = line_parts[1].split(" or ")
        field_rules[line_parts[0]].append( ( int(minmax_parts[0].split("-")[0]), int(minmax_parts[0].split("-")[1])) ) #first range
        field_rules[line_parts[0]].append( ( int(minmax_parts[1].split("-")[0]), int(minmax_parts[1].split("-")[1])) ) #second range
        
    my_ticket = [int(v) for v in notes[1].split("\n")[1].split(",") if v != ""]
    tickets = [[int(v) for v in val.split(",") if v != ""] for val in notes[2].split("\n")[1:] if val != ""]
    
    #! PART 1
    #!
    def valid_value(num):
        # {"class": [(49, 525), (543, 953)], ...}
        inrange = lambda x, y: num >= x and num <= y
        for ranges in field_rules.values():
            if inrange(*ranges[0]) or inrange(*ranges[1]):
                return True
        return False

    # [271, 852, 52, 65, 945, 625, 634, 484, 147, 842, 880, 521, 416, 893, ...]
    invalid_tickets = []
    invalid_sum = 0
    for idx, ticket in enumerate(tickets):
        for num in ticket:
            if not valid_value(num):
                invalid_sum += num
                invalid_tickets.append(idx)
    
    print(invalid_sum)  #19240
    
    #! part 2    
    #! 
    # remove invalid tickets from tickets
    tickets = [ticket for idx, ticket in enumerate(tickets) if idx not in invalid_tickets]
    #tickets.append(my_ticket)
    # bring the same fields of all tickets together
    fields = [list(z) for z in zip(*tickets)]
    fields_name = [set() for _ in range(len(fields))]
    # no find the fields, that match all numbers
    for field_no, nums in enumerate(fields):
        # test each field range on all fields from all tickets 
        for field_name, field_range in field_rules.items():
            # lists field values across all tickets - one list = one field
            valid = True
            for n in nums:
                # all values for one field (across all tickets)
                if n >= field_range[0][0] and n <= field_range[0][1] or n >= field_range[1][0] and n <= field_range[1][1]:
                    continue
                else:
                    valid = False
                    break
            if valid:
                fields_name[field_no].add(field_name)

    l = len(fields_name)
    while True:
        removed = False
        for i in range(l):
            if len(fields_name[i]) == 1:
                for j in range(l):
                    if i == j:
                        continue
                    if fields_name[i].issubset(fields_name[j]):  # remove the single, if it is included
                        removed = True
                        fields_name[j] -= fields_name[i]
        if removed == False:
            break 
    
    result = 1
    for idx, name in enumerate(fields_name):
        if list(name)[0].startswith("departure"):
             result *= my_ticket[idx]
    print (result)
                
            


main(16)
