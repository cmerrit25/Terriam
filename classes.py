"""
This file serves as class definition library and is extremely rudimentary. 
I'm planning to make multiple more bosses, enemies and friends for the player to interact with.
Need to make sure that balancing feels good as well.

- Courtney Merritt
"""

import math, random
    
class Nemesis:
    def __init__(self, name):
        self.name = name
        self.stats = {
            "attack": 25,
            "defense": 10,
            "speed": 15,
            "health": 75,
            "evasion": 10
        }

    # getter for nemesis name
    @property
    def name(self):
        return self._name
    
    # setter for nemesis name
    @name.setter
    def name(self, value):
        self._name = value

    def __str__(self):
        stats = f"{self.name}'s stats: Max HP - {self.health}, Attack - {self.attack}, Defense - {self.defense}, Speed - {self.speed}\n"
        return stats

class Boss:
    
    def __init__(self):
        self.health = 1000
        self.armor = 100
        self.speed = 100
        self.attack = 200
        
    def take_damage(self, enemy, damage):
        if enemy.pierce < self.armor:                        # <-------------- determine how to fix inheritance to properly reference Player class functions
            damage /= 2
        self.health -= damage

class Colossus(Boss):

    MULT = {"health": 2.0, "armor": 2.0, "speed": .5, "attack": 1.5}

   
    def __init__(self):

        # super init module to access parent init variables
        super().__init__()
        self.health = int(self.health * self.MULT["health"])
        self.armor  = int(self.armor * self.MULT["armor"])
        self.speed  = int(self.speed * self.MULT["speed"])
        self.attack = int(self.attack * self.MULT["attack"])

        self.moves = {
            "Crushing slam": self.attack * .4
        }

    def __str__(self):
        return f"Colossus HP: {self.health}"
    
    def get_move_damage(self):
        return random.choice(list(self.moves.values()))
    


class Vrolux(Boss):

    MULT = {"health": 1.0, "armor": .8, "speed": 2.5, "attack": 1.5}
    def __init__(self):
        super().__init__()
        self.health = int(self.health * self.MULT["health"])
        self.armor  = int(self.armor * self.MULT["armor"])
        self.speed  = int(self.speed * self.MULT["speed"])
        self.attack = int(self.attack * self.MULT["attack"])

        self.moves = {
            "Vortex Blitz": self.attack * .3
        }

    def __str__(self):
        return f"Vrolux HP: {self.health}"
    
    def get_move_damage(self):
        return random.choice(list(self.moves.values()))

class Miniboss():
    def __init__(self):
        self.health = 500
        self.armor = 50
        self.speed = 50
        self.attack = 100

    def take_damage(self, damage):
        self.health -= damage

class Sentry(Miniboss):
    MULT = {"health": 2.0, "armor": 2.0, "speed": .5, "attack": 1.5}

    def __init__(self):
        super().__init__()
        self.health = int(self.health * self.MULT["health"])
        self.armor  = int(self.armor * self.MULT["armor"])
        self.speed  = int(self.speed * self.MULT["speed"])
        self.attack = int(self.attack * self.MULT["attack"])

        self.moves = {
            "Grounding Crush": self.attack * .3
        }

    def __str__(self):
        return f"Sentry HP: {self.health}"
    
    def get_move_damage(self):
        return random.choice(list(self.moves.values()))
    
class Reaver(Miniboss):
    MULT = {"health": 1.0, "armor": .8, "speed": 2.5, "attack": 1.5}
    def __init__(self):
        super().__init__()
        self.health = int(self.health * self.MULT["health"])
        self.armor  = int(self.armor * self.MULT["armor"])
        self.speed  = int(self.speed * self.MULT["speed"])
        self.attack = int(self.attack * self.MULT["attack"])

        self.moves = {
            "Wrath Slash": self.attack * .3
        }

    def __str__(self):
        return f"Reaper HP: {self.health}"
    
    def get_move_damage(self):
        return random.choice(list(self.moves.values()))
    

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
            "palm strike": self.stats.get("attack") * .4
        }

    # setter for player name
    @name.setter
    def name(self, value):
        self._name = value

    # getter for player name
    @property
    def name(self):
        return self._name
    
    # getter for player stats
    @property
    def stats(self):
        return self.stats

    def __str__(self):
        stats = f"{self.name}'s stats: Max HP - {self.health}, Attack - {self.attack}, Defense - {self.defense}, Speed - {self.speed}\n"
        lvl_data = f"The player is level {self.level} and needs {self.calc_lvl_cost} to get to level {self.level + 1}!\n"
        return f"{stats}{lvl_data}"
    
    # return a random move's damage from the list of player moves
    def get_move_damage(self):
        return random.choice(list(self.moves.values()))
    
    def take_damage(self, enemy: Miniboss | Boss , damage):
        player_death = False
        if self.defense >= enemy.pierce:                    #  <----------- need to add pierce to enemy classes
            damage /= 2
        self.health -= damage
        if self.health <= 0:
            player_death = True
        return player_death

    # gain xp then check if level up is needed
    def gain_xp(self, xp_gained):
        self.xp += xp_gained
        self.level_up()

    # calc xp cost to lelel up
    def calc_lvl_cost(self):
        return 10 * math.pow(2, self.level - 1)
    
    # scale stats by 10 percent
    def scale_stats(self):
        for stat in self.stats.values():
            stat *= 1.1

    # check if level up is needed
    def level_up(self):
        lvl_up_xp = self.calc_lvl_cost()
        
        while self.xp >= lvl_up_xp:
            if self.xp == lvl_up_xp:
                self.xp -= lvl_up_xp
                self.level += 1
                self.scale_stats()

            lvl_up_xp = self.calc_lvl_cost()
        
        print(f"{self.name} has leveled up! Their new level is now {self.level}!")

# collection of current game instance information
class GameState:
    def __init__(self, player: Player, nemesis: Nemesis, boss_one=None, boss_two=None, mboss_one=None, mboss_two=None):
        self.player = player
        self.nemesis = nemesis
        self.progress = 0
        self.bosses_defeated = []
        if boss_one:
            self.boss_one = boss_one
        if boss_two:
            self.boss_two = boss_two
        if mboss_one:
            self.mboss_one = mboss_one
        if mboss_two:
            self.mboss_two = mboss_two

    # print relevant gamestate information to console
    def __str__(self):
        player_stats = str(self.player)
        nemesis_stats = str(self.nemesis)
        plyr_boss_prog = f"The player has defeated {len(self.bosses_defeated)} boss(es).\n"
        if self.player > self.nemesis:
            comp_strength = "The player is currently stronger than the nemesis.\n"
        else:
            comp_strength = "The player is currently weaker than the nemesis...\n"
        return f"{player_stats}{nemesis_stats}{plyr_boss_prog}{comp_strength}"
    
    # adjust player stats from item equip
    # def equip_item(self, item):
    #     player_stats = self.player.get_stats()
    #     item_stats = item.get_stats()
    #     for stat in item_stats.keys():
    #         player_stats[stat] += stat