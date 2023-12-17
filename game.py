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
        Affiche la grille de jeu actuelle avec des numéros de lignes et de colonnes.
        """
        # Afficher les numéros de colonne
        header = '   ' + ' '.join([str(i).rjust(2) for i in range(self.width)])
        print(header)
        print('  +' + '--' * self.width + '+')

        # Afficher chaque ligne avec son numéro de ligne
        for y in range(self.height):
            row = f'{y}'.rjust(2) + '| ' + ' '.join([cell.rjust(2) if cell != '*' else '■'.rjust(2) for cell in self.player_grid[y]]) + ' |'
            print(row)

        print('  +' + '--' * self.width + '+')
    
    def calculate_adjacent_mines(self):
        """
        Calcule le nombre de mines adjacentes pour chaque case non minée.
        """
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == 'M':
                    continue  # Pas besoin de calculer pour les mines

                # Compter les mines dans les cases adjacentes
                mine_count = 0
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < self.height and 0 <= nx < self.width and self.grid[ny][nx] == 'M':
                            mine_count += 1

                # Mettre à jour la grille avec le nombre de mines adjacentes
                self.grid[y][x] = mine_count
    
    def discover_cell(self, x, y):
        """
        Gère la découverte d'une case. Retourne True si une mine est découverte.
        False si la case a été découverte avec succès.
        Et None si la case a déjà été découverte.
        """
        if self.player_grid[y][x] != '*':  # Vérifier si la case a déjà été découverte
            return None  # Retourner None si la case a déjà été découverte

        if self.player_grid[y][x] == 'M':
            return None  # La case est marquée comme mine, ne peut pas être découverte

        if self.grid[y][x] == 'M':
            return True  # La partie se termine si une mine est découverte

        self.reveal_cell(x, y)
        return False

    def reveal_cell(self, x, y):
        """
        Révèle la case et, si elle a 0 mines adjacentes, révèle également les cases adjacentes.
        """
        if self.player_grid[y][x] != '*':
            return  # La case est déjà révélée

        self.player_grid[y][x] = str(self.grid[y][x])

        if self.grid[y][x] == 0:
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < self.height and 0 <= nx < self.width:
                        self.reveal_cell(nx, ny)

    def mark_mine(self, x, y):
        """
        Permet au joueur de marquer une case comme contenant une mine.
        """
        if self.player_grid[y][x] == '*':
            self.player_grid[y][x] = 'M'
        elif self.player_grid[y][x] == 'M':
            self.player_grid[y][x] = '*'

    def check_victory(self):
        """
        Vérifie si le joueur a gagné, c'est-à-dire si toutes les cases non-minées ont été découvertes.
        """
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] != 'M' and self.player_grid[y][x] == '*':
                    # Il reste des cases non-minées à découvrir
                    return False
        # Toutes les cases non-minées ont été découvertes
        return True
