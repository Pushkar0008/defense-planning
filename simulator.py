
from minimax import minimax

def run_turn(state, depth=2):
    score = minimax(state, depth, True)
    print("Predicted utility:", score)
