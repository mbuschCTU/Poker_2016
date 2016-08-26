from hand_eval import *
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

def test_find_ranks():
    pair_hand = [Card('9', '♦'), Card('9', '♥'), Card('4', '♠'), Card('J', '♠'), Card('Q', '♠')]
    assert find_ranks(pair_hand) == ['9', '9', '4', 'J', 'Q']


def test_find_suits():
    pair_hand = [Card('9', '♦'), Card('9', '♥'), Card('4', '♠'), Card('J', '♠'), Card('Q', '♠')]
    assert find_suits(pair_hand) == ['♦', '♥', '♠', '♠','♠']

def test_pairs():
    pair_hand = [Card('9', '♦'), Card('9', '♥'), Card('4', '♠'), Card('J', '♠'), Card('Q', '♠')]
    two_pair_hand = [Card('9', '♦'), Card('9', '♥'), Card('Q', '♠'), Card('J', '♠'), Card('Q', '♠')]
    no_pair_hand = [Card('8', '♦'), Card('9', '♥'), Card('4', '♠'), Card('J', '♠'), Card('Q', '♠')]
    assert find_pairs(pair_hand) == 1
    assert find_pairs(two_pair_hand) == 2
    assert find_pairs(no_pair_hand) == 0

def test_triple():
    hand1 = [Card(rank='9', suit='♦'), Card(rank='A', suit='♦'), Card(rank='A', suit='♥'), Card(rank='A', suit='♠'),
             Card(rank='3', suit='♠')]
    hand2 = [Card(rank='8', suit='♠'), Card(rank='K', suit='♠'), Card(rank='J', suit='♦'), Card(rank='Q', suit='♠'),
             Card(rank='Q', suit='♥')]
    assert triple(hand1) == 3
    assert triple(hand2) == 0

def test_quad():
    hand1 = [Card(rank='A', suit='♣'), Card(rank='A', suit='♦'), Card(rank='A', suit='♥'), Card(rank='A', suit='♠'),
             Card(rank='3', suit='♠')]
    hand2 = [Card(rank='A', suit='♣'), Card(rank='A', suit='♦'), Card(rank='A', suit='♥'), Card(rank='9', suit='♠'),
             Card(rank='3', suit='♠')]
    assert quad(hand1) == 7
    assert quad(hand2) == 0

def test_flush():
    hand1 = [Card(rank='9', suit='♦'), Card(rank='A', suit='♦'), Card(rank='A', suit='♦'), Card(rank='A', suit='♦'),
             Card(rank='3', suit='♦')]
    hand2 = [Card(rank='8', suit='♠'), Card(rank='K', suit='♠'), Card(rank='J', suit='♦'), Card(rank='Q', suit='♠'),
             Card(rank='Q', suit='♥')]
    assert flush(hand1) == 5
    assert flush(hand2) == 0

def test_sub_face_cards():
    hand1 = [Card(rank='J', suit='♦'), Card(rank='10', suit='♦'), Card(rank='A', suit='♦'), Card(rank='Q', suit='♦'),
             Card(rank='K', suit='♦')]
    ranks1 = find_ranks(hand1)
    assert sub_face_cards(ranks1) == ['11', '10', '14', '12', '13']


def test_straight():
    hand1 = [Card(rank='J', suit='♦'), Card(rank='10', suit='♦'), Card(rank='A', suit='♦'), Card(rank='Q', suit='♦'), Card(rank='K', suit='♦')]
    hand2 = [Card(rank='8', suit='♠'), Card(rank='K', suit='♠'), Card(rank='J', suit='♦'), Card(rank='Q', suit='♠'), Card(rank='Q', suit='♥')]
    hand3 = [Card(rank='3', suit='♦'), Card(rank='6', suit='♦'), Card(rank='4', suit='♦'), Card(rank='7', suit='♦'), Card(rank='5', suit='♦')]
    hand4 = [Card(rank='J', suit='♦'), Card(rank='10', suit='♦'), Card(rank='8', suit='♦'), Card(rank='Q', suit='♦'), Card(rank='9', suit='♦')]
    assert straight(hand1) == 9
    assert straight(hand2) == 0
    assert straight(hand3) == 4
    assert straight(hand4) == 4



def test_rate_hand():
   hand1 = [Card(rank='3', suit='♠'), Card(rank='6', suit='♦'), Card(rank='4', suit='♦'), Card(rank='7', suit='♦'), Card(rank='5', suit='♦')]
   hand2 = [Card(rank='3', suit='♦'), Card(rank='6', suit='♦'), Card(rank='4', suit='♦'), Card(rank='7', suit='♦'), Card(rank='5', suit='♦')]
   hand3 = [Card(rank='2', suit='♦'), Card(rank='6', suit='♦'), Card(rank='4', suit='♦'), Card(rank='7', suit='♦'), Card(rank='5', suit='♦')]
   hand4 = [Card(rank='J', suit='♦'), Card(rank='10', suit='♦'), Card(rank='8', suit='♦'), Card(rank='Q', suit='♦'), Card(rank='9', suit='♦')]
   hand5 = [Card(rank='8', suit='♠'), Card(rank='K', suit='♠'), Card(rank='J', suit='♦'), Card(rank='Q', suit='♠'), Card(rank='Q', suit='♥')]
   hand6 = [Card(rank='8', suit='♠'), Card(rank='K', suit='♠'), Card(rank='8', suit='♦'), Card(rank='Q', suit='♠'), Card(rank='Q', suit='♥')]
   hand7 = [Card(rank='9', suit='♦'), Card(rank='A', suit='♦'), Card(rank='A', suit='♥'), Card(rank='A', suit='♠'), Card(rank='3', suit='♠')]
   hand8 = [Card(rank='9', suit='♦'), Card(rank='A', suit='♦'), Card(rank='A', suit='♥'), Card(rank='A', suit='♠'), Card(rank='9', suit='♠')]
   hand9 = [Card(rank='A', suit='♣'), Card(rank='A', suit='♦'), Card(rank='A', suit='♥'), Card(rank='A', suit='♠'), Card(rank='3', suit='♠')]

   assert rate_hand(hand1) == 4
   assert rate_hand(hand2) == 8
   assert rate_hand(hand3) == 5
   assert rate_hand(hand4) == 8
   assert rate_hand(hand5) == 1
   assert rate_hand(hand6) == 2
   assert rate_hand(hand7) == 3
   assert rate_hand(hand8) == 6
   assert rate_hand(hand9) == 7


def print_card():
    card = Card(rank='9', suit='♦')
    assert print_card(card) == '9♦'

def test_eval_winner():
    hand1 = [Card(rank='3', suit='♦'), Card(rank='6', suit='♦'), Card(rank='4', suit='♦'), Card(rank='7', suit='♦'), Card(rank='5', suit='♦')]
    hand2 = [Card(rank='8', suit='♠'), Card(rank='K', suit='♠'), Card(rank='J', suit='♦'), Card(rank='Q', suit='♠'), Card(rank='Q', suit='♥')]
    hand3 = [Card(rank='3', suit='♠'), Card(rank='6', suit='♦'), Card(rank='4', suit='♦'), Card(rank='7', suit='♦'), Card(rank='5', suit='♦')]
    hand4 = [Card(rank='A', suit='♣'), Card(rank='A', suit='♦'), Card(rank='A', suit='♥'), Card(rank='A', suit='♠'), Card(rank='3', suit='♠')]
    assert eval_winner(hand1, hand2) == '1'
    assert eval_winner(hand3, hand4) == '2'