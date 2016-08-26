# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 19:15:04 2016

@author: zen
"""

from pokerdeck import *
from random import choice, shuffle

hand1 = []
hand2 = []

deck = PokerDeck()
shuffle(deck)

#----------------------------------------------------------------------
def deal_hand():
    '''
    >>> hand = deal_hand()
    >>> len(hand)
    5
    >>> len(deck)
    47
    '''
    hand = []
    while len(hand) < 5:
        card = choice(deck)
        hand.append(card)
        index = deck.index(card)
        deck.remove(deck[index])
    return hand

'''
0 high card        1 pair  
2 two pair         3 three of a kind
4 straight         5 flush
6 full house       7 four of a kind
8 straight flush   9 royal flush
'''
       
def find_ranks(hand):
    '''
    >>> hand = [Card(rank='8', suit='♠'), Card(rank='K', suit='♠'), Card(rank='J', suit='♦'), Card(rank='Q', suit='♠'), Card(rank='Q', suit='♥')]
    >>> find_ranks(hand)
    ['8', 'K', 'J', 'Q', 'Q']
    '''
    return [card.rank for card in hand]

#----------------------------------------------------------------------    
def find_suits(hand):
    '''
    >>> hand = [Card(rank='8', suit='♠'), Card(rank='K', suit='♠'), Card(rank='J', suit='♦'), Card(rank='Q', suit='♠'), Card(rank='Q', suit='♥')]
    >>> find_suits(hand)
    ['♠', '♠', '♦', '♠', '♥']
    '''
    return [card.suit for card in hand]

#----------------------------------------------------------------------    
def find_pairs(hand):
    '''
    >>> hand1 = [Card(rank='9', suit='♦'), Card(rank='A', suit='♦'), Card(rank='A', suit='♥'), Card(rank='A', suit='♠'), Card(rank='3', suit='♠')]
    >>> find_pairs(hand1)
    0
    >>> hand2 = [Card(rank='8', suit='♠'), Card(rank='K', suit='♠'), Card(rank='J', suit='♦'), Card(rank='Q', suit='♠'), Card(rank='Q', suit='♥')]
    >>> find_pairs(hand2)
    1
    >>> hand2 = [Card(rank='8', suit='♠'), Card(rank='K', suit='♠'), Card(rank='8', suit='♦'), Card(rank='Q', suit='♠'), Card(rank='Q', suit='♥')]
    >>> find_pairs(hand2)
    2

    '''
    ranks = find_ranks(hand)
    pairs = set()
    
    for number in ranks:
        if ranks.count(number) == 2:
            pairs.add(number)
        
    return len(pairs)


#----------------------------------------------------------------------
def triple(hand):
    '''
    >>> hand1 = [Card(rank='9', suit='♦'), Card(rank='A', suit='♦'), Card(rank='A', suit='♥'), Card(rank='A', suit='♠'), Card(rank='3', suit='♠')]
    >>> triple(hand1)
    3
    >>> hand2 = [Card(rank='8', suit='♠'), Card(rank='K', suit='♠'), Card(rank='J', suit='♦'), Card(rank='Q', suit='♠'), Card(rank='Q', suit='♥')]
    >>> triple(hand2)
    0
    '''
    ranks = find_ranks(hand)
    
    for number in ranks:
        if ranks.count(number) == 3:
            return 3
    return 0

#----------------------------------------------------------------------
def quad(hand):
    """
    >>> hand1 = [Card(rank='A', suit='♣'), Card(rank='A', suit='♦'), Card(rank='A', suit='♥'), Card(rank='A', suit='♠'), Card(rank='3', suit='♠')]
    >>> quad(hand1)
    7
    >>> hand1 = [Card(rank='A', suit='♣'), Card(rank='A', suit='♦'), Card(rank='A', suit='♥'), Card(rank='A', suit='♠'), Card(rank='3', suit='♠')]
    >>> quad(hand2)
    0
    """
    ranks = find_ranks(hand)
    
    for number in ranks:
        if ranks.count(number) == 4:
            return 7
    return 0    
    

def flush(hand):
    '''
    >>> hand1 = [Card(rank='9', suit='♦'), Card(rank='A', suit='♦'), Card(rank='A', suit='♦'), Card(rank='A', suit='♦'), Card(rank='3', suit='♦')]
    >>> flush(hand1)
    5
    >>> hand2 = [Card(rank='8', suit='♠'), Card(rank='K', suit='♠'), Card(rank='J', suit='♦'), Card(rank='Q', suit='♠'), Card(rank='Q', suit='♥')]
    >>> flush(hand2)
    0
    '''
    suits = []
    for card in hand:
        suits.append(card.suit)
    if suits.count(suits[0]) == 5:
        return 5
    return 0

def straight(hand):
    '''
    >>> hand1 = [Card(rank='J', suit='♦'), Card(rank='10', suit='♦'), Card(rank='A', suit='♦'), Card(rank='Q', suit='♦'), Card(rank='K', suit='♦')]
    >>> straight(hand1)
    9
    >>> hand2 = [Card(rank='8', suit='♠'), Card(rank='K', suit='♠'), Card(rank='J', suit='♦'), Card(rank='Q', suit='♠'), Card(rank='Q', suit='♥')]
    >>> straight(hand2)
    0
    >>> hand1 = [Card(rank='3', suit='♦'), Card(rank='6', suit='♦'), Card(rank='4', suit='♦'), Card(rank='7', suit='♦'), Card(rank='5', suit='♦')]
    >>> straight(hand1)
    4
    >>> hand1 = [Card(rank='J', suit='♦'), Card(rank='10', suit='♦'), Card(rank='8', suit='♦'), Card(rank='Q', suit='♦'), Card(rank='9', suit='♦')]
    >>> straight(hand1)
    4
    '''    
    ranks = find_ranks(hand)
    ranks = sub_face_cards(ranks)
    ranks.sort(key = int)
    if int(ranks[4]) - int(ranks[0]) == 4:
        if ranks[0] == '10':
            return 9
        else:
            return 4
    return 0


def sub_face_cards(ranks):
    '''
    >>> hand1 = [Card(rank='J', suit='♦'), Card(rank='10', suit='♦'), Card(rank='A', suit='♦'), Card(rank='Q', suit='♦'), Card(rank='K', suit='♦')]
    >>> ranks = find_ranks(hand1)
    >>> sub_face_cards(ranks)
    ['11', '10', '14', '12', '13']
    '''
    for card in ranks:
        if card == 'J':
            i = ranks.index('J')
            ranks[i] = '11'
        elif card == 'Q':
            i = ranks.index('Q')
            ranks[i] = '12'            
        elif card == 'K':
            i = ranks.index('K')
            ranks[i] = '13'
    if 'A' in ranks:
        i = ranks.index('A')
        if 'A' in ranks and '2' in ranks:  # check for pair before straight      
            ranks[i] = '1'
        else:
            ranks[i]= '14'
    return ranks
        
            
def rate_hand(hand):
    '''
    >>> hand1 = [Card(rank='3', suit='♠'), Card(rank='6', suit='♦'), Card(rank='4', suit='♦'), Card(rank='7', suit='♦'), Card(rank='5', suit='♦')]
    >>> rate_hand(hand1)    # straight
    4
    >>> hand1 = [Card(rank='3', suit='♦'), Card(rank='6', suit='♦'), Card(rank='4', suit='♦'), Card(rank='7', suit='♦'), Card(rank='5', suit='♦')]
    >>> rate_hand(hand1)    # straight flush
    8
    >>> hand1 = [Card(rank='2', suit='♦'), Card(rank='6', suit='♦'), Card(rank='4', suit='♦'), Card(rank='7', suit='♦'), Card(rank='5', suit='♦')]
    >>> rate_hand(hand1)    # flush
    5
    >>> hand1 = [Card(rank='J', suit='♦'), Card(rank='10', suit='♦'), Card(rank='8', suit='♦'), Card(rank='Q', suit='♦'), Card(rank='9', suit='♦')]
    >>> rate_hand(hand1)    # straight flush
    8
    >>> hand2 = [Card(rank='8', suit='♠'), Card(rank='K', suit='♠'), Card(rank='J', suit='♦'), Card(rank='Q', suit='♠'), Card(rank='Q', suit='♥')]
    >>> rate_hand(hand2)    # pair
    1
    >>> hand2 = [Card(rank='8', suit='♠'), Card(rank='K', suit='♠'), Card(rank='8', suit='♦'), Card(rank='Q', suit='♠'), Card(rank='Q', suit='♥')]
    >>> rate_hand(hand2)    # two pair
    2
    >>> hand1 = [Card(rank='9', suit='♦'), Card(rank='A', suit='♦'), Card(rank='A', suit='♥'), Card(rank='A', suit='♠'), Card(rank='3', suit='♠')]
    >>> rate_hand(hand1)    # three of a kind
    3
    >>> hand1 = [Card(rank='9', suit='♦'), Card(rank='A', suit='♦'), Card(rank='A', suit='♥'), Card(rank='A', suit='♠'), Card(rank='9', suit='♠')]
    >>> rate_hand(hand1)    # full house
    6
    >>> hand1 = [Card(rank='A', suit='♣'), Card(rank='A', suit='♦'), Card(rank='A', suit='♥'), Card(rank='A', suit='♠'), Card(rank='3', suit='♠')]
    >>> rate_hand(hand1)
    7
    '''
    pair_score = find_pairs(hand)
    triple_score = triple(hand)
    quad_score  = quad(hand)
    if pair_score == 1 and triple_score == 3:  # check for full house before returning pair or triple
        return 6
    elif triple_score:      # only one triple
        return triple_score
    elif pair_score:      # return 1 or 2 pair
        return pair_score
    if quad_score:
        return quad_score
    straight_score = straight(hand)
    flush_score = flush(hand)
    if flush_score == 5:
        if straight_score == 9:
            return 9
        elif straight_score == 4:
            return 8
        else:    
            return 5
    elif straight_score:
        return 4
    else:
        return 0

#----------------------------------------------------------------------
def print_card(card):
    """
    >>> card = Card(rank='9', suit='♦')
    >>> print_card(card)
    9♦ 
    """
    print(''.join(card) + ' ', end='')
    

#----------------------------------------------------------------------
def print_hand(hand): # pragma: no cover
    """
    >>> hand1 = [Card(rank='9', suit='♦'), Card(rank='A', suit='♦'), Card(rank='A', suit='♥'), Card(rank='A', suit='♠'), Card(rank='9', suit='♠')]
    >>> print_hand(hand1)
    9♦ A♦ A♥ A♠ 9♠ 
    """
    for card in hand:
        print_card(card)
    print()
    
#----------------------------------------------------------------------
def eval_winner(hand1, hand2):
    """
    >>> hand1 = [Card(rank='3', suit='♦'), Card(rank='6', suit='♦'), Card(rank='4', suit='♦'), Card(rank='7', suit='♦'), Card(rank='5', suit='♦')]
    >>> hand2 = [Card(rank='8', suit='♠'), Card(rank='K', suit='♠'), Card(rank='J', suit='♦'), Card(rank='Q', suit='♠'), Card(rank='Q', suit='♥')]
    >>> eval_winner(hand1, hand2)
    '1'
    >>> hand1 = [Card(rank='3', suit='♠'), Card(rank='6', suit='♦'), Card(rank='4', suit='♦'), Card(rank='7', suit='♦'), Card(rank='5', suit='♦')]
    >>> hand2 = [Card(rank='A', suit='♣'), Card(rank='A', suit='♦'), Card(rank='A', suit='♥'), Card(rank='A', suit='♠'), Card(rank='3', suit='♠')]
    >>> eval_winner(hand1, hand2)
    '2'
    """
    score1 = rate_hand(hand1)
    score2 = rate_hand(hand2)
    if score1 > score2:
        return '1'
    elif score2 > score1:
        return '2'
    else:
        return 'tie'
    
if __name__ == '__main__': # pragma: no cover
    import doctest
    doctest.testmod()
    hand1 = deal_hand()
    hand2 = deal_hand()

    print('\n==============================')
    print('Hand 1: ', end='')
    print_hand(hand1)
    print('\nHand 2: ', end='')
    print_hand(hand2)
    print('==============================')
    print('\n\tWinner: '+ eval_winner(hand1, hand2) + '\n')
