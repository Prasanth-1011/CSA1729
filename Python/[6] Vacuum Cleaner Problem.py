import copy
from collections import deque

def print_grid(grid):
    for row in grid:
        print(' '.join(row))
    print()

def find_shortest_path(grid, start):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    shortest_path = []
    visited = set()
    queue = deque([(start, [])])

    while queue:
        (x, y), path = queue.popleft()
        if grid[x][y] == 'D':
            shortest_path = path
            break

        visited.add((x, y))
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in visited and grid[nx][ny] != '#':
                queue.append(((nx, ny), path + [(nx, ny)]))

    return shortest_path

def move_vacuum(grid, path):
    for x, y in path:
        grid[x][y] = 'C'
        print_grid(grid)
        grid[x][y] = 'C'

def main():
    rows, cols = map(int, input("Enter Number of Rows And Columns : ").split())
    grid = [['C' for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        row = input(f"Enter Row {i + 1} : ").strip().split()
        for j in range(cols):
            grid[i][j] = row[j]

    print("Initial Grid : ")
    print_grid(grid)

    start_x, start_y = map(int, input("Enter Initial Position (Mention Row And Column) : ").split())

    shortest_paths = []

    while True:
        shortest_path = find_shortest_path(grid, (start_x, start_y))
        if not shortest_path:
            print("All Cells Cleaned!")
            break

        move_vacuum(grid, shortest_path)
        start_x, start_y = shortest_path[-1]  # Update start position for next move

        # Clean cells visited during the shortest path
        for x, y in shortest_path:
            grid[x][y] = 'C'

        shortest_paths.append(shortest_path)  # Store the shortest path for this move

    print("\nShortest Path :")
    for i, path in enumerate(shortest_paths, 1):
        print(f"Move {i}: {path}")

if __name__ == "__main__":
    main()
