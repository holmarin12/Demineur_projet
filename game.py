import random

class Game:
    def __init__(self, height, width, num_mines):
        """
        Initialise une nouvelle partie de démineur.
        """
        self.height = height
        self.width = width
        self.num_mines = num_mines
        self.grid = self.initialize_grid()
        self.player_grid = [['*' for _ in range(self.width)] for _ in range(self.height)]

    def initialize_grid(self):
        """
        Initialise la grille de jeu avec des mines placées aléatoirement.
        """
        grid = [[0 for _ in range(self.width)] for _ in range(self.height)]

        # Placement des mines
        mines_placed = 0
        while mines_placed < self.num_mines:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)

            # Si la case n'a pas déjà une mine, placez-en une
            if grid[y][x] != 'M':
                grid[y][x] = 'M'
                mines_placed += 1

        return grid

    def print_grid(self):
        """
        Affiche la grille de jeu actuelle.
        """
        for row in self.player_grid:
            print(' '.join(row))
        print()


# CODE DE TEST
if __name__ == "__main__":
    game = Game(10, 10, 20)  # Crée une grille 10x10 avec 20 mines
    game.print_grid()  # Affiche la grille