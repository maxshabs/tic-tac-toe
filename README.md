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
You will be prompted to select a difficulty level for Player X and Player O.

After each game, you'll have the option to play again or exit.

🧠 Difficulty Levels
Name	Command	Description
Human	human	You control the moves through keyboard input
Easy	easy	AI picks random valid moves
Medium	medium	AI tries to win if it can
Hard	hard	AI tries to win or block the opponent from winning
Very Hard	very hard	Classic minimax AI — plays perfectly assuming the opponent does too
Impossible	impossible	Minimax AI with heuristic tie-breaking — prefers smarter-looking moves
💡 The higher the difficulty, the less likely you are to win. Good luck beating “impossible”!

🛠 Project Structure
tictactoe.py — Main entry point and game loop

player.py — Handles human player input

heuristic_ai.py — Rule-based AI logic (easy/medium/hard)

minmax.py — Minimax and heuristic-based AIs (very hard/impossible)

utils.py — Shared functions: board generation, move logic, winner checking
