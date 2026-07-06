import random

HUMAN = "X"
AI = "O"
EMPTY = " "


def create_board():
    return [EMPTY] * 9


def print_board(board):
    def cell(i):
        return board[i] if board[i] != EMPTY else str(i + 1)

    print()
    print(f" {cell(0)} | {cell(1)} | {cell(2)} ")
    print("---+---+---")
    print(f" {cell(3)} | {cell(4)} | {cell(5)} ")
    print("---+---+---")
    print(f" {cell(6)} | {cell(7)} | {cell(8)} ")
    print()


def winner(board):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]

    for a, b, c in winning_combinations:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    return None


def board_full(board):
    return EMPTY not in board


def available_moves(board):
    return [i for i, cell in enumerate(board) if cell == EMPTY]


def find_winning_move(board, player):
    """Return a winning move for player if one exists."""
    for move in available_moves(board):
        board[move] = player
        if winner(board) == player:
            board[move] = EMPTY
            return move
        board[move] = EMPTY
    return None


def best_ai_move(board):
    """A beatable AI with some randomness."""

    moves = available_moves(board)

    if not moves:
        return None

    # 1. Win if possible
    win_move = find_winning_move(board, AI)
    if win_move is not None:
        return win_move

    # 2. Block the player 80% of the time
    block_move = find_winning_move(board, HUMAN)
    if block_move is not None:
        if random.random() < 0.8:
            return block_move

    # 3. Take the center 70% of the time
    if board[4] == EMPTY and random.random() < 0.7:
        return 4

    # 4. Take a random corner 70% of the time
    corners = [i for i in [0, 2, 6, 8] if board[i] == EMPTY]
    if corners and random.random() < 0.7:
        return random.choice(corners)

    # 5. Otherwise choose any random move
    return random.choice(moves)


def get_human_move(board):
    while True:
        try:
            choice = int(input("Choose a square (1-9): "))

            if choice < 1 or choice > 9:
                print("Please enter a number between 1 and 9.")
                continue

            move = choice - 1

            if board[move] != EMPTY:
                print("That square is already taken.")
                continue

            return move

        except ValueError:
            print("Please enter a valid number.")


def announce_result(board):
    result = winner(board)

    print_board(board)

    if result == HUMAN:
        print("🎉 Congratulations! You win!")
    elif result == AI:
        print("🤖 You lose! The AI wins.")
    else:
        print("🤝 It's a tie!")


def play_game():
    board = create_board()

    print("===================================")
    print("      TIC TAC TOE")
    print("===================================")
    print("You are X")
    print("AI is O")
    print("Enter a number (1-9) to make a move.")

    print_board(board)

    while True:
        # Human turn
        move = get_human_move(board)
        board[move] = HUMAN
        print_board(board)

        if winner(board) or board_full(board):
            break

        # AI turn
        ai_move = best_ai_move(board)
        board[ai_move] = AI

        print(f"AI chooses square {ai_move + 1}.")
        print_board(board)

        if winner(board) or board_full(board):
            break

    announce_result(board)


if __name__ == "__main__":
    play_game()