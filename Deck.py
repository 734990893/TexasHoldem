from enum import Enum, unique
from random import shuffle

@unique
class Suits(Enum):
    HEART = 'H'
    SPADE = 'S'
    CLUB = 'C'
    DIAMOND = 'D'

@unique
class Ranks(Enum):
    A = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    J = 11
    Q = 12
    K = 13

class Card(object):
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    def get_rank(self):
        return self._rank
    
    def get_suit(self):
        return self._suit

    def __str__(self):
        return str(self._rank.value) + ' ' + self._suit.value

class Deck(object):
    def __init__(self):
        self.__cards = [Card(rank, suit) for rank in Ranks for suit in Suits]

    def get_cards(self):
        return self.__cards

    def shuffle(self):
        shuffle(self.__cards)

    def print_deck(self):
        for card in self.__cards:
            print(card)

if __name__ == "__main__":
    d = Deck()
    d.shuffle()
    d.print_deck()