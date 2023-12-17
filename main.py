import ui
from game import Game

def main():
    """
    Fonction principale qui gère le menu principal et les interactions avec l'utilisateur.
    """
    while True:
        choix = ui.display_menu()

        if choix == '1':
            ui.print_message("La partie personnalisable va commencer...")
            start_game(custom=True)
        elif choix == '2':
            niveau = ui.choose_level()
            start_level_game(niveau)
        elif choix == '3':
            ui.print_message("Merci d'avoir joué au Démineur. À bientôt !")
            break
        else:
            ui.print_message("Choix non valide. Veuillez entrer 1, 2 ou 3.")

def start_game(custom, height=None, width=None, num_mines=None):
    """
    Démarre une partie de démineur. Peut démarrer une partie personnalisée ou basée sur un niveau.
    
    Args:
    custom (bool): Si True, démarre une partie personnalisée avec des paramètres demandés à l'utilisateur.
    height, width, num_mines (int): Paramètres de la grille de jeu si la partie n'est pas personnalisée.
    """
    if custom:
        height, width, num_mines = ui.get_game_parameters()
    
    game = Game(height, width, num_mines)
    game.initialize_grid()
    game.calculate_adjacent_mines()

    game_over = False
    while not game_over:
        game.print_grid()

        action, x, y = ui.get_player_action(height, width)
        if action == 'D':
            result = game.discover_cell(x, y)
            if result is True:
                ui.print_message("Boom! Vous avez découvert une mine. Partie perdue.")
                game_over = True
            elif result is None:
                ui.print_message("Cette case a déjà été découverte ou est marquée (M).")
        elif action == 'M':
            game.mark_mine(x, y)
        elif action == 'R':
            ui.print_message("Retour au menu principal.")
            return

        if game.check_victory():
            ui.print_message("Félicitations ! Vous avez gagné !")
            game_over = True

    ui.print_message("Jeu terminé. Merci d'avoir joué !")

def start_level_game(niveau):
    """
    Démarre une partie de démineur basée sur un niveau de difficulté prédéfini.

    Args:
    niveau (str): Le niveau de difficulté choisi par l'utilisateur.
    """
    levels = {
        '1': {'height': 9, 'width': 9, 'num_mines': 10},
        '2': {'height': 16, 'width': 16, 'num_mines': 40},
        '3': {'height': 30, 'width': 16, 'num_mines': 99}
    }

    if niveau in levels:
        start_game(custom=False, **levels[niveau])
    else:
        ui.print_message("Niveau non valide. Retour au menu principal.")

if __name__ == "__main__":
    main()