# Python Games Collection 🎮

Welcome to the **Python Games Collection** repository! This project contains implementations of classic games in Python, using **Pygame** for an interactive and fun experience. Each game is contained within its own folder, complete with the main game code, unit tests, and detailed instructions for playing. Whether you’re looking to enjoy these classic games or learn from their code, this collection has something for everyone!

## Project Structure 📂

```plaintext
Python-Games-Collection/
│
├── GuessTheNumber/
│   ├── GuessTheNumber.py         # Main code for the Guess The Number game
│   ├── test_GuessTheNumber.py    # Unit tests for the Guess The Number game
│   └── README.md                 # Documentation for the Guess The Number game
│
├── Pong/
│   ├── Pong.py                   # Main code for the Pong game
│   ├── test_Pong.py              # Unit tests for the Pong game
│   └── README.md                 # Documentation for the Pong game
│
├── Snake/
│   ├── Snake.py                  # Main code for the Snake game
│   ├── test_Snake.py             # Unit tests for the Snake game
│   └── README.md                 # Documentation for the Snake game
│
├── TicTacToe/
│   ├── TicTacToe.py              # Main code for the Tic Tac Toe game
│   ├── test_TicTacToe.py         # Unit tests for the Tic Tac Toe game
│   └── README.md                 # Documentation for the Tic Tac Toe game
│
├── SpaceInvaders/
│   ├── SpaceInvaders.py          # Main code for the Space Invaders game
│   ├── test_SpaceInvaders.py     # Unit tests for the Space Invaders game
│   └── README.md                 # Documentation for the Space Invaders game
│
├── 2048/
│   ├── 2048.py                   # Main code for the 2048 game
│   ├── test_2048.py              # Unit tests for the 2048 game
│   └── README.md                 # Documentation for the 2048 game
│
├── MemoryGame/
│   ├── Memory.py                 # Main code for the Memory game
│   ├── test_Memory.py            # Unit tests for the Memory game
│   └── README.md                 # Documentation for the Memory game
│
└── README.md                     # Global documentation for the repository
```

## Games Included 🕹️

### 1. Guess The Number 🎲
A number guessing game where the player tries to guess a randomly generated number within a range. The game provides hints after each guess, indicating if the target number is "Higher" or "Lower" than the player's guess. Features include:
- Customizable range for the target number
- Feedback on each guess: "Higher", "Lower", or "Correct!"
- Keeps track of the number of attempts

[See the Guess The Number README](GuessTheNumber/README.md)

### 2. Pong 🏓
A classic two-player game where each player controls a paddle, and the objective is to hit the ball past the opponent’s paddle to score points. Features include:
- Player-controlled paddle with arrow keys
- AI-controlled opponent paddle
- Ball bouncing off walls and paddles
- Score display

[See the Pong README](Pong/README.md)

### 3. Snake 🐍
A single-player game where the player controls a snake that grows each time it eats food. The objective is to avoid colliding with the snake’s own body or the boundaries. Features include:
- Growing snake with each food item eaten
- Increasing difficulty as the snake grows
- Boundary and self-collision detection
- Score display

[See the Snake README](Snake/README.md)

### 4. Tic Tac Toe ❌⭕
A two-player game (played on the same screen) where the objective is to be the first player to align three of your symbols in a row, column, or diagonal. Features include:
- 3x3 grid display
- Turn-based gameplay for two players
- Win and draw detection
- Console-based interface for simplicity

[See the Tic Tac Toe README](TicTacToe/README.md)

### 5. Space Invaders 🚀
A classic arcade game where you control a spaceship and try to defend against waves of invading enemies. Destroy as many enemies as you can, earn points, and survive for as long as possible. Features include:
- Player-controlled spaceship that can shoot bullets
- Waves of enemies that move in formation and drop down as they reach screen edges
- Score tracking and lives system
- Game Over detection

[See the Space Invaders README](SpaceInvaders/README.md)

### 6. 2048 Game 🎲
A puzzle game where the objective is to combine tiles with the same value to reach the elusive **2048** tile. Slide the tiles, combine matching numbers, and try to reach the highest score! Features include:
- 4x4 grid with sliding and combining mechanics
- Random tile generation after each move
- Score tracking and win/lose conditions
- Reset option to start a new game

[See the 2048 README](2048/README.md)

### 7. Memory Game 🧠
A classic memory card game where the objective is to find all matching pairs of cards on a 4x4 grid. Flip the cards, try to remember their positions, and match all pairs to win the game! Features include:
- Flip and match mechanics with 1-second delay for unmatched pairs
- 4x4 grid with 8 unique pairs, randomly shuffled
- Game completion detection with a congratulatory message

[See the Memory Game README](MemoryGame/README.md)

## Requirements 🛠️

Each game requires:
- Python 3.6 or higher
- Pygame library (for all games except **Guess The Number** and **Tic Tac Toe**)

To install Pygame, run:
```bash
pip install pygame
```

## How to Run Each Game ▶️

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Python-Games-Collection.git
    cd Python-Games-Collection
    ```

2. Navigate to the desired game folder:
    ```bash
    cd Pong          # or cd Snake, cd TicTacToe, cd GuessTheNumber, etc.
    ```

3. Run the game:
    ```bash
    python Pong.py           # or python Snake.py, python TicTacToe.py, etc.
    ```

4. To run the tests:
    ```bash
    python -m unittest test_Pong.py    # or test_Snake.py, test_TicTacToe.py, etc.
    ```

## Contributions 🤝

Contributions to improve these games or add features are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a Pull Request.

## License 📄

This project is licensed under the MIT License. See the LICENSE file for more details.

---

Enjoy playing and exploring these classic games with Python! 🎉