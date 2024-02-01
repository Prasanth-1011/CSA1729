from collections import deque

def canMeasureWater(jug1Capacity, jug2Capacity, targetCapacity):
    visited = set()  # To keep track of visited states
    queue = deque([(0, 0, [])])  # Initial state with an empty list to store steps

    while queue:
        current_state = queue.popleft()
        jug1, jug2, steps = current_state

        # Check if the target capacity is achieved
        if jug1 + jug2 == targetCapacity or jug1 == targetCapacity or jug2 == targetCapacity:
            steps.append(f"Reached Target Capacity of {targetCapacity} Litres")
            return True, steps

        # Try all possible operations: Fill jug1, Fill jug2, Empty jug1, Empty jug2,
        # Pour water from jug1 to jug2, Pour water from jug2 to jug1
        next_states = [
            (jug1Capacity, jug2, steps + [f"Fill Jug 1 With {jug1Capacity} Litres"]), 
            (jug1, jug2Capacity, steps + [f"Fill Jug 2 With {jug2Capacity} Litres"]),
            (0, jug2, steps + ["Empty jug1"]),
            (jug1, 0, steps + ["Empty jug2"]),
            (min(jug1 + jug2, jug1Capacity), max(0, jug1 + jug2 - jug1Capacity), steps + ["Pour Water From jug 2 - Jug 1"]),  # Pour jug1 to jug2
            (max(0, jug1 + jug2 - jug2Capacity), min(jug1 + jug2, jug2Capacity), steps + ["Pour Water From Jug 1 - Jug 2"])   # Pour jug2 to jug1
        ]

        for next_state in next_states:
            if next_state[:2] not in visited:
                visited.add(next_state[:2])
                queue.append(next_state)

    return False, []

A = int(input("Enter Capacity of Jug 1 : "))
B = int(input("Enter Capacity of Jug 2 : "))
C = int(input("Enter Target Capacity : "))

success, steps = canMeasureWater(A, B, C)
print(success)
if success:
    for step in steps:
        print(step)
