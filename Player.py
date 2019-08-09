class Player(object):
    def __init__(self, host, name, password):
        self.__host = host
        self.__passward = password
        self._name = name
        self._capital = 0

    def set_capital(self, capital):
        self._capital = capital

    def deduct_bet(self, bet):
        self._capital -= bet

    def __repr__(self):
        return f'<Player {self._name} ${self._capital}>'

if __name__ == "__main__":
    player1 = Player(0x800, 'Bryan', 1234)
    player2 = Player(0x500, 'Tom', 5678)
    players = [player1, player2]

    print(players)

    player1.deduct_bet(10)
    player2.deduct_bet(999)

    print(players)
