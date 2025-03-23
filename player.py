import utils

def human_player(board, current_player):
    """
    Prompts a human player for input until a valid move is entered.
    Returns the move as an (x, y) tuple.
    """
    move_co_ords = None
    while True:
        move_co_ords = _get_move()
        if _is_valid_move(board, move_co_ords):
            move_co_ords = int(move_co_ords[0]), int(move_co_ords[1])
            break
        print("Invalid move!")

    return move_co_ords

def _get_move():
    """
    Prompts the user for x and y coordinates as strings.
    Returns them as a tuple of strings.
    """
    x = input("Enter X coordinate: ")
    y = input("Enter Y coordinate: ")
    return x, y

def _is_valid_move(board, move_coords):
    """
    Validates whether the given (x, y) input is a legal move on the board.
    Returns True if it's a valid move, False otherwise.
    """
    try:
        x, y = int(move_coords[0]), int(move_coords[1])
    except ValueError:
        return False

    if not (0 <= x < utils.BOARD_WIDTH and 0 <= y < utils.BOARD_HEIGHT):
        return False

    if board[y][x] is not None:  # Ensure the target cell is empty
        return False

    return True
