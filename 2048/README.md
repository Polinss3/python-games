# 2048 Game 🎲

Welcome to **2048**! This is a Python-based version of the popular puzzle game where the objective is to combine tiles with the same value to reach the elusive **2048** tile. Slide the tiles, combine matching numbers, and try to reach the highest score!

## Project Structure 📂

```plaintext
2048/
│
├── 2048.py              # Main code for the 2048 game
├── test_2048.py         # Unit tests for the game's logic
└── README.md            # Documentation for the 2048 game
```

## How to Play 🕹️

1. **Objective**: Combine tiles with the same value to create tiles with higher values, ultimately reaching the 2048 tile. The game ends when you either reach 2048 (win) or run out of possible moves (lose).
2. **Controls**:
   - **LEFT Arrow**: Slide tiles left
   - **RIGHT Arrow**: Slide tiles right
   - **UP Arrow**: Slide tiles up
   - **DOWN Arrow**: Slide tiles down

3. **Game Mechanics**:
   - Each move slides all tiles in the chosen direction.
   - Tiles with the same value combine to form a new tile with double the value (e.g., two tiles with 2 combine to form a 4).
   - After each move, a new tile (2 or 4) is added to an empty cell.

## Requirements 🛠️

- Python 3.6 or higher
- Pygame library

To install Pygame, run:
```bash
pip install pygame
```

## How to Run ▶️

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/2048.git
    cd 2048
    ```

2. Run the game:
    ```bash
    python 2048.py
    ```

3. To run the tests:
    ```bash
    python -m unittest test_2048.py
    ```

## Features 🎮

- **Slide and Combine**: Slide tiles in any direction, and combine tiles with the same value.
- **Random Tile Generation**: After each move, a new tile appears in a random empty cell.
- **Score Tracking**: Your score increases with each combination.
- **Win/Lose Conditions**: The game ends when you reach a 2048 tile (win) or have no possible moves left (lose).
- **Reset Option**: Restart the game when you win or lose.

## Code Overview 📝

- **`Game2048` Class**: Contains the main game logic for moving tiles, combining tiles, and generating new tiles.
  - **`add_new_tile`**: Adds a new tile (2 or 4) in a random empty cell.
  - **`move_left`, `move_right`, `move_up`, `move_down`**: Functions to slide tiles in each direction.
  - **`compress`**: Helper function to handle tile merging and compressing rows.
  - **`check_game_over`**: Checks if the game is won (2048 tile) or lost (no moves left).
  - **`draw`**: Draws the game board and updates tile values on the screen.
  - **`reset`**: Resets the board to start a new game.

## Tests 🧪

The `test_2048.py` file includes unit tests to verify the main functionalities of the game:

- **test_initial_tiles**: Checks that the game starts with exactly two tiles on the grid.
- **test_move_left**: Tests that tiles slide and combine correctly when moving left.
- **test_move_right**: Tests that tiles slide and combine correctly when moving right.
- **test_game_win**: Simulates a winning condition (2048 tile) and verifies the game state.
- **test_game_over**: Tests that the game detects a loss when there are no more possible moves.

## Contributions 🤝

Contributions to improve the game or add features are welcome! Please follow these steps:

1. Fork the project.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a Pull Request.

## License 📄

This project is licensed under the MIT License. See the LICENSE file for more details.

---

Enjoy the game and good luck reaching 2048! 🎉