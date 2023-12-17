import ui
from game import Game

def main():
    """
    Fonction principale qui gère le menu principal et les interactions avec l'utilisateur.
    """
    while True:
        choix = ui.afficher_menu()

        if choix == '1':
            ui.afficher_message("La partie personnalisable va commencer...")
            demarrer_jeu(personnalise=True)
        elif choix == '2':
            niveau = ui.choisir_niveau()
            demarrer_jeu_niveau(niveau)
        elif choix == '3':
            ui.afficher_message("Merci d'avoir joué au Démineur. À bientôt !")
            break
        else:
            ui.afficher_message("Choix non valide. Veuillez entrer 1, 2 ou 3.")

def demarrer_jeu(personnalise, hauteur=None, largeur=None, nb_mines=None):
    """
    Démarre une partie de démineur. Peut démarrer une partie personnalisée ou basée sur un niveau.
    
    Args:
    personnalise (bool): Si True, démarre une partie personnalisée avec des paramètres demandés à l'utilisateur.
    hauteur, largeur, nb_mines (int): Paramètres de la grille de jeu si la partie n'est pas personnalisée.
    """
    if personnalise:
        hauteur, largeur, nb_mines = ui.obtenir_parametres_jeu()
    
    jeu = Game(hauteur, largeur, nb_mines)
    jeu.initialiser_grille()
    jeu.calculer_mines_adjacentes()

    jeu_termine = False
    while not jeu_termine:
        jeu.afficher_grille()

        action, x, y = ui.obtenir_action_joueur(hauteur, largeur)
        if action == 'D':
            resultat = jeu.decouvrir_case(x, y)
            if resultat is True:
                ui.afficher_message("Boom! Vous avez découvert une mine. Partie perdue.")
                jeu_termine = True
            elif resultat is None:
                ui.afficher_message("Cette case a déjà été découverte ou est marquée (M).")
        elif action == 'M':
            jeu.marquer_mine(x, y)
        elif action == 'R':
            ui.afficher_message("Retour au menu principal.")
            return

        if jeu.verifier_victoire():
            ui.afficher_message("Félicitations ! Vous avez gagné !")
            jeu_termine = True

    ui.afficher_message("Jeu terminé. Merci d'avoir joué !")

def demarrer_jeu_niveau(niveau):
    """
    Démarre une partie de démineur basée sur un niveau de difficulté prédéfini.

    Args:
    niveau (str): Le niveau de difficulté choisi par l'utilisateur.
    """
    niveaux = {
        '1': {'hauteur': 9, 'largeur': 9, 'nb_mines': 10},
        '2': {'hauteur': 16, 'largeur': 16, 'nb_mines': 40},
        '3': {'hauteur': 30, 'largeur': 16, 'nb_mines': 99}
    }

    if niveau in niveaux:
        demarrer_jeu(personnalise=False, **niveaux[niveau])
    else:
        ui.afficher_message("Niveau non valide. Retour au menu principal.")

if __name__ == "__main__":
    main()
