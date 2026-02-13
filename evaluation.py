
def evaluate(state):
    friendly_health = sum(u.health for u in state.friendly if u.is_alive())
    enemy_health = sum(u.health for u in state.enemy if u.is_alive())
    return friendly_health - enemy_health
