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
        # available action choices
        action_choices = ["fight", "explore", "train", "f", "e", "t"]

        # prompt the user for an action choice
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
                # spawn enemy based on player stats/level, right now spawn a boss
                enemy = game_state.boss_one

                # fight returns whether player lost or won
                player_win = fight(enemy, game_state)

                # break if player lost
                if not player_win:
                    print(f"The player lost to {enemy.name}\n")
                    break
                else:
                    print(f"The player defeated {enemy.name}\n")
                    for _ in range(2):
                        lvl_xp = game_state.player.calc_lvl_cost()
                        game_state.player.gain_xp(lvl_xp)
                    print(f"The player has been rewarded with two levels!")

            # if user wants to explore
            elif user_choice == "explore" or user_choice == "e":
                pass

            # if user wants to train
            elif user_choice == "train" or user_choice == "t":
                pass


            # print game state
            print(game_state)

