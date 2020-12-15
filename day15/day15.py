# https://adventofcode.com/2020/day/15

def main(day):

    #deck = [0, 3, 6] #test input
    #deck = [1,3,6] #test input
    deck = [1, 0, 18, 10, 19, 6] # input
    end = 202100 #part 1
    #end = 30000000 #part 2

    for round in range(len(deck)+1, end):
        if deck[-1] not in deck[:-1]:
            # the last number has not been said before
            deck.append(0)
        else:
            # the last number was said before, so find the number in the deck
            # I reverse the deck without the last card, to use index (to find the first occurence from the end)
            #diff = len(deck)-(len(deck)-1 - deck[-2::-1].index(deck[-1]) )
            deck.append(len(deck)-(len(deck)-1 - deck[-2::-1].index(deck[-1]) ))
    print(f"The last number said in round {round} is {deck[-1]}")


import cProfile, pstats, io
from pstats import SortKey
pr = cProfile.Profile()
pr.enable()

main(14)

pr.disable()
s = io.StringIO()
sortby = SortKey.CUMULATIVE
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())
