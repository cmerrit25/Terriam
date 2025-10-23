"""
This is a rudimentary implementation of action classes to allow the player/user to make moves during the game. 
Currently limited to explore, fight and train. Need to improve readability with proper variable naming.
"""


from utils import get_item, get_small_enemy, get_large_enemy, get_miniboss, get_boss
import random
from classes import GameState, Player, Boss, Miniboss

# defines possible findings on explore action
def explore(gamestate: GameState):

    findings = {
        "item": get_item(),
        "small_enemy": get_small_enemy(),
        "large_enemy": get_large_enemy(),
        "miniboss": get_miniboss(),
        "boss": get_boss()
    }

    find_options = ["item", "small_enemy", "large_enemy", "miniboss", "boss"]
    explore = random.randint(0, len(find_options) - 1)

    found = findings[find_options[explore]]
    plyr_choice(found, find_options[explore], gamestate)

# adjust player object on item find
def plyr_choice(item_found, item_type: str, gamestate: GameState):
    if item_type == "item":
        print(f"{item_found} was found!\n")
        print(item_found)
        choice = input(f"Do you want to keep and equip {item_found}?\n").lower()
        if choice == "yes" or "y":
            # need to implement items class
            # gamestate.equip_item(item_found)
            pass
        else:
            print(f"{item_found} was not equipped...")

# adjust player object on train action
# rudimentary, need to insert minigame or something to reward on success with training xp
def train(gamestate: GameState) -> None:
    # always give a 4th of a level per training
    train_xp = gamestate.player.calc_lvl_cost() / 4
    gamestate.player.gain_xp(train_xp)
    return

# adjust player object on fight action
def fight(enemy: Miniboss | Boss, gamestate: GameState):
    print(enemy)
    # print(gamestate.player.xp)
    player_move = gamestate.player.get_move_damage()
    enemy_move = ""
    if gamestate.player.speed >= enemy.speed:
        enemy.take_damage(player_move.damage)
        if check_for_death(enemy):
            return True                             # return is checking for enemy death here. need to fix to more clearly show logic of winning/losing
        if gamestate.player.evasion > 0:                                                # <----- condense this logic into a function maybe?
            ran_int = random.randint(0, gamestate.player.evasion)
            if ran_int <= gamestate.player.evasion:
                print(f"{gamestate.player.name} dodged {enemy_move}")
            else:
                gamestate.player.take_damage(enemy_move)
                if check_for_death(gamestate.player):
                    return False
    else:
        if gamestate.player.evasion > 0:                                                # <----- condense this logic into a function maybe?
            ran_int = random.randint(0, gamestate.player.evasion)
            if ran_int <= gamestate.player.evasion:
                print(f"{gamestate.player.name} dodged {enemy_move}")
            else:
                gamestate.player.take_damage(enemy_move)
                if check_for_death(gamestate.player):
                    return False
        enemy.take_damage(player_move)
        if check_for_death(enemy):
            return True

# checking for full hp loss of a person/enemy
def check_for_death(entity):
    if entity.health <= 0:
        return True
    return False
    