from Deck import Deck
from Player import Player


class Game(object):
    def __init__(self):
        self.__deck = Deck().shuffle()
        self.__players = set()

    def print_players(self):
        print(self.__players)

    def add_player(self, player: Player) -> set:
        self.__players.add(player)
        return self.__players

    def remove_player(self, player: Player) -> set:
        self.__players.remove(player)
        return self.__players


if __name__ == "__main__":
    game = Game()
    bryan = Player(0x800, "Bryan", "123")
    print(game.add_player(bryan))
    print(game.remove_player(bryan))
