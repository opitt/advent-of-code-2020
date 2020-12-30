from collections import deque

def part1():
    # solution with a list and rotate
    # not scalable!

    cups = list(map(int, "186524973"))
    min_cup = min(cups)
    max_cup = max(cups)
    max_idx = len(cups)-1
    cups = deque(cups)

    cur = cups[0]
    for i in range(100):
        # The crab picks up the three cups that are immediately clockwise of the current cup. They are removed from the circle; 
        # cup spacing is adjusted as necessary to maintain the circle.
        cur = cups[0] # keep the current cup always at position 0
        cups.rotate(-1)
        pickup = [cups.popleft()]
        pickup.append(cups.popleft())
        pickup.append(cups.popleft())
        cups.rotate(1)
        # The crab selects a destination cup: the cup with a label equal 
        # to the current cup's label minus one. 
        dest = cur - 1 
        # If this would select one of the cups that was just picked up, 
        # the crab will keep subtracting one
        # until it finds a cup that wasn't just picked up. 
        if dest < min_cup:
            dest = max_cup
        while dest in pickup and cur >= min_cup:
            dest -= 1
            # If at any point in this process the value goes below the lowest value on any cup's label, 
            # it wraps around to the highest value on any cup's label instead.
            if dest < min_cup:
                dest = max_cup
        # The crab places the cups it just picked up so that they are immediately clockwise of the destination cup. 
        # They keep the same order as when they were picked up.

        dest_idx = cups.index(dest) # where is the destination?
        cups.rotate(-dest_idx-1)    # move destination to the end of the cups
        cups.extendleft(reversed(pickup)) # append the pickup on the left side (reversed necessary)

        # The crab selects a new current cup: the cup which is immediately clockwise of the current cup.
        cur_idx = cups.index(cur) + 1 # get the position of the current cup, and take the next position
        if cur_idx > max_idx:
            cur_idx = 0
        else:
            cups.rotate(-cur_idx) # bring the current cup to position 0

    idx1 = cups.index(1) # find the number 1
    cups.rotate(-idx1)   # move it to position 0
    cups.popleft()       # and remove it
    print("".join(map(str, list(cups))))  # joint the rest into result string
    #45983627

def part2():
    # solution with dict 
    # scalable!

    min_cup = 1
    max_cup = 1000*1000 # one million
    cups = {1: 8,
            8: 6,
            6: 5,
            5: 2,
            2: 4,
            4: 9,
            9: 7,
            7: 3,
            3: 10
            } # the starting point
    cups = cups | {i: i + 1 for i in range(10, max_cup + 1)}
    cups[max_cup] = min_cup  #the last cup connects to the first cup
    
    cur = 1
    for _ in range(10*max_cup):
        # The crab picks up the three cups that are immediately clockwise of the current cup. They are removed from the circle; 
        # cup spacing is adjusted as necessary to maintain the circle.
        pickup = cups[cur]
        pickedup = [pickup, cups[pickup], cups[cups[pickup]] ] # cups picked up
        cups[cur] = cups[cups[cups[pickup]]]  # the next three cups are removed, the fourth is now connected to cur
        # The crab selects a destination cup: the cup with a label equal 
        # to the current cup's label minus one. 
        dest = cur - 1 
        # If this would select one of the cups that was just picked up, 
        # the crab will keep subtracting one
        # until it finds a cup that wasn't just picked up. 
        if dest < min_cup:
            dest = max_cup
        while dest in pickedup and cur >= min_cup:
            dest -= 1
            # If at any point in this process the value goes below the lowest value on any cup's label, 
            # it wraps around to the highest value on any cup's label instead.
            if dest < min_cup:
                dest = max_cup
        # The crab places the cups it just picked up so that they are immediately clockwise of the destination cup. 
        # They keep the same order as when they were picked up.
        #print(f"destination: {dest}")
        cups[pickedup[-1]] = cups[dest]
        cups[dest] = pickedup[0]
        # The crab selects a new current cup: the cup which is immediately clockwise of the current cup.
        cur = cups[cur]

    #result = ""
    #cur = 1
    #while cups[cur] != 1:
    #    result += str(cups[cur])
    #    cur = cups[cur]
    #print(result)

    result = cups[1] * cups[cups[1]]
    print(result)    # 111080192688

part1()

part2()
