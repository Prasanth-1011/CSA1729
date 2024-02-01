def is_valid_state(state):
    missionaries_left, cannibals_left, boat_left = state
    missionaries_right = 3 - missionaries_left
    cannibals_right = 3 - cannibals_left
    
    if missionaries_left < 0 or missionaries_left > 3:
        return False
    if cannibals_left < 0 or cannibals_left > 3:
        return False
    if missionaries_right < 0 or missionaries_right > 3:
        return False
    if cannibals_right < 0 or cannibals_right > 3:
        return False
    if (missionaries_left < cannibals_left) and missionaries_left > 0:
        return False
    if (missionaries_right < cannibals_right) and missionaries_right > 0:
        return False
    return True

def generate_next_states(current_state):
    states = []
    missionaries, cannibals, boat = current_state
    
    for m in range(3):
        for c in range(3):
            if 1 <= m + c <= 2:
                new_state = (missionaries - m, cannibals - c, not boat)
                if is_valid_state(new_state):
                    states.append(new_state)
                    
    return states

def depth_first_search(current_state, visited, path):
    visited.add(current_state)

    if current_state == (0, 0, 0):
        return path

    for next_state in generate_next_states(current_state):
        if next_state not in visited:
            result = depth_first_search(next_state, visited, path + [next_state])
            if result:
                return result

    return None

initial_state = (3, 3, 1)
visited_states = set()
path = depth_first_search(initial_state, visited_states, [initial_state])

if path:
    print("Solution Found : ")
    for state in path:
        missionaries, cannibals, boat = state
        print(f"Missionaries : {missionaries}, Cannibals : {cannibals}, Boat : {'Left' if boat == 0 else 'Right'}")
else:
    print("No Solution Found.")
