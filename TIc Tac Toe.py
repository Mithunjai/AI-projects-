import time

player = "X"
robot = "O"

board = [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    print()
    for i, row in enumerate(board):
        print("  | ".join(row))
        if i < 2:
            print("---+---+---")
    print()

def check_moves(board):
    return any(cell == " " for row in board for cell in row)

def score(board):
    for i in range(3):
        # rows
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return -1 if board[i][0] == player else 1
        # columns
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return -1 if board[0][i] == player else 1
    # diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return -1 if board[0][0] == player else 1
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return -1 if board[0][2] == player else 1

    if not check_moves(board):
        return 0  # Draw
    return None  # Game still going

def minimax(board, position, depth, alpha, beta):
    result = score(board)
    if result is not None:
        return result   

    if not position:  # player's turn (minimizer)
        best = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = player
                    value = minimax(board, True, depth+1, alpha, beta)
                    board[i][j] = ' '
                    best = min(best, value)
                    beta = min(beta, best)
                    if beta <= alpha:
                        break
        return best
    else:  # robot's turn (maximizer)
        best = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = robot
                    value = minimax(board, False, depth+1, alpha, beta)
                    board[i][j] = ' '
                    best = max(best, value)
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break
        return best

def robot_move(board):
    best_val = -float('inf')
    nxt_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = robot
                moved_val = minimax(board, False, 0, -float('inf'), float('inf'))
                board[i][j] = ' '
                if moved_val > best_val:
                    best_val = moved_val
                    nxt_move = (i, j)

    return nxt_move

def play():
    time.sleep(1.5)
    print("\n Welcome to XO, can you beat the robot? 🤖")
    time.sleep(2.5)
    print_board(board)
    time.sleep(2.5)
    print("\n You are X, the robot is O. Let's play!")
    time.sleep(2.5)

    while True:
        try:
            r, c = map(int, input("\n Enter row,col (0-2 each) for X: ").split(','))
        except:
            print("\n Invalid input, use format: row,col (example: 1,2)")
            continue

        if not (0 <= r < 3 and 0 <= c < 3):
            print("\n Out of range! Use numbers 0,1,2")
            continue
        if board[r][c] != ' ':
            print("\n Invalid move, cell already taken.")
            continue

        board[r][c] = player
        print_board(board)

        if score(board) == -1:
            print("\n 🎉 You won the game!")
            break
        if not check_moves(board):
            print("\n 🤝 It's a Draw, well played!")
            break

        print("\n Robot is thinking...")
        move = robot_move(board)
        board[move[0]][move[1]] = robot
        print_board(board)

        if score(board) == 1:
            print("\n 🤖 Robot won the game!")
            break
        if not check_moves(board):
            print("\n 🤝 It's a Draw, well played!")
            break

if __name__ == '__main__':
    play()
