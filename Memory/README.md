# Memory Game 🧠

Welcome to **Memory Game**! This is a Python-based version of the classic memory card game, where the objective is to find all matching pairs of cards. Flip the cards, try to remember their positions, and match all pairs to win the game!

## Project Structure 📂

```plaintext
MemoryGame/
│
├── Memory.py            # Main code for the Memory game
├── test_Memory.py       # Unit tests for the game's logic
└── README.md            # Documentation for the Memory game
```

## How to Play 🕹️

1. **Objective**: The goal is to find all pairs of matching cards on a 4x4 grid by remembering their positions. The game is won when all pairs are matched.
2. **Controls**:
   - Click on a card to flip it over and reveal the number.
   - Click on a second card to try to find a matching pair.

3. **Game Mechanics**:
   - If the two selected cards match, they stay flipped.
   - If they don’t match, both cards will remain visible for 1 second and then flip back face down.
   - The game ends when all pairs are matched.

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
    git clone https://github.com/yourusername/MemoryGame.git
    cd MemoryGame
    ```

2. Run the game:
    ```bash
    python Memory.py
    ```

3. To run the tests:
    ```bash
    python -m unittest test_Memory.py
    ```

## Features 🎮

- **4x4 Grid**: A board with 16 tiles containing 8 unique pairs of numbers, randomly shuffled.
- **Flip and Match**: Click on tiles to reveal their values. If two flipped tiles match, they remain visible.
- **1-Second Delay for Non-Matching Tiles**: If two flipped tiles do not match, they remain visible for 1 second before flipping back down, allowing you to remember their positions.
- **Game Completion Detection**: The game detects when all pairs have been matched and displays a congratulatory message.

## Code Overview 📝

- **`MemoryGame` Class**: Contains the main game logic for creating, shuffling, and managing the tiles.
  - **`create_grid`**: Initializes the grid with pairs of numbers.
  - **`shuffle_tiles`**: Randomly shuffles the numbers across the grid.
  - **`select_tile`**: Manages tile selection, flipping logic, and checks for matching pairs.
  - **`check_match`**: Checks if two selected tiles match. If they don’t, starts a 1-second timer to flip them back.
  - **`update`**: Manages the timer for flipping non-matching tiles back down after 1 second.
  - **`is_game_over`**: Checks if the game has been won (all pairs have been matched).
  - **`draw`**: Draws the grid on the screen, displaying flipped tiles and hiding unmatched tiles.

## Tests 🧪

The `test_Memory.py` file includes unit tests to verify the main functionalities of the game:

- **test_initial_grid**: Ensures the grid is initialized with exactly 8 unique pairs.
- **test_select_tile**: Verifies that selecting a tile flips it over.
- **test_check_match**: Simulates a matching scenario and verifies that the tiles stay visible when matched.
- **test_no_match**: Simulates a non-matching scenario and checks that the tiles do not remain flipped.
- **test_is_game_over**: Verifies that the game detects when all pairs have been matched.

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

Have fun and test your memory skills! 🎉