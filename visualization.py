
def print_state(state):
    print("Friendly Units:")
    for u in state.friendly:
        print(u.name, u.position, u.health)

    print("Enemy Units:")
    for u in state.enemy:
        print(u.name, u.position, u.health)
