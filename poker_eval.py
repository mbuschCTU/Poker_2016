from pokerdeck import *
from random import choice, shuffle




def deal_hand():
    hand = []
    deck = PokerDeck()
    shuffle(deck)
    for _ in range(5):
        card = choice(deck)
        deck.remove(card)
        # del deck[deck.index(card)]
        hand.append(card)
    return hand

def print_hand(hand):
    for card in hand:
        print(card, end=' ')
    print()

def get_ranks(hand):
    rank_list = []
    for card in hand:
        rank_list.append(card.rank)
    return rank_list
# print(rank_list)

def get_suits(hand):
    suit_list = []
    for card in hand:
        suit_list.append(card.suit)
    return suit_list


def find_pairs(rank_list):
    pairs = []
    for rank in rank_list:
        if rank_list.count(rank) == 2 and rank not in pairs:
            pairs.append(rank)
    return len(pairs)

def find_flush(suits):
    if suits.count(suits[0]) == 5:
        return True
    else:
        return False

# print(find_pairs(rank_list))

if __name__ == '__main__':  # pragma: no cover
    # hand = []
    hand = deal_hand()
    print_hand(hand)
    ranks = get_ranks(hand)
    suits = get_suits(hand)
    [print(r, end = ' ') for r in ranks]
    print()
    [print(s, end=' ') for s in suits]
    print()
    myHand = [Card(rank='6', suit='♦'), Card(rank='6', suit='♦'), Card(rank='7', suit='♠'), Card(rank='7', suit='♥'), Card(rank='K', suit='♥')]
    print_hand(myHand)
    ranks = get_ranks(myHand)
    print(find_pairs(ranks))
    flushHand = [Card(rank='6', suit='♦'), Card(rank='6', suit='♦'), Card(rank='7', suit='♦'), Card(rank='7', suit='♦'), Card(rank='K', suit='♦')]
    suits = get_suits(flushHand)
    print(find_flush(suits))
