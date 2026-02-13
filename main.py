
from unit import Unit
from game_state import GameState
from simulator import run_turn
from visualization import print_state

def main():
    friendly = [Unit("F1", (0,0), 10, 3, 1)]
    enemy = [Unit("E1", (2,2), 10, 2, 1)]

    state = GameState(friendly, enemy, True)

    print_state(state)
    run_turn(state)

if __name__ == "__main__":
    main()
