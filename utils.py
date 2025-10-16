from classes import Player, Nemesis, Colossus, Vrolux, Sentry, Reaver

def get_player_nemesis():
    start_msg = "Welcome to Terriam, a world of wonder and randomness inspired by the peakness of Terraria and Pokemon!\n"
    print(start_msg)

    player_name = input("Please give me a valid name for your character!\n")
    while True:
        if len(player_name) == 0:
            player_name = input("You didn't input anything. Please give me a valid name for your character!\n")
        elif len(player_name) > 20:
            player_name = input("You gave an input that was longer that 20 characters\
                                Please give me a valid name for your character!\n" )
        else: 
            break

    player = Player(player_name)

    nemesis_name = input("What do you want your nemesis to be called?\n")
    while True:
        if len(nemesis_name) == 0:
            nemesis_name = input("You didn't input anything. Please give me a valid name for your character!\n")
        elif len(player_name) > 20:
            nemesis_name = input("You gave an input that was longer that 20 characters\
                                Please give me a valid name for your character!\n" )
        else: 
            break
        
    nemesis = Nemesis(nemesis_name)

    return player, nemesis

def spawn_enemies():
    enemies = {}

    colosuss = Colossus()
    vrolux = Vrolux()
    bosses = [colosuss, vrolux]
    enemies["bosses"] = bosses

    sentry = Sentry()
    reaver = Reaver()
    minibosses = [sentry, reaver]
    enemies["minibosses"] = minibosses

    return colosuss, vrolux, sentry, reaver, enemies