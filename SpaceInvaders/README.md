# Space Invaders 🚀

Welcome to **Space Invaders**! This is a Python-based version of the classic arcade game where you control a spaceship and try to defend against waves of invading enemies. Destroy as many enemies as you can, earn points, and survive for as long as possible.

## Project Structure 📂

```plaintext
SpaceInvaders/
│
├── SpaceInvaders.py         # Main code for the Space Invaders game
├── test_SpaceInvaders.py    # Unit tests for the game's logic
└── README.md                # Documentation for the Space Invaders game
```

## How to Play 🕹️

1. **Objective**: Shoot the invading enemies before they reach the bottom of the screen. The game ends when you lose all lives or an enemy successfully invades.
2. **Controls**:
   - **LEFT Arrow**: Move spaceship left
   - **RIGHT Arrow**: Move spaceship right
   - **SPACEBAR**: Shoot bullets

3. **Scoring and Lives**:
   - You earn points for each enemy you destroy.
   - You start with 3 lives. If an enemy reaches the bottom, you lose a life.
   - The game ends when you lose all your lives.

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
    git clone https://github.com/yourusername/SpaceInvaders.git
    cd SpaceInvaders
    ```

2. Run the game:
    ```bash
    python SpaceInvaders.py
    ```

3. To run the tests:
    ```bash
    python -m unittest test_SpaceInvaders.py
    ```

## Features 🎮

- **Player Control**: Move the spaceship left and right and shoot bullets to destroy enemies.
- **Enemy Waves**: Enemies move in a formation and drop down as they reach the screen edges.
- **Score Tracking**: Each enemy destroyed increases the score by 10 points.
- **Lives System**: Start with 3 lives. Each time an enemy reaches the bottom of the screen, you lose a life.
- **Game Over**: When lives reach zero, the game ends.

## Code Overview 📝

- **`Player` Class**: Controls the player's spaceship, movement, and shooting mechanics.
- **`Bullet` Class**: Represents the bullets fired by the player, moving upwards and checking for collisions with enemies.
- **`Enemy` Class**: Represents each enemy in the wave, moving left to right and downwards when reaching the screen edges.
- **`SpaceInvaders` Class**: The main game class, handling the game loop, score tracking, collision detection, and game over conditions.

## Tests 🧪

The `test_SpaceInvaders.py` file includes unit tests to verify the main functionalities of the game:

- **TestPlayer**:
  - `test_initial_position`: Verifies the initial position of the player's spaceship.
  - `test_move_left` and `test_move_right`: Ensures that the spaceship moves correctly in both directions.
  - `test_shoot`: Checks that bullets are created correctly when shooting.

- **TestEnemy**:
  - `test_initial_position`: Checks the initial position of an enemy.
  - `test_move_right` and `test_move_left`: Verifies the movement of enemies in both directions.

- **TestSpaceInvaders**:
  - `test_create_enemies`: Ensures that the correct number of enemies are created at the start of the game.
  - `test_score_increase_on_collision`: Simulates a collision and checks that the score is incremented.
  - `test_game_over`: Tests that the game ends when the enemies reach the bottom of the screen and the player loses all lives.

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

Enjoy the game and defend the galaxy! 🌌💥👾