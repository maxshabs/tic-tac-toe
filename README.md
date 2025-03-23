# 🤖 Tic-Tac-Toe AI

A fully playable Tic-Tac-Toe game in Python featuring multiple levels of AI difficulty — from random bots to unbeatable minimax strategy. Challenge your friends or battle the bots!

---

## 🎮 How to Play

1. Clone or download this repository.
2. Make sure you have Python 3 installed.
3. Run the game from your terminal:

   ```bash
   python tictactoe.py
   ```
4. You will be prompted to select a difficulty level for Player X and Player O.
5. After each game, you'll have the option to play again or exit.

### 🧠 Difficulty Levels

- **Human** (`human`)  
  You control the moves via keyboard input.

- **Easy** (`easy`)  
  AI chooses random valid moves.

- **Medium** (`medium`)  
  AI looks for winning moves, but doesn’t block the opponent.

- **Hard** (`hard`)  
  AI tries to win, or block the opponent if they are about to win.

- **Very Hard** (`very hard`)  
  Classic **minimax** AI — plays perfectly assuming the opponent does too.

- **Impossible** (`impossible`)  
  Minimax AI with **heuristic tie-breaking** — prefers smarter-looking moves to increase pressure.

> 💡 *The higher the difficulty, the stronger the AI. “Impossible” is designed to be unbeatable.*


### 📁 Project Structure

- `tictactoe.py`  
  Main entry point. Handles game loop, rendering, and user interaction.

- `player.py`  
  Implements the human player interface (keyboard input and move validation).

- `heuristic_ai.py`  
  Contains simple AI strategies:
  - `random_ai`: picks a random move
  - `winning_moves_ai`: looks for winning moves
  - `winning_and_losing_moves_ai`: tries to win or block opponent

- `minmax.py`  
  Implements advanced AI strategies:
  - `minmax_ai`: perfect play using minimax algorithm
  - `tie_breaking_minmax_ai`: adds heuristic scoring for smarter tie-breaking

- `utils.py`  
  Shared utility functions for move validation, win checking, board creation, etc.

### 🙌 Credits

This project was inspired by Robert Heaton's excellent tutorial:  
**[Programming Projects for Advanced Beginners #3: Tic-Tac-Toe AI](https://robertheaton.com/2018/10/09/programming-projects-for-advanced-beginners-3-b/)**  
His guide provided the foundation for building the game logic, AI strategies, and minimax implementation.

