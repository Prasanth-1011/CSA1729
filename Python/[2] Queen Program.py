def print_solution(board):
    for row in board:
        print(" ".join(row))
    print()

def is_safe(board, row, col, n):
    # Check if there is a queen in the same row to the left
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    return True

def solve_n_queens_util(board, col, n, solution_count):
    if col == n:
        global total_solutions
        total_solutions += 1
        print_solution(board)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 'Q'
            solve_n_queens_util(board, col + 1, n, solution_count)
            board[i][col] = '.'

def solve_n_queens():
    try:
        n = int(input("Enter Number of Queens : "))
        if n <= 0:
            print("Please Enter Positive Integer.")
            return
    except ValueError:
        print("Invalid Input. Please Enter Valid Integer.")
        return

    global total_solutions
    total_solutions = 0

    board = [['.' for _ in range(n)] for _ in range(n)]
    solve_n_queens_util(board, 0, n, total_solutions)

    print(f"Total Number of Solutions : {total_solutions}")

if __name__ == "__main__":
    solve_n_queens()
