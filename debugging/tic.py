def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False


def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True


def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Input validation
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
        except ValueError:
            print("❌ Invalid input. Please enter numbers only (0, 1, or 2).")
            continue

        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("❌ Invalid move. Row and column must be 0, 1, or 2.")
            continue

        if board[row][col] != " ":
            print("❌ That spot is already taken! Try again.")
            continue

        # Make the move
        board[row][col] = player

        # Check for win
        if check_winner(board):
            print_board(board)
            print(f"🎉 Player {player} wins!")
            break

        # Check for tie
        if is_full(board):
            print_board(board)
            print("🤝 It's a tie!")
            break

        # Switch players
        player = "O" if player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()