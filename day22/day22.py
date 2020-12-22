import os
from copy import deepcopy

script_path = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(script_path, f"input.txt"), encoding="utf-8") as input:
        lines = input.read().split("\n\n")

p1_input = lines[0].splitlines()[1:]
p2_input = lines[1].splitlines()[1:]

#! ########### PART 1 ############
def calc_score(p):
    return sum([(i + 1) * int(c) for i, c in enumerate(p[::-1])])

p1 = deepcopy(p1_input)
p2 = deepcopy(p2_input)

def play_game1(p1, p2):
    while len(p1) > 0 and len(p2) > 0:
        c1, c2 = p1.pop(0), p2.pop(0)
        if int(c1) > int(c2):
            p1.extend([c1,c2])
        else:
            p2.extend([c2, c1])
        result = calc_score(p1) if len(p1) > 0 else calc_score(p2)
    return result

print (f"Part 1 result = {play_game1(p1,p2)}") #34127
        
#! ########### PART 2 ############
p1 = deepcopy(p1_input)
p2 = deepcopy(p2_input)

def play_game(p1, p2, game):
    game += 1
    rounds = 1
    #print(" "*game + f"=== Game {game} ===\n")
    log = set()
    while len(p1)>0 and len(p2) > 0:
        # Before either player deals a card, if there was a previous round in this game that had 
        # exactly the same cards in the same order in the same players' decks, 
        # the game instantly ends in a win for player 1. Previous rounds from other games are not considered. 
        # (This prevents infinite games of Recursive Combat, which everyone agrees is a bad idea.)
        #print(" "*game + f"-- Round {rounds} (Game {game} --")
        #print(f"Player 1s deck: {','.join(p1)}")
        #print(f"Player 2s deck: {','.join(p2)}")
        log_entry = ",".join(p1) + "|" + ",".join(p2)
        if log_entry in log:
            return 1, p1
        else:
            log.add(log_entry)
             #the players begin the round by each drawing the top card of their deck as normal.
            c1, c2 = p1.pop(0), p2.pop(0)
            #print(f"Player 1 plays: {c1}")
            #print(f"Player 2 plays: {c2}")

            #If both players have at least as many cards remaining in their deck as the value of the card they just drew, 
            # the winner of the round is determined by playing a new game of Recursive Combat (see below).
            if len(p1) >= int(c1) and len(p2) >= int(c2):
                #To play a sub-game of Recursive Combat, each player creates a new deck by making a copy of the next cards 
                # in their deck (the quantity of cards copied is equal to the number on the card they drew to trigger the sub-game).
                winner, _ = play_game(deepcopy(p1[:int(c1)]),
                                      deepcopy(p2[:int(c2)]), game) # new sub game
            else:
                #otherwise, at least one player must not have enough cards left in their deck to recurse; 
                # the winner of the round is the player with the higher-value card.
                winner = 1 if int(c1) > int(c2) else 2
        if winner == 1:
            p1.extend([c1,c2])
        else:
            p2.extend([c2,c1])
        rounds += 1 
    return winner, p1 if winner == 1 else p2

winner, p = play_game(p1, p2, game=0)
result = calc_score(p)
print(f"Player {winner} wins with {result}") #32054
