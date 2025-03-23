# Board dimensions (used throughout the game)
BOARD_WIDTH = 3
BOARD_HEIGHT = 3

def get_all_valid_moves(board):
    """
    Returns a list of all valid moves (x, y) on the board,
    where a move is valid if the cell is currently empty (None).
    """
    valid = []
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] is None:
                valid.append((x, y))
    return valid

def _check_rows(board):
    """
    Checks each row for a win.
    Returns 'X' or 'O' if any row is filled by the same player.
    Returns None if no winning row is found.
    """
    for row in board:
        first = row[0]
        if first is not None and all(cell == first for cell in row):
            return first
    return None

def _check_cols(board):
    """
    Checks each column for a win.
    Returns 'X' or 'O' if any column is filled by the same player.
    Returns None if no winning column is found.
    """
    for col in range(BOARD_WIDTH):
        first = board[0][col]
        if first is not None and all(board[row][col] == first for row in range(BOARD_HEIGHT)):
            return first
    return None

def _check_diag(board):
    """
    Checks both diagonals for a win:
    - Top-left to bottom-right
    - Top-right to bottom-left
    Returns 'X' or 'O' if any diagonal is filled by the same player.
    Returns None if no winning diagonal is found.
    """
    # Top-left to bottom-right
    first = board[0][0]
    if first is not None and all(board[i][i] == first for i in range(min(BOARD_WIDTH, BOARD_HEIGHT))):
        return first

    # Top-right to bottom-left
    first = board[0][BOARD_WIDTH - 1]
    if first is not None and all(board[i][BOARD_WIDTH - 1 - i] == first for i in range(min(BOARD_WIDTH, BOARD_HEIGHT))):
        return first

    return None

def get_winner(board):
    """
    Returns the winner of the current board, if any.
    Checks rows, columns, and diagonals.
    Returns 'X', 'O', or None if no winner is found.
    """
    return _check_rows(board) or _check_cols(board) or _check_diag(board)

def is_board_full(board):
    """
    Checks whether the board is full (i.e., no empty cells).
    Returns True if full, False otherwise.
    """
    for row in board:
        for pos in row:
            if not pos:
                return False
    return True

def make_move(board, move, player):
    """
    Returns a new board with the given move applied.
    Does not mutate the original board (creates a shallow copy).
    
    Parameters:
    - board: current game board
    - move: (x, y) tuple for move position
    - player: 'X' or 'O'
    """
    new_board = [row.copy() for row in board]
    x, y = move
    new_board[y][x] = player
    return new_board

def get_opponent(player):
    """
    Returns the opponent of the current player.
    If input is 'X', returns 'O'. If 'O', returns 'X'.
    """
    return 'X' if player == 'O' else 'O'
