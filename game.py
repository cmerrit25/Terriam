from classes import GameState
from actions import explore, train, fight
from utils import get_player_nemesis, spawn_enemies

def game():
    # start game and grab player + nemesis names
    player, nemesis = get_player_nemesis()

    # spawn enemies
    colosuss, vrolux, sentry, reaver, enemies = spawn_enemies()

    # declare game state
    game_state = GameState(player, nemesis, colosuss, vrolux, sentry, reaver, enemies)

    # Game Loop
    # prompt the user for an action
    while True:
        # available action choices
        action_choices = ["fight", "explore", "train", "f", "e", "t"]

        # prompt the user for an action choice
        action_msg = "Explore? Train? Fight?\n"
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

                # tell the player that they have entered the colosseum
                print(f"{game_state.player.name} has entered the colosseum")

                # check if win con has been met

                if len(game_state.bosses_defeated) == 3:
                    print("You've defeated all the bosses. Time for the final boss...")
                    # spawn final boss
                    final_boss = game_state.spawn_enemy("final_bosses")
                    if fight(final_boss, game_state):
                        print("You've beat Terriam!")
                        break
                # ask the player which enemy type they'd like to challenge
                while True: 
                    print("Please choose the enemy type you'd like to fight from the following choices:")
                    enemy_choice = input("Small enemy, Large enemy, Mini-boss, or Boss?")

                    choices ={"Small enemy": "small_enemies", "Large enemy": "large_enemies", "Mini-boss": "minibosses", "Boss": "bosses"}

                    if enemy_choice not in choices.keys():
                        print("Incorrect choice...")
                    else:
                        choice = choices.get(enemy_choice)
                        enemy = game_state.spawn_enemy(choice)
                        break
                # spawn this enemy type then call fight with the enemy and gamestate
                # fight returns whether player lost or won
                player_win, escape = fight(enemy, game_state)

                # break if player lost
                if not player_win:
                    if not escape:
                        print(f"The player lost to {enemy.name}\n")
                        break
                    else:
                        print(f"The player fled the battle...")
                        continue
                else:
                    print(f"The player defeated {enemy.name}\n")

            # if user wants to explore
            elif user_choice == "explore" or user_choice == "e":
                explore(game_state)

            # if user wants to train
            elif user_choice == "train" or user_choice == "t":
                train(game_state)

            # print game state
            print(game_state)

        break
 