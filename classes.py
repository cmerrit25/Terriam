"""
This file serves as class definition library and is extremely rudimentary. 
I'm planning to make multiple more bosses, enemies and friends for the player to interact with.
Need to make sure that balancing feels good as well.

- Need to start building items class/list to let the user find things in explore. 10/23

- Courtney Merritt
"""

import math, random
from typing import Dict

class Small_Enemy:
    def __init__(self):
        self.health = 50
        self.armor = 5
        self.speed = 5
        self.attack = 10
        
    def take_damage(self, enemy, damage) -> None:
        if enemy.pierce < self.armor:                        # <-------------- determine how to fix inheritance to properly reference Player class functions
            damage /= 2
        self.health -= damage
        print(f"{enemy.name} dealt {damage} damage to {self.name}")

    def get_move_damage(self) -> tuple[str, float]:
        return random.choice(list(self.moves.items()))
    
class Slime(Small_Enemy):
    def __init__(self):

        # super init module to access parent init variables
        super().__init__()
        self.name = "Slime"
        self.moves = {
            "Slap": self.attack * .4
        }

    def __str__(self) -> None:
        print(self.name)
    
class Large_Enemy:
    def __init__(self):
        self.health = 100
        self.armor = 10
        self.speed = 10
        self.attack = 20

    def take_damage(self, enemy, damage) -> None:
        if enemy.pierce < self.armor:
            damage /= 2
        self.health -= damage
        print(f"{enemy.name} dealt {damage} damage to {self.name}")

    def get_move_damage(self) -> tuple[str, float]:
        return random.choice(list(self.moves.items()))
    
class Ogre(Large_Enemy):
    def __init__(self):

        # super init module to access parent init variables
        super().__init__()
        self.name = "Ogre"
        self.moves = {
            "Stone Charge": self.attack * .4
        }

    def __str__(self) -> None:
        print(self.name)
    
class Nemesis:
    def __init__(self, name: str):
        self.name = name
        self.attack = 25
        self.defense = 10
        self.speed = 15
        self.health = 75
        self.evasion = 10
        self.pierce = 10

        self.combat_power = self.attack + self.defense + self.speed + self.health + self.evasion + self.pierce

    # getter for nemesis name
    @property
    def name(self) -> str:
        return self._name
    
    # setter for nemesis name
    @name.setter
    def name(self, value) -> None:
        self._name = value

    def __str__(self) -> str:
        stats = f"{self.name}'s stats: Max HP - {self.health}, Attack - {self.attack}, Defense - {self.defense}, Speed - {self.speed}\n"
        return stats

class Final_Boss:
    def __init__(self):
        self.health = 3000
        self.armor = 300
        self.speed = 300
        self.attack = 600
        
    def take_damage(self, enemy, damage) -> None:
        if enemy.pierce < self.armor:                        # <-------------- determine how to fix inheritance to properly reference Player class functions
            damage /= 2
        self.health -= damage
        print(f"{enemy.name} dealt {damage} damage to {self.name}")
        return

    def get_move_damage(self) -> tuple[str, float]:
        return random.choice(list(self.moves.items()))
    
class Penetrator(Final_Boss):
    MULT = {"health": 1.0, "armor": .8, "speed": 2.5, "attack": 1.5}
    def __init__(self):
        super().__init__()
        self.name = "The Penetrator"
        self.health = int(self.health * self.MULT["health"])
        self.armor  = int(self.armor * self.MULT["armor"])
        self.speed  = int(self.speed * self.MULT["speed"])
        self.attack = int(self.attack * self.MULT["attack"])

        self.moves = {
            "True Penetrator": self.attack * .3
        }

    def __str__(self) -> str:
        return f"Penetrator HP: {self.health}"
    
    def get_move_damage(self) -> tuple[str, float]:
        return random.choice(list(self.moves.items()))

class Boss:
    
    def __init__(self):
        self.health = 1000
        self.armor = 100
        self.speed = 100
        self.attack = 200
        
    def take_damage(self, enemy, damage) -> None:
        if enemy.pierce < self.armor:                        # <-------------- determine how to fix inheritance to properly reference Player class functions
            damage /= 2
        self.health -= damage
        print(f"{enemy.name} dealt {damage} damage to {self.name}")
        return

    def get_move_damage(self) -> tuple[str, float]:
        return random.choice(list(self.moves.items()))

class Colossus(Boss):

    MULT = {"health": 2.0, "armor": 2.0, "speed": .5, "attack": 1.5}

   
    def __init__(self):

        # super init module to access parent init variables
        super().__init__()
        self.name = "Colossus the Penetrator"
        self.health = int(self.health * self.MULT["health"])
        self.armor  = int(self.armor * self.MULT["armor"])
        self.speed  = int(self.speed * self.MULT["speed"])
        self.attack = int(self.attack * self.MULT["attack"])

        self.moves = {
            "Crushing slam": self.attack * .4
        }

    def __str__(self):
        return f"Colossus HP: {self.health}"
    
    def get_move_damage(self) -> tuple[str, float]:
        return random.choice(list(self.moves.items()))
    


class Vrolux(Boss):

    MULT = {"health": 1.0, "armor": .8, "speed": 2.5, "attack": 1.5}
    def __init__(self):
        super().__init__()
        self.name = "Vrolux the Penetrator"
        self.health = int(self.health * self.MULT["health"])
        self.armor  = int(self.armor * self.MULT["armor"])
        self.speed  = int(self.speed * self.MULT["speed"])
        self.attack = int(self.attack * self.MULT["attack"])

        self.moves = {
            "Vortex Blitz": self.attack * .3
        }

    def __str__(self) -> str:
        return f"Vrolux HP: {self.health}"
    
    def get_move_damage(self) -> tuple[str, float]:
        return random.choice(list(self.moves.items()))

class Miniboss():
    def __init__(self):
        self.health = 500
        self.armor = 50
        self.speed = 50
        self.attack = 100

    def take_damage(self, enemy, damage) -> None:
        if enemy.pierce < self.armor:                        # <-------------- determine how to fix inheritance to properly reference Player class functions
            damage /= 2
        self.health -= damage
        print(f"{enemy.name} dealt {damage} damage to {self.name}")
        return

    def get_move_damage(self) -> tuple[str, float]:
        return random.choice(list(self.moves.items()))

class Sentry(Miniboss):
    MULT = {"health": 2.0, "armor": 2.0, "speed": .5, "attack": 1.5}

    def __init__(self):
        super().__init__()
        self.name = "Sentry the Penetrator"
        self.health = int(self.health * self.MULT["health"])
        self.armor  = int(self.armor * self.MULT["armor"])
        self.speed  = int(self.speed * self.MULT["speed"])
        self.attack = int(self.attack * self.MULT["attack"])

        self.moves = {
            "Grounding Crush": self.attack * .3
        }

    def __str__(self) -> str:
        return f"Sentry HP: {self.health}"
    
    def get_move_damage(self) -> tuple[str, float]:
        return random.choice(list(self.moves.items()))
    
class Reaver(Miniboss):
    MULT = {"health": 1.0, "armor": .8, "speed": 2.5, "attack": 1.5}
    def __init__(self):
        super().__init__()
        self.name = "Reaver the Penetrator"
        self.health = int(self.health * self.MULT["health"])
        self.armor  = int(self.armor * self.MULT["armor"])
        self.speed  = int(self.speed * self.MULT["speed"])
        self.attack = int(self.attack * self.MULT["attack"])

        self.moves = {
            "Wrath Slash": self.attack * .3
        }

    def __str__(self) -> str:
        return f"Reaper HP: {self.health}"
    
    def get_move_damage(self) -> tuple[str, float]:
        return random.choice(list(self.moves.items()))
    

class Player:
    def __init__(self, name):
        self.name = name
       
        self.attack = 25
        self.defense = 10
        self.speed = 15
        self.health = 75
        self.evasion = 10
        self.pierce = 10
        self.xp = 0
        self.level = 1

        self.moves = {
            "palm strike": self.attack * .4
        }

        self.combat_power = self.attack + self.defense + self.speed + self.speed + self.health + self.evasion + self.pierce



        self.energy = 3
        self.energy_max = 3
    # getter for player name
    @property
    def name(self) -> str:
        return self._name
    
    # setter for player name
    @name.setter
    def name(self, value) -> None:
        self._name = value
        return
    
    # getter for player stats
    @property
    def get_stats(self) -> Dict:
        return {
            "attack": self.attack,
            "defense": self.defense,
            "speed": self.speed,
            "health": self.health,
            "evasion": self.evasion,
            "pierce": self.pierce,
            "level": self.level,
            "xp": self.xp
        }

    def __str__(self) -> str:
        stats = f"{self.name}'s stats: Max HP - {self.health}, Attack - {self.attack}, Defense - {self.defense}, Speed - {self.speed}\n"
        lvl_data = f"The player is level {self.level} and needs {self.calc_lvl_cost()} to get to level {self.level + 1}!\n"
        return f"{stats}{lvl_data}"
    
    def show_moves(self) -> None:
        moves = self.moves
        print(f"{self.name}'s moveset:\n")
        for key, value in moves.items():
            print(f"{key}: {value} damage")
        print("\n")
    
    # return a random move's damage from the list of player moves
    def get_move_damage(self, move) -> tuple[str, float]:
        return (move, self.moves[move])
    
    # add energy to player energy pool
    def add_energy(self, energy: int) -> None:
        self.energy += energy
        return 
    
    # take damage from enemy
    def take_damage(self, enemy: Miniboss | Boss | Small_Enemy | Large_Enemy, damage: int) -> bool:
        player_death = False
        if self.defense >= enemy.pierce:                    #  <----------- need to add pierce to enemy classes
            damage /= 2
        self.health -= damage
        if self.health <= 0:
            player_death = True
        print(f"{enemy.name} dealt {damage} damage to {self.name}")
        return player_death

    # gain xp then check if level up is needed
    def gain_xp(self, xp_gained) -> None:
        self.xp += xp_gained
        self.check_level_up()
        return
    
    def escape_energy(self, enemy: Boss | Miniboss | Large_Enemy | Small_Enemy) -> None:

        energy_costs = {
            Boss: 5,
            Miniboss: 3,
            Large_Enemy: 2,
            Small_Enemy: 1
        }

        for enemy_type, energy in energy_costs.items():
            if isinstance(enemy, enemy_type):
                self.energy -= energy
                print(f"You used {energy} to escape this enemy.")
                break

    # calc xp cost to level up
    def calc_lvl_cost(self) -> int:
        return 10 * math.pow(2, self.level - 1)
    
    # scale stats by 10 percent
    def scale_stats(self) -> float:
        for attr in ("attack", "defense", "speed", "health", "evasion", "pierce"):
            setattr(self, attr, int(getattr(self, attr) * 1.1))

        self.energy_max += 1
        self.energy = self.energy_max
        return

    # check if level up is needed
    def check_level_up(self) -> None:
        lvl_up_xp = self.calc_lvl_cost()
        
        while self.xp >= lvl_up_xp:
            if self.xp == lvl_up_xp:
                self.xp -= lvl_up_xp
                self.level += 1
                self.scale_stats()

            lvl_up_xp = self.calc_lvl_cost()
        
        print(f"{self.name} has leveled up! Their new level is now {self.level}!\n")
        return
    
    def level_up(self, levels: int) -> None:
        for _ in range(levels):
            xp_needed = self.calc_lvl_cost()
            self.gain_xp(xp_needed)
        return

    def drain_energy(self) -> None:
        self.energy -= 1
        return
    
    def __eq__(self, other: Nemesis) -> bool:
        if self.combat_power == other.combat_power:
            return True
        return False
    
    def __gt__(self, other: Nemesis) -> bool:
        if self.combat_power > other.combat_power:
            return True
        return False 
    
    def __lt__(self, other: Nemesis) -> bool:
        if self.combat_power < other.combat_power:
            return True
        return False


    

# collection of current game instance information
class GameState:
    def __init__(self, player: Player, nemesis: Nemesis, boss_one=None, boss_two=None, mboss_one=None, mboss_two=None, enemies=None):
        self.player = player
        self.nemesis = nemesis
        self.progress = 0
        self.bosses_defeated = []
        self.enemies = enemies
        if boss_one:
            self.boss_one = boss_one
        if boss_two:
            self.boss_two = boss_two
        if mboss_one:
            self.mboss_one = mboss_one
        if mboss_two:
            self.mboss_two = mboss_two

    # print relevant gamestate information to console
    def __str__(self) -> str:
        player_stats = str(self.player)
        nemesis_stats = str(self.nemesis)
        plyr_boss_prog = f"The player has defeated {len(self.bosses_defeated)} boss(es).\n"
        if self.player > self.nemesis:
            comp_strength = "The player is currently stronger than the nemesis.\n"
        else:
            comp_strength = "The player is currently weaker than the nemesis...\n"
        return f"{player_stats}{nemesis_stats}{plyr_boss_prog}{comp_strength}"
    
    def get_random_enemy(self) -> Boss | Miniboss | Large_Enemy | Small_Enemy:
        enemy_type = random.choice([lst for lst in self.enemies.values()])
        enemy = random.choice(enemy_type)
        return enemy
    
    # adjust player stats from item equip
    # def equip_item(self, item):
    #     player_stats = self.player.get_stats()
    #     item_stats = item.get_stats()
    #     for stat in item_stats.keys():
    #         player_stats[stat] += stat

    def defeat_enemy(self, enemy: Boss | Miniboss | Large_Enemy | Small_Enemy) -> None:
        if isinstance(enemy, Boss):
            self.player.level_up(5)
            self.player.add_energy(5)
            self.bosses_defeated.append(enemy)
        elif isinstance(enemy, Miniboss):
            self.player.level_up(3)
            self.player.add_energy(3)
        elif isinstance(enemy, Large_Enemy):
            self.player.level_up(2)
            self.player.add_energy(2)
        elif isinstance(enemy, Small_Enemy):
            self.player.level_up(1)
            self.player.add_energy(1)

        return

    def spawn_enemy(self, enemy) -> Small_Enemy | Large_Enemy | Miniboss | Boss | Final_Boss:
        return random.choice(self.enemies.get(enemy))