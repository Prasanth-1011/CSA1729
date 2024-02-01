import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")

def check_winner(board, player):
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, is_maximizing):
    scores = {'X': 1, 'O': -1, 'Tie': 0}

    if check_winner(board, 'X'):
        return -1
    elif check_winner(board, 'O'):
        return 1
    elif is_board_full(board):
        return 0

    player = 'O' if is_maximizing else 'X'
    best_score = float('-inf') if is_maximizing else float('inf')

    for i, j in get_empty_cells(board):
        board[i][j] = player
        score = minimax(board, depth + 1, not is_maximizing)
        board[i][j] = ' '

        if is_maximizing:
            best_score = max(best_score, score)
        else:
            best_score = min(best_score, score)

    return best_score

def get_best_move(board):
    best_score = float('-inf')
    best_move = None

    for i, j in get_empty_cells(board):
        board[i][j] = 'O'
        score = minimax(board, 0, False)
        board[i][j] = ' '

        if score > best_score:
            best_score = score
            best_move = (i, j)

    return best_move

def play_tic_tac_toe():
    player_choice = input("Choose Game Mode :\n1. Player vs Player\n2. Player vs Computer\nEnter Choice (1/2) : ")

    if player_choice not in ('1', '2'):
        print("Invalid Choice. Please Enter Either '1' or '2'.")
        return
    
    if(player_choice == '1'):
        player_symbol = input("Player 1 Choose Your Symbol ('X' or 'O'): ").upper()
    else:
        player_symbol = input("Choose Your Symbol ('X' or 'O'): ").upper()

    if player_symbol not in ('X', 'O'):
        print("Invalid Symbol. Please Choose Either 'X' or 'O'.")
        return

    board = [[' ' for _ in range(3)] for _ in range(3)]

    while True:
        print_board(board)
        row = int(input("Enter Row (0, 1, 2): "))
        col = int(input("Enter Column (0, 1, 2): "))

        if board[row][col] != ' ':
            print("Cell Already Occupied. Try Again.")
            continue

        board[row][col] = player_symbol

        if check_winner(board, player_symbol):
            print_board(board)
            if player_choice == '1':
                if player_symbol == 'X':
                    print("Player 1 Wins!")
                else:
                    print("Player 2 Wins!")
            else:
                print("You Win!")
            break

        if is_board_full(board):
            print_board(board)
            print("Match Draw!")
            break

        if player_choice == '1':
            player_symbol = 'O' if player_symbol == 'X' else 'X'
        else:
            print("Computer is Making a Move...")
            player_symbol = 'X' if player_symbol == 'O' else 'O'
            ai_row, ai_col = get_best_move(board)
            board[ai_row][ai_col] = player_symbol

            if check_winner(board, player_symbol):
                print_board(board)
                if player_symbol == 'X':
                    print("Player 1 Wins!")
                else:
                    print("Player 2 Wins!")
                break

            if is_board_full(board):
                print_board(board)
                print("It's a Tie!")
                break

if __name__ == "__main__":
    play_tic_tac_toe()
