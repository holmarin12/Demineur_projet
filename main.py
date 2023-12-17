import ui
from game import Game

def main():
    while True:
        choix = ui.display_menu()

        if choix == '1':
            ui.print_message("La partie va commencer...")
            start_game()
        elif choix == '2':
            ui.print_message("Merci d'avoir joué au Démineur. À bientôt !")
            break
        else:
            ui.print_message("Choix non valide. Veuillez entrer 1 ou 2.")

def start_game():
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
                ui.print_message("Cette case a déjà été découverte.")
        elif action == 'M':
            game.mark_mine(x, y)
        elif action == 'R':
            ui.print_message("Retour au menu principal.")
            return  # Sortir de start_game pour retourner au menu

        if game.check_victory():
            ui.print_message("Félicitations ! Vous avez gagné !")
            game_over = True

    ui.print_message("Jeu terminé. Merci d'avoir joué !")

if __name__ == "__main__":
    main()