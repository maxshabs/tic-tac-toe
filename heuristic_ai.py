import utils
import random

def random_ai(board, current_player):
    """
    Returns a random valid move for the current player.
    """
    return _random_move(board)

def winning_moves_ai(board, current_player):
    """
    Checks for a winning move; if found, plays it.
    Otherwise, returns a random move.
    """
    move = _find_winning_move(board, current_player)
    return move if move else _random_move(board)

def winning_and_losing_moves_ai(board, current_player):
    """
    Tries to win if possible.
    If not, tries to block the opponent’s winning move.
    Otherwise, returns a random move.
    """
    move = _find_winning_move(board, current_player)
    if move:
        return move

    move = _find_blocking_move(board, current_player)
    if move:
        return move

    return _random_move(board)

def _random_move(board):
    """
    Helper function to select a random valid move.
    """
    valid_moves = utils.get_all_valid_moves(board)
    return random.choice(valid_moves)

def _find_winning_move(board, current_player):
    """
    Searches all valid moves and returns one that would
    win the game for current_player. Returns None if no such move exists.
    """
    valid_moves = utils.get_all_valid_moves(board)

    for move in valid_moves:
        x, y = move
        test_board = [row.copy() for row in board]
        test_board[y][x] = current_player
        if utils.get_winner(test_board) == current_player:
            return move

    return None

def _find_blocking_move(board, current_player):
    """
    Searches all valid moves and returns one that would block the opponent’s
    winning move. Returns None if no such move exists.
    """
    valid_moves = utils.get_all_valid_moves(board)
    opponent = 'O' if current_player == 'X' else 'X'

    for move in valid_moves:
        x, y = move
        test_board = [row.copy() for row in board]
        test_board[y][x] = opponent
        if utils.get_winner(test_board) == opponent:
            return move

    return None
