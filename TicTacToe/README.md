Aquí tienes el archivo `README.md` en inglés:

```markdown
# TicTacToe 🎮

This is a Python project that implements the classic Tic-Tac-Toe game. The game allows two players to play in the console, taking turns to place their markers on a 3x3 board. The first player to achieve three markers in a row, either horizontally, vertically, or diagonally, wins the game.

## Project Structure 📁

```plaintext
TikTakToe/
│
├── TicTacToe.py      # Main game code
├── test_TicTacToe.py # Unit tests
└── README.md         # Project documentation
```

## Features 🚀

- **3x3 Board**: Represented as a list of 9 elements, allowing fast access to each position.
- **Turn Switching**: Alternates between two players ('X' and 'O') automatically.
- **Winner Detection**: Checks for a winning combination after each move.
- **Draw Detection**: Identifies if the board is full without a winner, indicating a draw.
- **Move Validation**: Prevents players from making moves in already occupied positions.

## Requirements 🛠️

To run this project, you need Python 3.6 or higher.

## Installation and Execution ▶️

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/TikTakToe.git
    cd TikTakToe
    ```

2. Run the game in the console:
    ```bash
    python TicTacToe.py
    ```

3. To run the tests:
    ```bash
    python -m unittest test_TicTacToe.py
    ```

## Game Usage 🕹️

When the game starts, the empty board is displayed in the console. Players should enter a position (from 0 to 8) where they want to place their marker. The board has the following position numbering:

```plaintext
0 | 1 | 2
---------
3 | 4 | 5
---------
6 | 7 | 8
```

### Example of Gameplay

- **Player X** chooses position `0`.
- **Player O** chooses position `4`.
- The game continues until a player wins or a draw is detected.

## Tests 🧪

The `test_TicTacToe.py` file contains unit tests to verify the correct functioning of the main game functionalities:

- **test_initial_board**: Checks that the board is empty at the start.
- **test_make_move_valid**: Tests that players can make valid moves.
- **test_make_move_invalid**: Verifies that moves cannot be made in already occupied positions.
- **test_switch_player**: Confirms that the player turn changes after each move.
- **test_check_winner_row/column/diagonal**: Simulates and verifies wins across rows, columns, and diagonals.
- **test_is_draw**: Tests the detection of a draw when the board is full without a winner.
- **test_no_winner_no_draw**: Ensures no winner or draw at the start of the game.

## Contributions 🤝

Contributions are welcome! If you would like to improve the code or add features, please follow these steps:

1. Fork the project.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a Pull Request.

## License 📜

This project is licensed under the MIT License. See the LICENSE file for more details.

---

Enjoy playing Tic-Tac-Toe in Python! 😄
```

This `README.md` provides a comprehensive guide in English, covering project structure, features, installation, usage, tests, and contribution guidelines. Let me know if you need any further modifications!