import unittest
from Snake import Snake, Food, Game, SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE

class TestSnake(unittest.TestCase):

    def setUp(self):
        self.snake = Snake()

    def test_initial_snake_length(self):
        self.assertEqual(len(self.snake.body), 3)

    def test_move_snake(self):
        initial_head = self.snake.body[0]
        self.snake.move()
        self.assertNotEqual(self.snake.body[0], initial_head)

    def test_grow_snake(self):
        initial_length = len(self.snake.body)
        self.snake.grow()
        self.snake.move()
        self.assertEqual(len(self.snake.body), initial_length + 1)

    def test_collision_with_self(self):
        self.snake.body = [(100, 100), (80, 100), (100, 100)]
        self.assertTrue(self.snake.check_collision())

    def test_collision_with_wall(self):
        self.snake.body = [(0, 100), (20, 100), (40, 100)]
        self.snake.set_direction((-BLOCK_SIZE, 0))
        self.snake.move()
        self.assertTrue(self.snake.check_collision())

class TestFood(unittest.TestCase):

    def setUp(self):
        self.food = Food()

    def test_food_spawn_in_bounds(self):
        x, y = self.food.position
        self.assertGreaterEqual(x, 0)
        self.assertLess(x, SCREEN_WIDTH)
        self.assertGreaterEqual(y, 0)
        self.assertLess(y, SCREEN_HEIGHT)

    def test_food_respawn(self):
        initial_position = self.food.position
        self.food.spawn()
        self.assertNotEqual(self.food.position, initial_position)

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_initial_score(self):
        self.assertEqual(self.game.score, 0)

    def test_score_increase(self):
        # Configura la serpiente para que coma la comida después de moverse
        self.game.snake.body = [(100, 100)]
        self.game.snake.direction = (BLOCK_SIZE, 0)  # Mover a la derecha
        self.game.food.position = (100 + BLOCK_SIZE, 100)  # Coloca la comida frente a la serpiente
        initial_score = self.game.score
        self.game.update()
        self.assertEqual(self.game.score, initial_score + 1)

    def test_game_over_on_collision(self):
        # Configura la serpiente para colisionar consigo misma después de moverse
        self.game.snake.body = [(100, 100), (80, 100), (80, 120), (100, 120)]
        self.game.snake.direction = (0, BLOCK_SIZE)  # Mover hacia abajo
        self.game.update()
        self.assertFalse(self.game.running)

    def test_direction_change(self):
        initial_direction = self.game.snake.direction
        self.game.snake.set_direction((0, -BLOCK_SIZE))
        self.assertNotEqual(self.game.snake.direction, initial_direction)
        # Intenta revertir a la dirección opuesta
        self.game.snake.set_direction((0, BLOCK_SIZE))
        self.assertEqual(self.game.snake.direction, (0, -BLOCK_SIZE))

if __name__ == "__main__":
    unittest.main()
