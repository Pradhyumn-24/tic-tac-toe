# 😀 Introduction 
Welcome to a simple **Tic Tac Toe** game based on Python (3.13.6)!

This game is based on programming concepts of dictionaries and loops.

## 🧠 How to Play Tic Tac Toe (IRL)

Tic Tac Toe is a **two-player strategy game** played on a 3×3 grid.

- **Player 1** uses **X** and **Player 2** uses **O**
- Players take turns marking a square
- The **first player to get three in a row** (horizontally, vertically, or diagonally) **wins!**
- If all 9 squares are filled and nobody wins, it’s a **draw**.

## 🕹️ How to Play This Game (in Python)

### ▶️ Running the Game

Make sure both files `main.py` and `helpers.py` are in the **same folder**.

To run the game, simply execute:

```bash
python main.py
```

### 🎯 Objective

- You and a friend will take turns entering numbers 1–9 to mark your spots.
- Game will end when either of you win or if it's a tie.
- Or you can just quit the game by typing **q**.

### 🔧 How It Works Behind the Scenes

- The game board is a dictionary with keys 1 to 9, representing each position.

- The screen clears after every turn to keep things clean.

- Your input updates the board with either X or O, depending on whose turn it is.

- A helper module helpers.py checks for win conditions and manages the visuals.


Example in-game board (tie):

| O | O | X |
|---|---|---|
| X | X |  O |
| O | X  | X |

## 💡 Fun Fact About Tic Tac Toe

The game is mathematically solved. If both players play optimally, the result will always be a tie!

Want to win more? Try to go first and take the center square – it gives you the highest chance of winning. 😎

## 🙌 Thanks for Playing!
