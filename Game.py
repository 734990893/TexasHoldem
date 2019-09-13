from Deck import Deck
from Player import Player

class Game(object):
    def __init__(self):
        self.__deck = Deck().shuffle()
        self.__players = list()

    def print_players(self):
        print(self.__players)

    def add_player(self, player: Player) -> None:
        self.__players.append(player)


if __name__ == "__main__":
    game = Game()
    player = Player(0x800, "Bryan", "123")
    game.add_player(player)
    game.print_players()

