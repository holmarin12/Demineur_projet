import time
import os
import platform
import ui
from game import Game
import scores


def effacer_ecran():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def demarrer_jeu(hauteur, largeur, nb_mines, personnalise=False, niveau=None):
    """
    Démarre une partie de démineur.
    """
    jeu = Game(hauteur, largeur, nb_mines)
    jeu.initialiser_grille()
    jeu.calculer_mines_adjacentes()

    jeu_termine = False
    debut_jeu = time.time()  # Capture le temps de début de jeu


    while not jeu_termine:
        effacer_ecran()  # Efface l'écran avant de réafficher la gril
        jeu.afficher_grille()

        action, x, y = ui.obtenir_action_joueur(jeu.hauteur, jeu.largeur)
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
            fin_jeu = time.time()  # Capture le temps de fin de jeu
            temps_ecoule = fin_jeu - debut_jeu
            ui.afficher_message(f"Félicitations ! Vous avez gagné en {temps_ecoule:.2f} secondes !")
            if not personnalise:
                enregistrer_score_apres_victoire(niveau, temps_ecoule, jeu.grille)
            jeu_termine = True

def choisir_et_demarrer_jeu_niveau():
    """
    Permet à l'utilisateur de choisir un niveau et démarre la partie.
    """
    niveau = ui.choisir_niveau()
    if niveau == '4':  # Option pour revenir au menu principal
        return
    elif niveau in ['1', '2', '3']:
        parametres = {
            '1': (9, 9, 10, 'Facile'),
            '2': (16, 16, 40, 'Moyen'),
            '3': (30, 16, 99, 'Difficile')
        }
        hauteur, largeur, nb_mines, niveau_texte = parametres[niveau]
        demarrer_jeu(hauteur, largeur, nb_mines, personnalise=False, niveau=niveau_texte)
    else:
        ui.afficher_message("Niveau non valide. Retour au menu principal.")


def enregistrer_score_apres_victoire(niveau, temps, grille):
    """
    Demande au joueur d'entrer son nom et enregistre le score.
    """
    nom = input("Entrez votre nom pour enregistrer votre score : ")
    scores.enregistrer_score(nom, temps, niveau, grille)

def afficher_scores_et_rejouer():
    """
    Affiche les scores enregistrés et permet à l'utilisateur de choisir une grille à rejouer.
    """
    scores_enregistres = scores.lire_scores()
    for index, score in enumerate(scores_enregistres):
        print(f"{index + 1}. {score['nom']} - {score['temps']:.2f}s - Niveau: {score['niveau']}")

    choix = input("Entrez le numéro de la grille à rejouer, ou 'q' pour quitter : ")
    if choix.lower() == 'q':
        return

    try:
        choix_index = int(choix) - 1
        if 0 <= choix_index < len(scores_enregistres):
            rejouer_grille(scores_enregistres[choix_index])
        else:
            print("Choix non valide.")
    except ValueError:
        print("Veuillez entrer un numéro valide.")

def rejouer_grille(score):
    """
    Lance une partie avec la grille spécifiée dans le score sélectionné.
    """
    niveau = score['niveau']
    hauteur, largeur, nb_mines = determiner_parametres_niveau(niveau)

    jeu = Game(hauteur, largeur, nb_mines)
    jeu.initialiser_grille()
    jeu.calculer_mines_adjacentes()

    jeu_termine = False
    while not jeu_termine:
        jeu.afficher_grille()
        action, x, y = ui.obtenir_action_joueur(jeu.hauteur, jeu.largeur)

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

def determiner_parametres_niveau(niveau):
    """
    Détermine les paramètres de la grille en fonction du niveau de difficulté.
    """
    if niveau == "Facile":
        return 9, 9, 10
    elif niveau == "Moyen":
        return 16, 16, 40
    elif niveau == "Difficile":
        return 30, 16, 99
    else:
        print("Niveau non reconnu")
        return 0, 0, 0  # Valeurs par défaut en cas de niveau non reconnu

def main():
    """
    Fonction principale qui gère le menu principal et les interactions avec l'utilisateur.
    """
    actions_menu = {
        '1': lambda: demarrer_jeu(*ui.obtenir_parametres_jeu(), personnalise=True),
        '2': choisir_et_demarrer_jeu_niveau,
        '3': afficher_scores_et_rejouer,
        '4': lambda: ui.afficher_message("Merci d'avoir joué au Démineur. À bientôt !")
    }

    while True:
        choix = ui.afficher_menu()
        action = actions_menu.get(choix)
        if action:
            action()
        if choix == '4':
            break
        if not action:
            ui.afficher_message("Choix non valide. Veuillez entrer 1, 2, 3 ou 4.")

if __name__ == "__main__":
    main()