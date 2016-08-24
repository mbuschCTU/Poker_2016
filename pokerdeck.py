import collections

'''
Card and PokerDeck (originally named FrenchDeck) borrowed from "Fluent Python" by 
Luciano Ramalho.

'''


Card = collections.namedtuple('Card', ['rank', 'suit'])
'''
Card is a "named tuple" data type. Named tuples are like classes with no functions -
in other words they are bundles of attributes. In this case, a Card has a rank and suit.
'''


class PokerDeck(collections.MutableSequence):
    '''
    PokerDeck is a class that contains a list of all the cards in the deck, called _cards.
    Using Python's "magic methods," PokerDeck supports:
    
    * querying for length, 
    * get a card, 
    * set a card's rank and suit (used in shuffle),
    * delete a card,
    * insert a card
    
    Using PokerDeck:
    
    from pokerdeck import *
    from random import choice, shuffle
    
    deck = PokerDeck()
    
    shuffle(deck)
    
    myCard = choice(deck)
    
    print(myCard)
    Card(rank='K', suit='hearts')
    
    print(myCard.rank)
    K
    
    print(myCard.suit)
    hearts
    
    
    Note: it should be possible to use the Unicode suit symbols:
    
    suits = '♥ ♦ ♣ ♠'.split()
    '''
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = '♥ ♦ ♣ ♠'.split()
#    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, value):  # <1>
        self._cards[position] = value

    def __delitem__(self, position):  # <2>
        del self._cards[position]

    def insert(self, position, value):  # <3>
        self._cards.insert(position, value)
