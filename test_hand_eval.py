from poker_eval import *
from pokerdeck import *

# suits = '♥ ♦ ♣ ♠'.split()

def test_deal_hand():
    assert(len(deal_hand()) == 5)

def test_no_dupes():
    hand = deal_hand()
    for card in hand:
        assert hand.count(card) == 1

# pair_hand = [Card('9', '♦'), Card('9', '♥'), Card('4', '♠'), Card('J', '♠'), Card('Q', '♠')]
# no_pair_hand = [Card('8', '♦'), Card('9', '♥'), Card('4', '♠'), Card('J', '♠'), Card('Q', '♠')]

def test_get_ranks():
    pair_hand = [Card('9', '♦'), Card('9', '♥'), Card('4', '♠'), Card('J', '♠'), Card('Q', '♠')]
    assert get_ranks(pair_hand) == ['9', '9', '4', 'J', 'Q']


def test_get_suits():
    pair_hand = [Card('9', '♦'), Card('9', '♥'), Card('4', '♠'), Card('J', '♠'), Card('Q', '♠')]
    assert get_suits(pair_hand) == ['♦', '♥', '♠', '♠','♠']

def test_pairs():
    pair_hand = ['9','9','A','Q','J']
    two_pair_hand  = ['9','9','A','Q','Q']
    no_pair_hand = ['8','9','A','Q','J']
    assert find_pairs(pair_hand) == 1
    assert find_pairs(two_pair_hand) == 2
    assert find_pairs(no_pair_hand) == 0