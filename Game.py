import random

from Player import Player

class Game:
    """Constructeur"""
    def __init__(self):
        self._board: list = [
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None]
        ]
        self._generated: list[list[int]] = []
        self._turn: int = 0
        self._is_over: bool = False
        self._is_solved: bool = False
        self._winner: Player|None = None
        self._generate_board()
        self.print_board()


    """Génére une grille de sudoku sur le board"""
    def _generate_board(self, difficulty: str = "done"):
        if difficulty == "done":
            number = 81
        elif difficulty == "easy":
            number = 60
        elif difficulty == "merdium":
            number = 40
        elif difficulty == "hard":
            number = 20
        else:
            return
        random_tuple = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(random_tuple)
        random_y = random.randint(0, 8)
        self._board[random_y] = random_tuple
        for i in range(len(self._board)):
            if self._board[i][0] is not None:
                for j in range(len(self._board[i])):
                    possibilities = self._get_possibilities_for_coordinates(j, i)




    """Pour un set de coordonnées x y passé en paramètre, renvoi une list de toute les valeurs possible"""
    def _get_possibilities_for_coordinates(self, x: int, y: int) -> list:
        number_set = (1, 2, 3, 4, 5, 6, 7, 8, 9)
        returned_set = list()
        for num in number_set:
            if self._check_if_valid(x, y, num):
                returned_set.append(num)
        return returned_set


    """Vérifie si une valeur qu'on place a une position [x, y] est 
    valide (donc qu'elle est absente dans la ligne, la colonne, et le carré 3x3)"""
    def _check_if_valid(self, x: int, y: int, value: int) -> bool:
        #Check sur l'axe x (horizontal)
        for val in self._board[y]:
            if val == value:
                return False
        #Check sur l'axe y (vertical)
        for i in range(len(self._board)):
            if self._board[i][x] == value:
                return False
        #Check dans le carré 3x3
        x_start: int = (x//3) * 3
        y_start: int = (y//3) * 3
        for i in range(3):
            for j in range(3):
                if self._board[y_start + j][x_start + i] == value:
                    return False
        return True


    """Permet de jouer un tour"""
    def play(self, player: Player, x: int, y: int, value: int) -> bool:
        if 0 <= x <= 8 and 0 <= y <= 8 and 1 <= value <= 9 and self._check_if_valid(x, y, value):
            self._board[y][x] = value
            self._turn += 1
            self.print_board()
            self._check_if_over(player)
            return True
        return False


    """Vérifie si la partie est terminé"""
    def _check_if_over(self, player: Player):
        for i in range(len(self._board)):
            for j in range(len(self._board[i])):
                if self._board[i][j] is None:
                    return
        self._is_over = True


    """Affiche la grille de jeu dans la console"""
    def print_board(self):
        print("  -   -   -   -   -   -   -   -   -")
        for i in range(len(self._board)):
            print("|", end="")
            for j in range(len(self._board[i])):
                print(" {} |".format(self._board[i][j] or " "), end="")
            print("\n  -   -   -   -   -   -   -   -   -")


    """Getter pour le champ is_over"""
    def is_over(self):
        return self._is_over
