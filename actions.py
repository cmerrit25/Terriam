from utils import get_item, get_small_enemy, get_large_enemy, get_miniboss, get_boss
import random
from classes import GameState

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
    train_xp = gamestate.player.xp / 4
    gamestate.player.gain_xp(train_xp)
    return

# adjust player object on fight action
def fight(enemy, gamestate: GameState):
    pass