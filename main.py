from Game import Game
from Player import Player

if __name__ == '__main__':
    while True:
        player = Player(input("Enter your name: "))
        game = Game()
        while not game.is_over():
            x: int|None = None
            y: int|None = None
            value: int|None = None
            while x is None and y is None and value is None:
                try:
                    x = int(input("Enter your x: "))
                    y = int(input("Enter your y: "))
                    value = int(input("Enter your value: "))
                except ValueError:
                    print("Les valeurs fournies ne sont pas valides")
            print("ici")
            print(game.play(player, x, y, value))

