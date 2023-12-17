def display_menu():
    """
    Affiche le menu principal du jeu et retourne le choix de l'utilisateur.
    """
    print("Menu du Démineur")
    print("1. Démarrer une nouvelle partie personnalisable")
    print("2. Démarrer une partie par niveau")
    print("3. Quitter")

    choix = input("Entrez votre choix (1, 2 ou 3): ")
    return choix


def get_game_parameters():
    """
    Demande à l'utilisateur de saisir les paramètres de la partie.
    """
    height = get_valid_input("Entrez la hauteur de la grille (max 30) : ", min_value=1, max_value=30)
    width = get_valid_input("Entrez la largeur de la grille (max 16) : ", min_value=1, max_value=16)
    max_mines = height * width - 1
    num_mines = get_valid_input("Entrez le nombre de mines : ", min_value=1, max_value=max_mines)

    return height, width, num_mines

def choose_level():
    """
    Permet à l'utilisateur de choisir un niveau de difficulté.
    """
    print("Choisissez un niveau de difficulté:")
    print("1. Facile (9x9 avec 10 mines)")
    print("2. Moyen (16x16 avec 40 mines)")
    print("3. Difficile (30x16 avec 99 mines)")

    niveau = input("Entrez votre choix (1, 2 ou 3): ")
    return niveau

def get_valid_input(prompt, min_value=0, max_value=None):
    """
    Demande à l'utilisateur d'entrer un nombre entier valide.
    """
    while True:
        try:
            value = int(input(prompt))
            if (value >= min_value) and (max_value is None or value <= max_value):
                return value
            else:
                print(f"Veuillez entrer un nombre entre {min_value} et {max_value}.")
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

def get_player_action(height, width):
    """
    Demande au joueur de choisir une action, de fournir les coordonnées, ou de revenir au menu.
    """
    valid_actions = ['D', 'M', 'R']  # Ajouter 'R' pour "Revenir au menu"
    action = ''

    while action not in valid_actions:
        action = input("Choisissez une action (Découvrir 'D', Marquer 'M', Revenir au menu 'R'): ").strip().upper()
        if action not in valid_actions:
            print("Action non valide. Veuillez entrer 'D', 'M', ou 'R'.")

    if action == 'R':  # Si l'utilisateur choisit de revenir au menu
        return action, None, None

    x = get_valid_coordinate("Entrez la coordonnée X (colonne): ", width)
    y = get_valid_coordinate("Entrez la coordonnée Y (ligne): ", height)
    return action, x, y


def get_valid_coordinate(prompt, max_value):
    """
    Demande à l'utilisateur d'entrer une coordonnée valide (X ou Y).
    """
    value = -1
    while value < 0 or value >= max_value:
        try:
            value = int(input(prompt))
            if value < 0 or value >= max_value:
                print(f"Veuillez entrer un nombre entre 0 et {max_value - 1}.")
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")
    return value

def print_message(message):
    """
    Affiche un message à l'utilisateur.
    """
    print(message)