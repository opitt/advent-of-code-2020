from copy import deepcopy

p1='''9
2
6
3
1'''.splitlines()

p2='''5
8
4
7
10'''.splitlines()


p1_input = '''4
14
5
49
3
48
41
39
18
15
46
23
32
16
19
27
47
17
29
26
33
6
10
38
45'''.splitlines()

p2_input = '''1
24
7
44
20
40
42
50
37
21
43
9
12
8
34
13
28
36
25
35
22
2
11
30
31'''.splitlines()

p1 = list(map(int, p1_input))
p2 = list(map(int, p2_input))

#! ########### PART 1 ############
while len(p1) > 0 and len(p2) > 0:
    c1, c2 = p1.pop(0), p2.pop(0)
    if c1 > c2:
        p1.append(c1)
        p1.append(c2)
    else:
        p2.append(c2)
        p2.append(c1)
if len(p1) > 0:
   result = sum([(i + 1) * c for i, c in enumerate(p1[::-1])])
else:
   result = sum([(i + 1) * c for i, c in enumerate(p2[::-1])])
print (f"Part 1 result = {result}") #34127
        
#! ########### PART 2 ############
#test
p1_input='''43
19'''.splitlines()

p2_input='''2
29
14'''.splitlines()

p1 = deepcopy(p1_input)
p2 = deepcopy(p2_input)

def hist_string(p1, p2):
    return ",".join(p1) + "|" + ",".join(p2)

def check_history(p1, p2, p_hist):
    s = hist_string(p1, p2)
    return s in p_hist


def play_game(p1, p2, game):
    game += 1
    rounds = 1
    p_hist = []
    print(f"=== Game {game} ===\n")
    while len(p1)>0 and len(p2) > 0:
        # Before either player deals a card, if there was a previous round in this game that had 
        # exactly the same cards in the same order in the same players' decks, 
        # the game instantly ends in a win for player 1. Previous rounds from other games are not considered. 
        # (This prevents infinite games of Recursive Combat, which everyone agrees is a bad idea.)
        print(f"-- Round {rounds} (Game {game} --")
        print(f"Player 1's deck: {p1}")
        print(f"Player 2's deck: {p2}")
        if check_history(p1, p2, p_hist):
            print("same set detected. player 1 wins the game.")
            return 1, p1, p2
        else:
            p_hist.append(hist_string(p1, p2))
             #the players begin the round by each drawing the top card of their deck as normal.
            c1, c2 = p1.pop(0), p2.pop(0)
            print(f"Player 1 plays: {c1}")
            print(f"Player 2 plays: {c2}")

            #If both players have at least as many cards remaining in their deck as the value of the card they just drew, 
            # the winner of the round is determined by playing a new game of Recursive Combat (see below).
            if len(p1) >= int(c1) and len(p2) >= int(c2):
                winner, _, _ = play_game(deepcopy(p1), deepcopy(p2), game) # new sub game
                print(f"Player {winner} wins round {rounds} of game {game}! (sub-game)")
            else:
                #Otherwise, at least one player must not have enough cards left in their deck to recurse; 
                # the winner of the round is the player with the higher-value card.
                winner = 1 if int(c1) > int(c2) else 2
                print(f"Player {winner} wins round {rounds} of game {game}! (cards)")
        if winner == 1:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)
        rounds += 1

    return winner, p1, p2

game = 0
winner, p1, p2 = play_game(p1, p2, game)
print(f"Player {winner} wins!")
