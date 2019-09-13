from enum import Enum, unique
from random import shuffle, sample

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

    def __repr__(self):
        return f'<Card {self._rank} {self._suit}>'

class Deck(object):
    def __init__(self):
        self.__fullset = frozenset([Card(rank, suit) for rank in Ranks for suit in Suits])
        self.__remaining_cards = list(self.__fullset)
        self.__dealt_cards = list()

    def get_fullset(self) -> frozenset:
        return self.__fullset

    def shuffle(self) -> None:
        shuffle(self.__remaining_cards)

    def reset(self) -> None:
        self.__remaining_cards = list(self.__fullset)
        self.__dealt_cards = list()

    def print_deck(self) -> None:
        print('Dealt: {}'.format(len(self.__dealt_cards)))
        print('Remaining: {}'.format(len(self.__remaining_cards)))
        print('Total: {}'.format(len(self.__fullset)))
    
    def deal_one(self) -> Card:
        if len(self.__remaining_cards) is 0:
            return False
        
        dealt_card = sample(self.__remaining_cards, 1)[0]
        self.__remaining_cards.remove(dealt_card)
        self.__dealt_cards.append(dealt_card)

        return dealt_card

    def deal_n(self, n: int) -> list:
        dealt_cards = list()
        for i in range(n):
            dealt_card = self.deal_one()

            if not dealt_card:
                return False
            else:
                dealt_cards.append(dealt_card)

        return dealt_cards

if __name__ == "__main__":
    d = Deck()
    d.shuffle()
    d.print_deck()
    print(d.deal_n(4))
    d.print_deck()