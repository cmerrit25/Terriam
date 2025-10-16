"""
This file serves as class definition library and is extremely rudimentary. 
I'm planning to make multiple more bosses, enemies and friends for the player to interact with.
Need to make sure that balancing feels good as well.

- Courtney Merritt
"""

class GameState:
    def __init__(self, Player, Nemesis, boss_one=None, boss_two=None, mboss_one=None, mboss_two=None):
        self.player = Player
        self.nemesis = Nemesis
        self.progress = 0
        self.bosses_defeated = 0
        if boss_one:
            self.boss_one = boss_one
        if boss_two:
            self.boss_two = boss_two
        if mboss_one:
            self.mboss_one = mboss_one
        if mboss_two:
            self.mboss_two = mboss_two

    def __str__(self):
        player_stats = str(self.player)
        nemesis_stats = str(self.nemesis)
        plyr_boss_prog = f"The player has defeated {self.bosses_defeated} boss(es).\n"
        if self.player > self.nemesis:
            comp_strength = "The player is currently stronger than the nemesis.\n"
        else:
            comp_strength = "The player is currently weaker than the nemesis...\n"
        return f"{player_stats}{nemesis_stats}{plyr_boss_prog}{comp_strength}"

class Player:
    def __init__(self, name):
        self.name = name
        self.attack = 25
        self.defense = 10
        self.speed = 15
        self.health = 75

    # getter for player name
    @property
    def name(self):
        return self._name
    
    # setter for player name
    @name.setter
    def name(self, value):
        self._name = value

    def __str__(self):
        stats = f"{self.name}'s stats: Max HP - {self.health}, Attack - {self.attack}, Defense - {self.defense}, Speed - {self.speed}\n"
        return stats
    
class Nemesis:
    def __init__(self, name):
        self.name = name
        self.attack = 23
        self.defense = 8
        self.speed = 13
        self.health = 73

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

class Colossus(Boss):

    MULT = {"health": 2.0, "armor": 2.0, "speed": .5, "attack": 1.5}

    def __init__(self):

        # super init module to access parent init variables
        super().__init__()
        self.health = int(self.health * self.MULT["health"])
        self.armor  = int(self.armor * self.MULT["armor"])
        self.speed  = int(self.speed * self.MULT["speed"])
        self.attack = int(self.attack * self.MULT["attack"])

class Vrolux(Boss):

    MULT = {"health": 1.0, "armor": .8, "speed": 2.5, "attack": 1.5}
    def __init__(self):
        super().__init__()
        self.health = int(self.health * self.MULT["health"])
        self.armor  = int(self.armor * self.MULT["armor"])
        self.speed  = int(self.speed * self.MULT["speed"])
        self.attack = int(self.attack * self.MULT["attack"])

class Miniboss():
    def __init__(self):
        self.health = 500
        self.armor = 50
        self.speed = 50
        self.attack = 100

class Sentry(Miniboss):
    MULT = {"health": 2.0, "armor": 2.0, "speed": .5, "attack": 1.5}

    def __init__(self):
        super().__init__()
        self.health = int(self.health * self.MULT["health"])
        self.armor  = int(self.armor * self.MULT["armor"])
        self.speed  = int(self.speed * self.MULT["speed"])
        self.attack = int(self.attack * self.MULT["attack"])

class Reaver(Miniboss):
    MULT = {"health": 1.0, "armor": .8, "speed": 2.5, "attack": 1.5}
    def __init__(self):
        super().__init__()
        self.health = int(self.health * self.MULT["health"])
        self.armor  = int(self.armor * self.MULT["armor"])
        self.speed  = int(self.speed * self.MULT["speed"])
        self.attack = int(self.attack * self.MULT["attack"])