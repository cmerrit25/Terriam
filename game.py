from classes import GameState
from actions import explore, train, fight
from utils import get_player_nemesis, spawn_enemies

def game():
    # start game and grab player + nemesis names
    player, nemesis = get_player_nemesis()

    # spawn enemies
    colosuss, vrolux, sentry, reaver, enemies = spawn_enemies()

    # declare game state
    game_state = GameState(player, nemesis, colosuss, vrolux, sentry, reaver)

    # Game Loop
    # prompt the user for an action
    while True:
        action_choices = ["fight", "explore", "train", "f", "e", "t"]

        action_msg = "Explore? Train? Fight mini-boss? Fight boss?\n"
        user_choice = ""
        while True:
            try:
                user_choice = input(action_msg).lower()
                if user_choice == "quit" or user_choice == "q":
                    return "Player has quit the game..."
                elif user_choice not in action_choices:
                    raise KeyError
            except KeyError:
                print("Invalid action choice. Please choose either \"fight\", \"explore\", or \"train\".\n")
                break

            # check if the player is high enough level to fight regular enemy, miniboss, or boss. Spawn enemy accordingly
            if user_choice == "fight" or user_choice == "f":
                # spawn enemy based on player stats/level
                enemy = ""
                player_win = fight(enemy, game_state)
                if not player_win:
                    print(f"The player lost to {enemy}\n")

            # print game state
            print(game_state)

