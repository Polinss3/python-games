import unittest
from Pong import Ball, Paddle, PongGame, SCREEN_WIDTH, SCREEN_HEIGHT, BALL_SIZE, PADDLE_HEIGHT


class TestBall(unittest.TestCase):
    def setUp(self):
        self.ball = Ball()

    def test_initial_position(self):
        self.assertEqual(self.ball.rect.center,
                         (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    def test_ball_movement(self):
        initial_x = self.ball.rect.x
        self.ball.move()
        self.assertNotEqual(self.ball.rect.x, initial_x)

    def test_ball_bounce_vertical(self):
        self.ball.rect.y = 0
        dummy_player = Paddle(0, 0)
        dummy_opponent = Paddle(0, 0)
        initial_speed_y = self.ball.speed_y
        self.ball.check_collision(dummy_player, dummy_opponent)
        self.assertEqual(self.ball.speed_y, -initial_speed_y)


class TestPaddle(unittest.TestCase):
    def setUp(self):
        self.paddle = Paddle(0, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)

    def test_paddle_move_up(self):
        self.paddle.speed = -5
        self.paddle.move()
        self.assertLess(self.paddle.rect.y, SCREEN_HEIGHT // 2)

    def test_paddle_move_down(self):
        self.paddle.speed = 5
        initial_y = self.paddle.rect.y
        self.paddle.move()
        self.assertGreater(self.paddle.rect.y, initial_y)

    def test_paddle_stays_in_bounds(self):
        self.paddle.rect.y = SCREEN_HEIGHT - 10
        self.paddle.speed = 10
        self.paddle.move()
        self.assertLessEqual(self.paddle.rect.bottom, SCREEN_HEIGHT)


class TestPongGame(unittest.TestCase):
    def setUp(self):
        self.game = PongGame()

    def test_player_scoring(self):
        self.game.ball.rect.left = 1
        self.game.ball.speed_x = -abs(self.game.ball.speed_x)
        self.game.update()
        self.assertEqual(self.game.player_score, 1)


    def test_opponent_scoring(self):
        # Simulate ball out of bounds on right
        self.game.ball.rect.right = SCREEN_WIDTH
        self.game.update()
        self.assertEqual(self.game.opponent_score, 1)

    def test_opponent_ai_follows_ball(self):
        self.game.ball.rect.centery = self.game.opponent.rect.centery - 10
        initial_opponent_centery = self.game.opponent.rect.centery
        self.game.opponent_ai()
        self.assertLess(self.game.opponent.rect.centery, initial_opponent_centery)

        self.game.ball.rect.centery = self.game.opponent.rect.centery + 10
        initial_opponent_centery = self.game.opponent.rect.centery
        self.game.opponent_ai()
        self.assertGreater(self.game.opponent.rect.centery, initial_opponent_centery)



if __name__ == "__main__":
    unittest.main()
