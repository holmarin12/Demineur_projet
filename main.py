import ui
from game import Game

def main():
    print("Bienvenue dans le jeu de démineur !")
    height, width, num_mines = ui.get_game_parameters()
    game = Game(height, width, num_mines)
    game.initialize_grid()
    game.calculate_adjacent_mines()

    game_over = False
    while not game_over:
        game.print_grid()

        action, x, y = ui.get_player_action(height, width)
        if action == 'D':
            game_over = game.discover_cell(x, y)
        elif action == 'M':
            game.mark_mine(x, y)

        if game.check_victory():
            ui.print_message("Félicitations ! Vous avez gagné !")
            game_over = True

    ui.print_message("Jeu terminé. Merci d'avoir joué !")

if __name__ == "__main__":
    main()