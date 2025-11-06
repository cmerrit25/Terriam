"""
This is a rudimentary implementation of action classes to allow the player/user to make moves during the game. 
Currently limited to explore, fight and train. Need to improve readability with proper variable naming.

Need to implement player move selection.
"""


from utils import get_item, get_small_enemy, get_large_enemy, get_miniboss, get_boss
import random
from classes import GameState, Player, Boss, Miniboss, Small_Enemy, Large_Enemy, Slime, Ogre

# defines possible findings on explore action
def explore(gamestate: GameState) -> None:
    # possible things to find on explore
    findings = {
        "item": get_item(),
        "small_enemy": get_small_enemy(),
        "large_enemy": get_large_enemy(),
        "miniboss": get_miniboss(),
        "boss": get_boss()
    }

    # choosing a random object type
    find_options = ["item", "enemy"]
    explore = random.randint(0, len(find_options) - 1)

    # object found 
    found = findings[find_options[explore]]

    # prompting player if they want to interact with the found object
    plyr_choice(found, find_options[explore], gamestate)

# adjust player object on item find
def plyr_choice(item_found, item_type: str, gamestate: GameState) -> None:
    match item_type:
        case "item":
            print(f"{item_found} was found!\n")
            print(item_found)
            choice = input(f"Do you want to keep and equip {item_found}?\n").lower()
            if choice == "yes" or "y":
                # need to implement items class
                # gamestate.equip_item(item_found)
                pass
            else:
                print(f"{item_found} was not equipped...")  

        case "enemy":
            enemy = gamestate.get_random_enemy()   
            player_prompt = input(f"You've encountered a {enemy}. Do you want to fight it?").lower()
            while True:
                if player_prompt not in ["yes", "no", "y", "n"]:
                    print("Please enter yes, y, no, or n to answer this prompt.")
                    player_prompt = input() 
                    break
            if player_prompt == "yes" or player_prompt == "y":
                fight(enemy, gamestate) 
            else:
                gamestate.player.escape_energy(enemy)
                # can you different amounts of energy to escape different enemies 
                     
                                                          # <------ need to add other options here
# adjust player object on train action
# rudimentary, need to insert minigame or something to reward on success with training xp
def train(gamestate: GameState) -> None:
    # always give a 4th of a level per training
    if gamestate.player.energy > 0:
        prompt = input(f"You have {gamestate.player.energy} energy left. Do you want to spend an energy to train?\n").lower()
        if prompt == "yes" or prompt == "y":
            gamestate.player.drain_energy()

            train_xp = gamestate.player.calc_lvl_cost() / 4

            starting_xp = gamestate.player.xp
            gamestate.player.gain_xp(train_xp)
            ending_xp = gamestate.player.xp

            xp_gained = ending_xp - starting_xp

            print(f"The player gained {xp_gained} xp from training.\n")
            return

    else:
        print(f"{gamestate.player.name} is out of energy! Please wait until level up for a refresh...\n")
        return
    
# adjust player object on fight action, right now moves are random but should be selected by user
def fight(enemy: Miniboss | Boss | Small_Enemy | Large_Enemy, gamestate: GameState) -> bool:
    # print enemy health
   

    # player and enemy fight until one dies
    while True:

        print(f"{enemy.name}'s HP: {enemy.health}")
    # print player health
        print(f"{gamestate.player.name}'s HP: {gamestate.player.health}\n")
        # grab player move name and damage

        gamestate.player.show_moves()
        # prompt player for choose move from moveset, make sure moves have PP
    
        while True:
            print("Please choose a move\n")

            move_choice = input()

            if move_choice not in gamestate.player.moves.keys():    

                print("That's not a valid move choice. Please choose again...\n")
            
            else:
                break



        player_move, player_damage = gamestate.player.get_move_damage(move_choice)

        # grab enemy move name and damage
        enemy_move, enemy_damage = enemy.get_move_damage()

        # the player hits and then enemy hits
        if gamestate.player.speed >= enemy.speed:
            enemy.take_damage(gamestate.player, player_damage)
            if check_for_death(enemy):
                gamestate.defeat_enemy(enemy)
                return True                             # return is checking for enemy death here. need to fix to more clearly show logic of winning/losing
            
            # evasion/dodge calc
            if gamestate.player.evasion > 0:                                                
                ran_int = random.randint(0, gamestate.player.evasion)
                if ran_int <= gamestate.player.evasion:
                    print(f"{gamestate.player.name} dodged {enemy_move}")
                else:
                    gamestate.player.take_damage(enemy, enemy_damage)
                    if check_for_death(gamestate.player):
                        return False
                    
        # the enemy hits and then the player hits
        else:
            # evasion/dodge calc
            if gamestate.player.evasion > 0:                                                # <----- condense this logic into a function maybe?
                ran_int = random.randint(0, gamestate.player.evasion)
                if ran_int <= gamestate.player.evasion:
                    print(f"{gamestate.player.name} dodged {enemy_move}")
                else:
                    gamestate.player.take_damage(enemy, enemy_damage)
                    if check_for_death(gamestate.player):
                        return False
            enemy.take_damage(gamestate.player, player_damage)
            if check_for_death(enemy):
                gamestate.defeat_enemy(enemy)
                return True

# checking for full hp loss of a person/enemy
def check_for_death(entity: Player | Miniboss | Boss) -> bool:
    if entity.health <= 0:
        return True
    return False

# could factor out evasion calculation logic
def evasion_calc(gamestate: GameState):
    pass
    