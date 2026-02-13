
def move(unit, new_pos):
    unit.position = new_pos

def attack(attacker, defender):
    defender.health -= attacker.attack
