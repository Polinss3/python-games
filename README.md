# Python Games 🎮

Welcome to the **Python Games** repository! This project contains implementations of classic 2D games in Python using the **Pygame** library. Each game is contained within its own folder, complete with the main game code, unit tests, and a README file for specific game instructions.

## Project Structure 📂

```plaintext
PYTHON-GAMES/
│
├── Pong/
│   ├── Pong.py         # Main code for the Pong game
│   ├── test_Pong.py    # Unit tests for the Pong game
│   └── README.md       # Documentation for the Pong game
│
├── Snake/
│   ├── Snake.py        # Main code for the Snake game
│   ├── test_Snake.py   # Unit tests for the Snake game
│   └── README.md       # Documentation for the Snake game
│
├── TicTacToe/
│   ├── TicTacToe.py    # Main code for the Tic Tac Toe game
│   ├── test_TicTacToe.py  # Unit tests for the Tic Tac Toe game
│   └── README.md       # Documentation for the Tic Tac Toe game
│
└── README.md           # Global documentation for the repository
```

## Games Included 🕹️

### 1. Pong 🏓
A classic two-player game where each player controls a paddle, and the objective is to hit the ball past the opponent’s paddle to score points. Features include:
- Player-controlled paddle with arrow keys
- AI-controlled opponent paddle
- Ball bouncing off walls and paddles
- Score display

[See the Pong README](Pong/README.md)

### 2. Snake 🐍
A single-player game where the player controls a snake that grows each time it eats food. The objective is to avoid colliding with the snake’s own body or the boundaries. Features include:
- Growing snake with each food item eaten
- Increasing difficulty as the snake grows
- Boundary and self-collision detection
- Score display

[See the Snake README](Snake/README.md)

### 3. Tic Tac Toe ❌⭕
A two-player game (played on the same screen) where the objective is to be the first player to align three of your symbols in a row, column, or diagonal. Features include:
- 3x3 grid display
- Turn-based gameplay for two players
- Win and draw detection
- Console-based interface for simplicity

[See the Tic Tac Toe README](TicTacToe/README.md)

## Requirements 🛠️

Each game requires:
- Python 3.6 or higher
- Pygame library

To install Pygame, run:
```bash
pip install pygame
```

## How to Run Each Game ▶️

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Python-Games.git
    cd Python-Games
    ```

2. Navigate to the desired game folder:
    ```bash
    cd Pong      # or cd Snake, cd TicTacToe
    ```

3. Run the game:
    ```bash
    python Pong.py       # or python Snake.py, python TicTacToe.py
    ```

4. To run the tests:
    ```bash
    python -m unittest test_Pong.py   # or test_Snake.py, test_TicTacToe.py
    ```

## Contributions 🤝

Contributions to improve these games or add new features are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a Pull Request.

## License 📄

This project is licensed under the MIT License. See the LICENSE file for more details.

---

Enjoy playing and exploring classic games with Python! 🎉