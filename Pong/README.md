# Pong Game 🏓

This is a Python implementation of the classic **Pong game** using the **Pygame** library. The game features two paddles (one for the player and one controlled by a simple AI) and a bouncing ball. The objective is to score points by making the ball go past the opponent’s paddle.

## Project Structure 📂

```plaintext
Pong/
│
├── Pong.py         # Main game code
├── test_Pong.py    # Unit tests for game logic
└── README.md       # Project documentation
```

## Features 🎮

- **Player Paddle Control**: Use arrow keys to move the player paddle up and down.
- **AI-Controlled Opponent**: The opponent paddle moves automatically based on the ball's position.
- **Score Display**: Each time the ball exits the screen on one side, the opposite player scores a point.
- **Ball Physics**: The ball bounces off paddles, walls, and changes direction based on collision angle.
- **Game Over Detection**: When the player or opponent reaches a certain score, the game can be set to end.

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
    git clone https://github.com/yourusername/PongGame.git
    cd PongGame
    ```

2. Run the game:
    ```bash
    python Pong.py
    ```

3. To run the tests:
    ```bash
    python -m unittest test_Pong.py
    ```

## Game Controls 🕹️

- **UP Arrow**: Move player paddle up
- **DOWN Arrow**: Move player paddle down

The opponent paddle is controlled by a simple AI that moves to follow the ball.

### Objective 🎯
Score points by making the ball pass the opponent's paddle. The first player to reach the designated score wins.

## Tests 🧪

The `test_Pong.py` file includes unit tests that verify the core functionalities of the game:

- **Ball Tests**:
  - `test_initial_position`: Confirms the ball starts in the center.
  - `test_ball_movement`: Checks that the ball moves when the game updates.
  - `test_ball_bounce_vertical`: Tests that the ball bounces when hitting the top or bottom edges.

- **Paddle Tests**:
  - `test_paddle_move_up` and `test_paddle_move_down`: Verify paddle movement.
  - `test_paddle_stays_in_bounds`: Ensures the paddle does not move outside the screen.

- **Game Tests**:
  - `test_player_scoring` and `test_opponent_scoring`: Simulate scoring for player and opponent.
  - `test_opponent_ai_follows_ball`: Ensures the opponent paddle follows the ball’s position.

## Code Structure

- **Ball class**: Manages the ball’s position, movement, and collision with paddles and walls.
- **Paddle class**: Represents the paddles for the player and the opponent, with functions for movement and boundary enforcement.
- **PongGame class**: Manages the main game loop, event handling, collision checks, scoring, and rendering elements on the screen.

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

Enjoy the game and happy coding! 🏓💻