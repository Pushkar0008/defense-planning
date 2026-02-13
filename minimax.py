
from evaluation import evaluate

def minimax(state, depth, maximizing):
    if depth == 0:
        return evaluate(state)

    if maximizing:
        best = float('-inf')
        for _ in range(1):  # placeholder for actions
            val = minimax(state, depth-1, False)
            best = max(best, val)
        return best
    else:
        best = float('inf')
        for _ in range(1):
            val = minimax(state, depth-1, True)
            best = min(best, val)
        return best
