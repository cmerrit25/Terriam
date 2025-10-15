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
        action_choices = {"fight": fight(game_state), "explore": explore(game_state), "train": train(game_state)}
        action_msg = "Explore? Train? Fight mini-boss? Fight boss?\n"
        user_choice = ""
        while True:
            try:
                user_choice = input(action_msg).lower()
                if user_choice == "quit" or user_choice == "q":
                    return 
                elif user_choice not in action_choices.keys():
                    raise KeyError
                break
            except KeyError:
                print("Invalid action choice. Please choose either \"fight\", \"explore\", or \"train\".")
                
        # modify player/game stats by editing game state
        action = action_choices[user_choice]

        # print game state
        print(game_state)

