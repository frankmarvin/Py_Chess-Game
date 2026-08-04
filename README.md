# ♟️ Python Chess Game

A desktop chess board game built entirely with **Python**.

The project is designed to provide a complete chess experience with a graphical interface, chess rules, player controls, and eventually a computer opponent.

## 🚀 Features

The game will include:

* ♟️ Complete 8×8 chess board
* 👑 All standard chess pieces
* 🖱️ Mouse-based piece selection
* ♜ Legal chess movement
* ⚔️ Piece capturing
* 👑 Check and checkmate detection
* 🤝 Stalemate and draw detection
* 🔄 Restart game
* ↩️ Undo moves
* 📝 Move history
* ⏱️ Chess timer
* 🤖 Computer/AI opponent
* 🎨 Clean and responsive chess interface

## 🛠️ Technologies

The project uses Python only.

### Main Technology

* **Python 3**
* **Pygame** — graphical interface and game window

## 📁 Project Structure

```text
chess_game/
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── game/
│   ├── __init__.py
│   ├── board.py
│   ├── piece.py
│   ├── player.py
│   └── game.py
│
├── ui/
│   ├── __init__.py
│   ├── board_view.py
│   └── menu.py
│
├── utils/
│   ├── __init__.py
│   └── constants.py
│
└── tests/
    ├── __init__.py
    └── test_board.py
```

## ⚙️ Installation

First, make sure Python 3 is installed on your computer.

Check your Python version:

```bash
python --version
```

Install the required package:

```bash
pip install -r requirements.txt
```

Or install Pygame directly:

```bash
pip install pygame
```

## ▶️ Running the Game

From the project folder, run:

```bash
python main.py
```

The chess game window will then open.

## 🧪 Running Tests

To run the project tests:

```bash
python -m unittest discover
```

## 👥 Game Modes

The planned game modes are:

### Player vs Player

Two players play against each other on the same computer.

### Player vs Computer

A player can compete against a computer-controlled opponent.

## 📌 Project Goal

The goal of this project is to create a complete, playable chess game using Python while keeping the code organized, readable, and easy to extend.

---

## 👨‍💻 Development

This project is being developed incrementally, with each part of the chess system separated into its own Python module.

**Built with ❤️ using Python.**
