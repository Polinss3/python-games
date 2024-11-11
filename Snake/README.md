# Snake Game 🐍

This is a Python implementation of the classic *Snake* game using the **Pygame** library. The objective of the game is to control a snake that grows longer each time it eats food. The game ends when the snake collides with itself or with the boundaries of the game area.

## Project Structure 📂

```plaintext
Snake/
│
├── Snake.py         # Main game code
├── test_Snake.py    # Unit tests for the game logic
└── README.md        # Project documentation
```

## Features 🎮

- **Dynamic Difficulty**: The game speeds up as your score increases, making it progressively more challenging.
- **Self-collision and Boundary Collision Detection**: The game ends if the snake collides with itself or with the game area boundaries.
- **Score Display**: The current score is displayed in real time.
- **Game Over Screen**: After a collision, a "Game Over" message is shown along with the final score.

## Requirements 🛠️

To run this project, you need:
- Python 3.6 or higher
- Pygame library

You can install Pygame via pip:
```bash
pip install pygame
```

## How to Run ▶️

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/SnakeGame.git
    cd SnakeGame
    ```

2. Run the game:
    ```bash
    python Snake.py
    ```

3. To run the tests:
    ```bash
    python -m unittest test_Snake.py
    ```

## How to Play 🕹️

Use the arrow keys on your keyboard to control the snake's direction:
- **UP**: Move up
- **DOWN**: Move down
- **LEFT**: Move left
- **RIGHT**: Move right

### Objective 🎯
The objective is to navigate the snake to eat the red food blocks. Each time the snake eats food:
- The score increases by 1.
- The snake grows in length.
- The game's speed slightly increases every 5 points, making it more challenging.

Avoid hitting the boundaries of the screen or the snake's own body. The game ends if either of these collisions occurs.

## Tests 🧪

The `test_Snake.py` file includes unit tests that verify the core functionalities of the game:

- **test_initial_snake_length**: Confirms that the snake starts with the correct length.
- **test_move_snake**: Verifies that the snake moves correctly when the game updates.
- **test_grow_snake**: Checks that the snake grows after eating food.
- **test_collision_with_self**: Tests self-collision detection.
- **test_collision_with_wall**: Tests boundary collision detection.
- **test_food_spawn_in_bounds**: Ensures that food spawns within game boundaries.
- **test_score_increase**: Verifies that the score increases after eating food.
- **test_game_over_on_collision**: Confirms that the game stops after a collision.

## Code Structure

- **Snake class**: Manages the snake's movement, growth, direction, and collision detection.
- **Food class**: Randomly generates food positions within the game boundaries.
- **Game class**: Manages the game loop, handling events, updating game state, drawing elements on screen, and displaying the score.

## Contributions 🤝

Contributions are welcome! If you'd like to improve the code or add features, please follow these steps:

1. Fork the project.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a Pull Request.

## License 📄

This project is licensed under the MIT License. See the LICENSE file for more details.

---

Enjoy the game and happy coding! 🐍💻
