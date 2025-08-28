import time

# Define the players
player = "X"
robot = "O"

# Initialize empty 3x3 board
board = [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    """Prints the current state of the board"""
    print()
    for i, row in enumerate(board):
        print("  | ".join(row))  # Join cells with vertical bars
        if i < 2:  # Add horizontal separator between rows
            print("---+---+---")
    print()

def check_moves(board):
    """Checks if there are any empty cells left (game not over)"""
    return any(cell == " " for row in board for cell in row)

def score(board):
    """
    Evaluates the board state:
    -1 = Player wins
     1 = Robot wins
     0 = Draw
     None = Game still ongoing
    """
    for i in range(3):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return -1 if board[i][0] == player else 1
        # Check columns
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return -1 if board[0][i] == player else 1

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return -1 if board[0][0] == player else 1
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return -1 if board[0][2] == player else 1

    # If no moves left → it's a draw
    if not check_moves(board):
        return 0  

    return None  # Game still ongoing

def minimax(board, position, depth, alpha, beta):
    """
    Minimax algorithm with alpha-beta pruning.
    - Robot is the maximizer (tries to maximize score)
    - Player is the minimizer (tries to minimize score)
    """
    result = score(board)
    if result is not None:
        return result   # Return score if game is over

    # Player's turn (minimizer)
    if not position:
        best = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = player
                    value = minimax(board, True, depth+1, alpha, beta)
                    board[i][j] = ' '  # Undo move
                    best = min(best, value)
                    beta = min(beta, best)
                    if beta <= alpha:  # Alpha-beta cutoff
                        break
        return best

    # Robot's turn (maximizer)
    else:  
        best = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = robot
                    value = minimax(board, False, depth+1, alpha, beta)
                    board[i][j] = ' '  # Undo move
                    best = max(best, value)
                    alpha = max(alpha, best)
                    if beta <= alpha:  # Alpha-beta cutoff
                        break
        return best

def robot_move(board):
    """Finds the best move for the robot using minimax"""
    best_val = -float('inf')
    nxt_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = robot
                moved_val = minimax(board, False, 0, -float('inf'), float('inf'))
                board[i][j] = ' '  # Undo move

                # Choose the move with highest value
                if moved_val > best_val:
                    best_val = moved_val
                    nxt_move = (i, j)

    return nxt_move

def play():
    """Main game loop: Player vs Robot"""
    time.sleep(1.5)
    print("\n Welcome to XO, can you beat the robot? 🤖")
    time.sleep(2.5)
    print_board(board)
    time.sleep(2.5)
    print("\n You are X, the robot is O. Let's play!")
    time.sleep(2.5)

    while True:
        # --- Player Move ---
        try:
            r, c = map(int, input("\n Enter row,col (0-2 each) for X: ").split(','))
        except:
            print("\n Invalid input, use format: row,col (example: 1,2)")
            continue

        # Validate move
        if not (0 <= r < 3 and 0 <= c < 3):
            print("\n Out of range! Use numbers 0,1,2")
            continue
        if board[r][c] != ' ':
            print("\n Invalid move, cell already taken.")
            continue

        # Apply player's move
        board[r][c] = player
        print_board(board)

        # Check win/draw after player's move
        if score(board) == -1:
            print("\n 🎉 You won the game!")
            break
        if not check_moves(board):
            print("\n 🤝 It's a Draw, well played!")
            break

        # --- Robot Move ---
        print("\n Robot is thinking...")
        move = robot_move(board)
        board[move[0]][move[1]] = robot
        print_board(board)

        # Check win/draw after robot's move
        if score(board) == 1:
            print("\n 🤖 Robot won the game!")
            break
        if not check_moves(board):
            print("\n 🤝 It's a Draw, well played!")
            break

# Run game
if __name__ == '__main__':
    play()
