import random

class Game:
    def __init__(self, hauteur, largeur, nb_mines):
        """
        Initialise une nouvelle partie de démineur.
        """
        self.hauteur = hauteur
        self.largeur = largeur
        self.nb_mines = nb_mines
        self.grille = self.initialiser_grille()
        self.grille_joueur = [['*' for _ in range(self.largeur)] for _ in range(self.hauteur)]

    def initialiser_grille(self):
        """
        Initialise la grille de jeu avec des mines placées aléatoirement.
        """
        grille = [[0 for _ in range(self.largeur)] for _ in range(self.hauteur)]
        mines = set()

        while len(mines) < self.nb_mines:
            position = (random.randint(0, self.hauteur - 1), random.randint(0, self.largeur - 1))
            if position not in mines:
                mines.add(position)
                y, x = position
                grille[y][x] = 'M'

        return grille

    def afficher_grille(self):
        """
        Affiche la grille de jeu actuelle avec des numéros de lignes et de colonnes.
        """
        entete = '   ' + ' '.join(str(i).rjust(2) for i in range(self.largeur))
        print(entete)
        print('  +' + '---' * self.largeur + '+')

        for y in range(self.hauteur):
            ligne = f'{y}'.rjust(2) + '|'
            for cellule in self.grille_joueur[y]:
                if cellule == '*':
                    cellule_formatee = '■'
                elif cellule == '0':
                    cellule_formatee = ' '
                else:
                    cellule_formatee = cellule
                ligne += cellule_formatee.center(3)
            ligne += '|'
            print(ligne)

        print('  +' + '---' * self.largeur + '+')
    
    def calculer_mines_adjacentes(self):
        """
        Calcule le nombre de mines adjacentes pour chaque case non minée.
        """
        for y in range(self.hauteur):
            for x in range(self.largeur):
                if self.grille[y][x] == 'M':
                    continue

                compte_mines = 0
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < self.hauteur and 0 <= nx < self.largeur and self.grille[ny][nx] == 'M':
                            compte_mines += 1

                self.grille[y][x] = compte_mines
    
    def decouvrir_case(self, x, y):
        """
        Gère la découverte d'une case. Retourne True si une mine est découverte.
        False si la case a été découverte avec succès.
        Et None si la case a déjà été découverte ou est marquée.
        """
        if self.grille_joueur[y][x] != '*':
            return None

        if self.grille[y][x] == 'M':
            return True

        self.reveler_case(x, y)
        return False

    def reveler_case(self, x, y):
        """
        Révèle la case et, si elle a 0 mines adjacentes, révèle également les cases adjacentes.
        """
        self.grille_joueur[y][x] = str(self.grille[y][x])

        if self.grille[y][x] == 0:
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < self.hauteur and 0 <= nx < self.largeur and self.grille_joueur[ny][nx] == '*':
                        self.reveler_case(nx, ny)

    def marquer_mine(self, x, y):
        """
        Permet au joueur de marquer ou démarquer une case comme contenant une mine.
        """
        if self.grille_joueur[y][x] == '*':
            self.grille_joueur[y][x] = 'M'
        elif self.grille_joueur[y][x] == 'M':
            self.grille_joueur[y][x] = '*'

    def verifier_victoire(self):
        """
        Vérifie si le joueur a gagné, c'est-à-dire si toutes les cases non-minées ont été découvertes.
        """
        for y in range(self.hauteur):
            for x in range(self.largeur):
                if self.grille[y][x] != 'M' and self.grille_joueur[y][x] == '*':
                    return False
        return True
