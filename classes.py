"""
This file serves as class definition library and is extremely rudimentary. 
I'm planning to make multiple more bosses, enemies and friends for the player to interact with.
Need to make sure that balancing feels good as well.

- Courtney Merritt
"""

class Player:
    def __init__(self, name):
        self.name = name

    # getter for player name
    @property
    def name(self):
        return self._name
    
    # setter for player name
    @name.setter
    def name(self, value):
        self._name = value
    
class Nemesis:
    def __init__(self, name):
        self.name = name

    # getter for nemesis name
    @property
    def name(self):
        return self._name
    
    # setter for nemesis name
    @name.setter
    def name(self, value):
        self._name = value

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