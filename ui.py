def afficher_menu():
    """
    Affiche le menu principal du jeu.
    """

    message_bienvenue = """
    *****************************************************
    *                                                   *
    *      Bienvenue au jeu du Démineur en Python !     *
    *                                                   *
    *****************************************************
    """
    print(message_bienvenue.upper())
    print("Menu du Démineur".upper())
    print()
    print("1. Démarrer une nouvelle partie personnalisable")
    print("2. Démarrer une partie par niveau")
    print("3. Scores partie par niveau")
    print("4. Quitter")
    print()

    while True:
        choix = input("Entrez votre choix (1, 2, 3 ou 4): ")
        if choix in ['1', '2', '3', '4']:
            return choix
        else:
            print("Choix non valide. Veuillez entrer 1, 2, 3 ou 4.")

def obtenir_parametres_jeu():
    """
    Demande à l'utilisateur de saisir les paramètres de la partie.
    Utilise la fonction obtenir_entree_valide pour valider les entrées.
    """
    hauteur = obtenir_entree_valide("Entrez la hauteur de la grille (max 30) : ", valeur_min=1, valeur_max=30)
    largeur = obtenir_entree_valide("Entrez la largeur de la grille (max 16) : ", valeur_min=1, valeur_max=16)
    max_mines = hauteur * largeur - 1
    nb_mines = obtenir_entree_valide("Entrez le nombre de mines : ", valeur_min=1, valeur_max=max_mines)

    return hauteur, largeur, nb_mines

def choisir_niveau():
    """
    Permet à l'utilisateur de choisir un niveau de difficulté pour la partie.
    Ajoute une option pour revenir au menu principal.
    """
    print("Choisissez un niveau de difficulté :")
    print("1. Facile (9x9 avec 10 mines)")
    print("2. Moyen (16x16 avec 40 mines)")
    print("3. Difficile (30x16 avec 99 mines)")
    print("4. Revenir au menu")

    while True:
        niveau = input("Entrez votre choix (1, 2, 3 ou 4): ")
        if niveau in ['1', '2', '3', '4']:
            return niveau
        else:
            print("Choix non valide. Veuillez entrer 1, 2, 3 ou 4.")


def obtenir_entree_valide(invite, valeur_min=0, valeur_max=None):
    """
    Demande à l'utilisateur d'entrer un nombre entier valide.
    Vérifie que la valeur entrée est dans la plage spécifiée.
    """
    while True:
        try:
            valeur = int(input(invite))
            if (valeur >= valeur_min) and (valeur_max is None or valeur <= valeur_max):
                return valeur
            else:
                print(f"Veuillez entrer un nombre entre {valeur_min} et {valeur_max}.")
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

def obtenir_action_joueur(hauteur, largeur):
    """
    Demande au joueur de choisir une action et de fournir les coordonnées.
    Inclut une option pour revenir au menu principal.
    """
    actions_valides = ['D', 'M', 'R']
    action = ''

    while action not in actions_valides:
        action = input("Choisissez une action (Découvrir 'D', Marquer 'M', Revenir au menu 'R'): ").strip().upper()
        if action not in actions_valides:
            print("Action non valide. Veuillez entrer 'D', 'M', ou 'R'.")

    if action == 'R':
        return action, None, None

    x = obtenir_entree_valide("Entrez la coordonnée X (colonne) : ", valeur_min=0, valeur_max=largeur - 1)
    y = obtenir_entree_valide("Entrez la coordonnée Y (ligne) : ", valeur_min=0, valeur_max=hauteur - 1)
    return action, x, y

def afficher_message(message):
    """
    Affiche un message à l'utilisateur.
    """
    print(message)