from classes import Player, Nemesis, Colossus, Vrolux, Sentry, Reaver, GameState
from actions import explore, train, fight

def game():
    # start game and grab player + nemesis names
    start_msg = "Welcome to Terriam, a world of wonder and randomness inspired by the peakness of Terraria!\n"
    print(start_msg)

    player_name = input("Please give me a valid name for your character!\n")
    player = Player(player_name)

    nemesis_name = input("What do you want your nemesis to be called?\n")
    nemesis = Nemesis(nemesis_name)

    # spawn enemies
    enemies = {}

    colosuss = Colossus()
    vrolux = Vrolux()
    bosses = [colosuss, vrolux]
    enemies["bosses"] = bosses

    sentry = Sentry()
    reaver = Reaver()
    minibosses = [sentry, reaver]
    enemies["minibosses"] = minibosses
    # declare game state
    game_state = GameState(player, nemesis, colosuss, vrolux, sentry, reaver)

    # game loop 
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

    
    return