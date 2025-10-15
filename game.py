from classes import Player, Nemesis, Colossus, Vrolux, Sentry, Reaver

def game():
    # start game and grab player + nemesis names
    start_msg = "Welcome to Terriam, a world of wonder and randomness inspired by the peakness of Terraria!\n"
    print(start_msg)

    player_name = input("Please give me a valid name for your character!")
    player = Player(player_name)

    nemesis_name = input("What do you want your nemesis to be called?")
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

    # prompt the user for an action
    action_choices = {}
    action_msg = "Explore? Train? Fight mini-boss? Fight boss?"
    action = input(action_msg)

    return