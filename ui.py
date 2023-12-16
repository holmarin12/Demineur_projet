def get_game_parameters():
    """
    Demande à l'utilisateur de saisir les paramètres de la partie.
    """
    height = get_valid_input("Entrez la hauteur de la grille (max 30) : ", min_value=1, max_value=30)
    width = get_valid_input("Entrez la largeur de la grille (max 16) : ", min_value=1, max_value=16)
    max_mines = height * width - 1
    num_mines = get_valid_input("Entrez le nombre de mines : ", min_value=1, max_value=max_mines)

    return height, width, num_mines

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
    Demande au joueur de choisir une action et de fournir les coordonnées.
    """
    valid_actions = ['D', 'M']
    action = ''

    while action not in valid_actions:
        action = input("Choisissez une action (découvrir 'D', marquer 'M'): ").strip().upper()
        if action not in valid_actions:
            print("Action non valide. Veuillez entrer 'D' pour découvrir ou 'M' pour marquer.")

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