import heuristic_ai
import utils
import player
import minmax

# A mapping of difficulty names to their corresponding player functions
player_map = {
    "human": player.human_player,
    "easy": heuristic_ai.random_ai,
    "medium": heuristic_ai.winning_moves_ai,
    "hard": heuristic_ai.winning_and_losing_moves_ai,
    "very hard": minmax.minmax_ai,
    "impossible": minmax.tie_breaking_minmax_ai
}

def new_board():
    """
    Creates a new empty board using the configured BOARD_WIDTH and BOARD_HEIGHT.
    Returns a 2D list filled with None.
    """
    board = []
    for y in range(utils.BOARD_HEIGHT):
        row = []
        for x in range(utils.BOARD_WIDTH):
            row.append(None)
        board.append(row)
    return board

def render(board) -> None:
    """
    Renders the current board to the console with row and column indices.
    """
    for i in range(-1, len(board)):
        if i == -1:
            for j in range(-1, len(board)):
                if j == -1:
                    print(' ', end=' ')
                else:
                    print(j, end=' ')
        else:
            for j in range(len(board) + 1):
                if j == 0:
                    print(i, end=' ')
                else:
                    cell = board[i][j - 1]
                    print(cell if cell is not None else ' ', end=' ')
        print()

def run_game(x_ai_name, o_ai_name):
    """
    Runs a single game between the selected players.
    """
    board = new_board()
    move_counter = 0
    print("Starting a new game!")
    print("Player X:", x_ai_name)
    print("Player O:", o_ai_name)
    render(board)

    while True:
        current_player = "X" if move_counter % 2 == 0 else "O"
        ai_func = player_map[x_ai_name] if current_player == "X" else player_map[o_ai_name]

        move_co_ords = ai_func(board, current_player)
        board = utils.make_move(board, move_co_ords, current_player)
        render(board)

        winner = utils.get_winner(board)
        if winner is not None:
            print(f"WINNER IS {winner}!!")
            break

        if utils.is_board_full(board):
            print("IT'S A DRAW!!")
            break

        move_counter += 1

def prompt_for_player(player_label):
    """
    Prompts the user to choose a player type by name.
    Returns the selected key from player_map.
    """
    while True:
        choice = input(f"Choose player {player_label} (or 0 to quit): ").strip().lower()
        if choice == "0":
            return "0"
        if choice in player_map:
            return choice
        else:
            print(f"Invalid choice. Available options: {', '.join(player_map.keys())}")

def main():
    """
    Main loop that allows the user to play multiple games with different player types.
    """
    print("Welcome to Tic-Tac-Toe!")
    print("Available player types:", ', '.join(player_map.keys()))
    print("Enter '0' to quit at any time.\n")

    while True:
        x_choice = prompt_for_player("X")
        if x_choice == "0":
            print("Goodbye!")
            break

        o_choice = prompt_for_player("O")
        if o_choice == "0":
            print("Goodbye!")
            break

        run_game(x_choice, o_choice)
        print("\n--- Game Over ---\n")

if __name__ == "__main__":
    main()
