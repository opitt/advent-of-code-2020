# https://adventofcode.com/2020/day/15

def main(day):
    #deck = [0, 3, 6] #test input
    #deck = [1,3,6] #test input
    deck = [1, 0, 18, 10, 19, 6]

    # part 1
    def simplesolution(deck, end):
        for round in range(len(deck)+1, end):
            if deck[-1] not in deck[:-1]:
                # the last number has not been said before
                deck.append(0)
            else:
                # the last number was said before, so find the number in the deck
                # I reverse the deck without the last card, to use index (to find the first occurence from the end)
                #diff = len(deck)-(len(deck)-1 - deck[-2::-1].index(deck[-1]) )
                deck.append(len(deck)-(len(deck)-1 - deck[-2::-1].index(deck[-1]) ))
        return deck[-1]
    
    end = 2021 #part 1
    result = simplesolution(deck, end)
    print(f"PART 2: The last number said in round {end} is {result}") #441

    # part 2
    def fastsolution(deck, end):
        cards_last_pos = {card: i+1 for i,card in enumerate(deck)} # card: lastpos
        last_card = deck[-1]
        last_pos = len(deck)
        deck = deck[:-1] 
        for round in range(len(deck)+2, end+1):
            if cards_last_pos.get(last_card, -1) == -1:
                cards_last_pos[last_card] = last_pos # move the last round into the deck
                # the last number has not been said before
                last_card = 0
                last_pos = round
            else:
                #  the last number was said before, so find the number in the deck
                # I reverse the deck without the last card, to use index (to find the first occurence from the end)
                diff = last_pos - cards_last_pos[last_card]
                cards_last_pos[last_card] = last_pos # move the last round into the deck
                last_card = diff
                last_pos = round
        return last_card

    #deck = [0, 3, 6]
    end = 30000000
    result = fastsolution(deck, end)        
    print(f"PART 2: The last number said in round {end} is {result}") #10613991


'''
import cProfile, pstats, io
from pstats import SortKey
pr = cProfile.Profile()
pr.enable()
'''
main(15)
'''
pr.disable()
s = io.StringIO()
sortby = SortKey.CUMULATIVE
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())
'''
