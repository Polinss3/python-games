import unittest
from SpaceInvaders import Player, Bullet, Enemy, SpaceInvaders

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player()

    def test_initial_position(self):
        self.assertEqual(self.player.rect.midbottom, (400, 570))

    def test_move_left(self):
        initial_x = self.player.rect.x
        self.player.move("left")
        self.assertLess(self.player.rect.x, initial_x)

    def test_move_right(self):
        initial_x = self.player.rect.x
        self.player.move("right")
        self.assertGreater(self.player.rect.x, initial_x)

    def test_shoot(self):
        self.player.shoot()
        self.assertEqual(len(self.player.bullets), 1)

class TestEnemy(unittest.TestCase):
    def setUp(self):
        self.enemy = Enemy(100, 100)

    def test_initial_position(self):
        self.assertEqual(self.enemy.rect.topleft, (100, 100))

    def test_move_right(self):
        initial_x = self.enemy.rect.x
        self.enemy.move("right")
        self.assertGreater(self.enemy.rect.x, initial_x)

    def test_move_left(self):
        initial_x = self.enemy.rect.x
        self.enemy.move("left")
        self.assertLess(self.enemy.rect.x, initial_x)

SCREEN_HEIGHT = 600  # Define the screen height

class TestSpaceInvaders(unittest.TestCase):
    def setUp(self):
        self.game = SpaceInvaders()

    def test_create_enemies(self):
        self.assertEqual(len(self.game.enemies), 24)

    def test_score_increase_on_collision(self):
        initial_score = self.game.score
        bullet = Bullet(self.game.enemies[0].rect.x, self.game.enemies[0].rect.y)
        self.game.player.bullets.append(bullet)
        self.game.check_collisions()
        self.assertGreater(self.game.score, initial_score)

    def test_game_over(self):
        self.game.lives = 1
        for enemy in self.game.enemies:
            enemy.rect.y = SCREEN_HEIGHT
        self.assertTrue(self.game.check_game_over())

if __name__ == "__main__":
    unittest.main()
