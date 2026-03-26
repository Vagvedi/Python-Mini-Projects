# Tic Tac Toe Game

A classic two-player Tic Tac Toe game built with Python's Tkinter library.

## 🎮 Description

This is a graphical implementation of the classic Tic Tac Toe game where two players can play against each other on the same computer. The game features a modern, colorful interface with score tracking and visual feedback.

## ✨ Features

- **Two-player gameplay**: Players X and O take turns
- **Visual turn indicators**: Shows whose turn it is with color coding
- **Score tracking**: Keeps track of wins for both players and draws
- **Win detection**: Automatically detects when a player wins
- **Winning line highlighting**: Highlights the winning combination
- **Draw detection**: Identifies when the game ends in a draw
- **New game functionality**: Start a fresh game while keeping scores
- **Reset scores**: Clear all scores and start fresh
- **Modern UI**: Clean, colorful interface with hover effects

## 🚀 How to Run

Since this game uses only Python's built-in Tkinter library, no additional installation is required.

```bash
python tic_tac_toe.py
```

## 🎯 How to Play

1. The game starts with Player X's turn (red color)
2. Click on any empty cell to place your mark
3. Players alternate turns automatically
4. The first player to get 3 marks in a row (horizontally, vertically, or diagonally) wins
5. If all cells are filled and no player wins, the game is a draw
6. Use the "New Game" button to start a fresh game while keeping scores
7. Use the "Reset Scores" button to clear all scores and start over

## 🎨 Interface Elements

- **Game Board**: 3x3 grid of clickable buttons
- **Turn Indicator**: Shows current player's turn with color coding
- **Score Display**: Shows wins for X, O, and number of draws
- **New Game Button**: Resets the board but keeps scores
- **Reset Scores Button**: Clears all scores and resets the game

## 🏆 Winning Conditions

A player wins by getting three of their marks in:
- Any horizontal row
- Any vertical column
- Either diagonal

## 🛠️ Technical Details

- **Language**: Python 3
- **GUI Library**: Tkinter (built-in)
- **Design Pattern**: Object-oriented programming
- **Game Logic**: 2D array for board state management
- **Event Handling**: Button click events for player moves

## 📁 File Structure

```
Tic_Tac_Toe/
├── tic_tac_toe.py    # Main game file
└── README.md         # This file
```

## 🎮 Controls

- **Mouse Click**: Place mark on empty cell
- **New Game Button**: Start fresh game
- **Reset Scores Button**: Clear all scores

## 🌟 Color Scheme

- **Background**: Dark blue-gray (#2c3e50)
- **Player X**: Red (#e74c3c)
- **Player O**: Blue (#3498db)
- **Buttons**: Dark gray (#34495e)
- **Winning Line**: Green (#27ae60)
- **Hover**: Lighter gray (#4a5f7a)

Enjoy playing Tic Tac Toe! 🎉
