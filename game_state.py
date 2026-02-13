
class GameState:
    def __init__(self, friendly, enemy, friendly_turn=True):
        self.friendly = friendly
        self.enemy = enemy
        self.friendly_turn = friendly_turn

    def clone(self):
        import copy
        return copy.deepcopy(self)
