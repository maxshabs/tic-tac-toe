import utils

def minmax_ai(board, current_player):
    """
    Standard minmax AI: chooses the move that leads to the best guaranteed outcome,
    assuming both players play perfectly.

    Returns the (x, y) move with the best minmax score.
    """
    best_move = None
    best_score = None

    moves = utils.get_all_valid_moves(board)
    opponent = utils.get_opponent(current_player)

    for move in moves:
        new_board = utils.make_move(board, move, current_player)
        score = _minmax_score(new_board, opponent, current_player)
        if best_score is None or score > best_score:
            best_score = score
            best_move = move

    return best_move

def tie_breaking_minmax_ai(board, current_player):
    """
    Enhanced minmax AI: adds a heuristic tie-breaker to prefer smarter-looking moves
    when multiple options yield the same minmax score.

    Returns the (x, y) move with the best combination of score and heuristic.
    """
    best_move = None
    best_score = None
    best_heuristic = None
    opponent = utils.get_opponent(current_player)

    for move in utils.get_all_valid_moves(board):
        new_board = utils.make_move(board, move, current_player)
        score, heuristic = _tie_breaking_minmax_score(new_board, opponent, current_player)

        if best_score is None or score > best_score:
            best_score = score
            best_heuristic = heuristic
            best_move = move
        elif score == best_score and heuristic > best_heuristic:
            best_heuristic = heuristic
            best_move = move

    return best_move

def _minmax_score(board, turn, original_player):
    """
    Core recursive function for minmax. Returns the minmax score for the given board.
    Positive = good for original_player, Negative = good for opponent.
    """
    winner = utils.get_winner(board)
    if winner == original_player:
        return 10
    elif winner == utils.get_opponent(original_player):
        return -10
    elif utils.is_board_full(board):
        return 0

    legal_moves = utils.get_all_valid_moves(board)
    scores = []

    for move in legal_moves:
        new_board = utils.make_move(board, move, turn)
        opponent = utils.get_opponent(turn)
        score = _minmax_score(new_board, opponent, original_player)
        scores.append(score)

    return max(scores) if turn == original_player else min(scores)

def _tie_breaking_minmax_score(board, turn, original_player):
    """
    minmax with heuristic scoring to break ties between equal score moves.
    Returns a tuple: (minmax score, heuristic score).
    """
    winner = utils.get_winner(board)
    if winner == original_player:
        return 10, 0
    elif winner is not None:
        return -10, 0
    elif utils.is_board_full(board):
        return 0, 0

    scores = []
    for move in utils.get_all_valid_moves(board):
        new_board = utils.make_move(board, move, turn)
        opponent = utils.get_opponent(turn)
        score, heuristic = _tie_breaking_minmax_score(new_board, opponent, original_player)
        scores.append((move, score, heuristic))

    if turn == original_player:
        max_score = max(scores, key=lambda x: x[1])[1]
        best_moves = [s for s in scores if s[1] == max_score]
        best = max(best_moves, key=lambda x: x[2])
    else:
        min_score = min(scores, key=lambda x: x[1])[1]
        best_moves = [s for s in scores if s[1] == min_score]
        best = min(best_moves, key=lambda x: x[2])

    return best[1], _heuristic_score(board, original_player)

def _heuristic_score(board, player):
    """
    Returns a tie-breaking heuristic score for the board from the perspective of `player`.
    Higher scores represent more "clever" positions:
    - Occupying corners
    - Controlling the center
    - Having 2 in a row
    """
    score = 0

    # Prefer corners
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    for x, y in corners:
        if board[y][x] == player:
            score += 1

    # Prefer center
    if board[1][1] == player:
        score += 2

    # Prefer having 2 in a row with 1 empty (potential threat)
    for row in board:
        if row.count(player) == 2 and row.count(None) == 1:
            score += 3

    return score
