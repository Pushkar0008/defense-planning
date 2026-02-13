
class Unit:
    def __init__(self, name, position, health, attack, range_):
        self.name = name
        self.position = position
        self.health = health
        self.attack = attack
        self.range = range_

    def is_alive(self):
        return self.health > 0
