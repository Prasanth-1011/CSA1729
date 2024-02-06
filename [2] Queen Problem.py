def Safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
            board[i] - i == col - row or \
            board[i] + i == col + row:
            return False
    return True

def Solve(n, row=0, board=[]):
    if row == n:
        return [board[:]]
    Solutions = []
    for col in range(n):
        if Safe(board, row, col):
            board.append(col)
            Solutions += Solve(n, row + 1, board)
            board.pop()
    return Solutions

def Print_Sol(Solution):
    for col in Solution:
        print(''.join(['Q' if i == col else '.' for i in range(len(Solution))]))

N = 4
Solutions = Solve(N)
for Sol in Solutions:
    Print_Sol(Sol)
    print()
print("Total Solutions : ", len(Solutions))

