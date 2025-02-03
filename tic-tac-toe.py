def print_board(board):
    """Prints the tic-tac-toe board with row letters and column numbers outside the grid."""
    print("    1   2   3")  # Column numbers
    print("  -------------")
    row_labels = ["A", "B", "C"]

    for i, row in enumerate(board):
        print(f"{row_labels[i]} | {' | '.join(row)} |")
        print("  -------------")

def check_winner(board, player):
    """Checks if the given player has won."""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    """Checks if the board is full (indicating a tie)."""
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    """Main function to run the tic-tac-toe game."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    row_mapping = {"A": 0, "B": 1, "C": 2}

    turn = 0

    while True:
        print_board(board)
        player = players[turn % 2]

        while True:
            try:
                move = input(f"Player {player}, enter your move (e.g., A1, B3): ").upper().strip()

                if len(move) != 2 or move[0] not in row_mapping or move[1] not in "123":
                    print("❌ Invalid input! Use format A1, B2, etc.")
                    continue

                row = row_mapping[move[0]]
                col = int(move[1]) - 1

                if board[row][col] == " ":
                    break
                else:
                    print("❌ Invalid move! The cell is occupied.")
            except Exception:
                print("❌ Invalid input! Enter a valid move like A1, B2, etc.")

        board[row][col] = player

        if check_winner(board, player):
            print_board(board)
            print(f"🎉 Player {player} wins! 🎉")
            break

        if is_full(board):
            print_board(board)
            print("🤝 It's a tie!")
            break

        turn += 1

# Run the game
tic_tac_toe()
