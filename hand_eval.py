from pokerdeck import *
from random import shuffle, choice
deck = PokerDeck()
shuffle(deck)

hand =  [choice(deck) for _ in range(5)]


#----------------------------------------------------------------------
def get_ranks(hand):
    """"""
    return [card.rank for card in hand]
#----------------------------------------------------------------------
def pair(hand):
    """"""
    ranks = get_ranks(hand)
    pair = {rank for rank in ranks if ranks.count(rank) == 2}
    return len(pair) == 1
    
#----------------------------------------------------------------------
def triple(hand):
    """"""
    ranks = get_ranks(hand)
    trip = {rank for rank in ranks if ranks.count(rank) == 3}
    return len(trip) == 1

pair(hand)
