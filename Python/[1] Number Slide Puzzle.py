from queue import Queue

def print_puzzle(state):
    for row in state:
        print(" ".join(map(str, row)))
    print()

def move_blank(state, direction):
    new_state = [row.copy() for row in state]
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                if direction == 'up' and i > 0:
                    new_state[i][j], new_state[i-1][j] = new_state[i-1][j], new_state[i][j]
                    return new_state, state[i-1][j]
                elif direction == 'down' and i < len(state) - 1:
                    new_state[i][j], new_state[i+1][j] = new_state[i+1][j], new_state[i][j]
                    return new_state, state[i+1][j]
                elif direction == 'left' and j > 0:
                    new_state[i][j], new_state[i][j-1] = new_state[i][j-1], new_state[i][j]
                    return new_state, state[i][j-1]
                elif direction == 'right' and j < len(state[i]) - 1:
                    new_state[i][j], new_state[i][j+1] = new_state[i][j+1], new_state[i][j]
                    return new_state, state[i][j+1]
    return None, None

def is_goal(state):
    return state == goal_state

def solve_puzzle(initial_state, goal_state):
    visited = set()
    queue = Queue()

    queue.put((initial_state, []))

    while not queue.empty():
        current_state, path = queue.get()

        if is_goal(current_state):
            return path

        if str(current_state) in visited:
            continue

        visited.add(str(current_state))

        for direction in ['up', 'down', 'left', 'right']:
            new_state, swapped_value = move_blank(current_state, direction)
            if new_state:
                new_path = path + [(direction, swapped_value)]
                queue.put((new_state, new_path))

    return None

def get_user_input():
    n = int(input("Enter Number of Grids : "))
    
    print("\nEnter Initial State :")
    initial_state = []
    for _ in range(n):
        row = [int(x) for x in input().split()]
        initial_state.append(row)

    print("\nEnter Goal State :")
    goal_state = []
    for _ in range(n):
        row = [int(x) for x in input().split()]
        goal_state.append(row)

    return initial_state, goal_state

initial_state, goal_state = get_user_input()
solution = solve_puzzle(initial_state, goal_state)

if solution:
    current_state = initial_state
    print("\nInitial State :")
    print_puzzle(current_state)

    for move, swapped_value in solution:
        current_state, _ = move_blank(current_state, move)
        print(f"Swap {swapped_value} With '0' :")
        print_puzzle(current_state)
else:
    print("No Solution Found.")
