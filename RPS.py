import random

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    if len(opponent_history) < 4:
        return random.choice(["R", "P", "S"])

    # Track most common 3-pattern from history
    patterns = {}
    for i in range(len(opponent_history) - 3):
        pattern = tuple(opponent_history[i:i+3])
        next_move = opponent_history[i+3]
        if pattern not in patterns:
            patterns[pattern] = {"R": 0, "P": 0, "S": 0}
        patterns[pattern][next_move] += 1

    last_pattern = tuple(opponent_history[-3:])
    if last_pattern in patterns:
        prediction = max(patterns[last_pattern], key=patterns[last_pattern].get)
    else:
        prediction = random.choice(["R", "P", "S"])  # Fallback if pattern not found

    # Counter the predicted move
    counter = {"R": "P", "P": "S", "S": "R"}
    return counter[prediction]
