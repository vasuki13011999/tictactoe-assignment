
#### Assignment-4 for Python Internship ###

def main():
    # Main function to run the Tic Tac Toe game
    introduction()
    board = create_grid()
    symbol_1, symbol_2 = get_symbols()
    play_game(board, symbol_1, symbol_2)


def introduction():
    ###Prints the game rules and waits for the user to press Enter to continue.
    # Introduces the rules of the game
    print("Hello! Welcome to Tic Tac Toe!")
    print("Rules: Player 1 and Player 2 take turns marking spaces in a 3x3 grid.")
    print("The player who succeeds in placing three of their marks in a row (horizontally, vertically, or diagonally) wins.")
    input("Press Enter to continue...")
    print()


def create_grid():
    # Creates a blank playboard
    ####Creates a 3x3 grid initialized with empty spaces.
    return [[" " for _ in range(3)] for _ in range(3)]


def get_symbols():
    # Prompts Player 1 to choose a symbol (X or O) and assigns the other symbol to Player 2. Ensures valid input.
    symbol_1 = input("Player 1, choose your symbol (X or O): ").upper()
    if symbol_1 not in ["X", "O"]:
        print("Invalid choice. Defaulting to X.")
        symbol_1 = "X"
    symbol_2 = "O" if symbol_1 == "X" else "X"
    print(f"Player 2, you are {symbol_2}.")
    input("Press Enter to continue...")
    return symbol_1, symbol_2


def print_board(board):
    # Prints the board in a readable format
    print("---+---+---")
    for row in board:
        print(" | ".join(row))
        print("---+---+---")


def is_winner(board, symbol):
    # Checks if the given symbol has won the game
    win_conditions = (
        # Rows
        [board[0], board[1], board[2]],
        # Columns
        [[board[0][0], board[1][0], board[2][0]],
         [board[0][1], board[1][1], board[2][1]],
         [board[0][2], board[1][2], board[2][2]]],
        # Diagonals
        [[board[0][0], board[1][1], board[2][2]],
         [board[0][2], board[1][1], board[2][0]]]
    )

    for condition in win_conditions:
        for line in condition:
            if line.count(symbol) == 3:
                return True
    return False


def is_board_full(board):
    # Checks if the board is full (no empty spaces).
    return all(cell != " " for row in board for cell in row)


def get_move():
    # Prompts the player for a valid row and column and returns the chosen move.
    while True:
        try:
            row = int(input("Pick a row (0, 1, 2): "))
            col = int(input("Pick a column (0, 1, 2): "))
            if row in range(3) and col in range(3):
                return row, col
            else:
                print("Invalid input. Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def play_game(board, symbol_1, symbol_2):
    # Manages the game play
    turn_count = 0
    current_symbol = symbol_1

    while not is_board_full(board):
        print_board(board)
        print(f"Player {current_symbol}, it's your turn.")
        
        row, col = get_move()
        if board[row][col] == " ":
            board[row][col] = current_symbol
            if is_winner(board, current_symbol):
                print_board(board)
                print(f"Player {current_symbol} wins!")
                return
            current_symbol = symbol_2 if current_symbol == symbol_1 else symbol_1
            turn_count += 1
        else:
            print("This cell is already taken. Try again.")

    print_board(board)
    print("The board is full. It's a tie!")


if __name__ == "__main__":
    main()
