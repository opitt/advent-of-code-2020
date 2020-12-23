from collections import deque

cups = list(map(int, "186524973"))
#cups = list(map(int, "389125467")) #test

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
    #print(f"-- move {i+1} --\n")
    #print(f"cups ({cur}) : {cups}")
    #print(f"pickup {pickup}")

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
    #print(f"destination: {dest}")

    
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
# Test: producing 92658374. If the crab were to complete all 100 moves, the order after cup 1 would be 67384529.
