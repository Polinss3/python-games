import unittest
from _2048 import Game2048

class TestGame2048(unittest.TestCase):
    def setUp(self):
        self.game = Game2048()

    def test_initial_tiles(self):
        non_zero_tiles = sum(cell != 0 for row in self.game.grid for cell in row)
        self.assertEqual(non_zero_tiles, 2)

    def test_move_left(self):
        self.game.grid = [
            [2, 2, 4, 4],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        moved = self.game.move_left()
        self.assertTrue(moved)
        self.assertEqual(self.game.grid[0], [4, 8, 0, 0])

    def test_move_right(self):
        self.game.grid = [
            [2, 2, 4, 4],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        moved = self.game.move_right()
        self.assertTrue(moved)
        self.assertEqual(self.game.grid[0], [0, 0, 4, 8])

    def test_game_win(self):
        self.game.grid = [
            [2048, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.assertEqual(self.game.check_game_over(), "WIN")

    def test_game_over(self):
        self.game.grid = [
            [2, 4, 2, 4],
            [4, 2, 4, 2],
            [2, 4, 2, 4],
            [4, 2, 4, 2],
        ]
        self.assertEqual(self.game.check_game_over(), "LOSE")

if __name__ == "__main__":
    unittest.main()
