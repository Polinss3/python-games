import unittest
from Memory import MemoryGame

class TestMemoryGame(unittest.TestCase):
    def setUp(self):
        self.game = MemoryGame()

    def test_initial_grid(self):
        # Comprueba que haya exactamente 8 pares en la cuadrícula (16 celdas en total)
        flat_grid = [tile for row in self.game.grid for tile in row]
        unique_tiles = set(flat_grid)
        self.assertEqual(len(unique_tiles), 8)
        self.assertEqual(len(flat_grid), 16)

    def test_select_tile(self):
        # Comprueba que al seleccionar una ficha se añade a la lista de flipped_tiles
        self.game.select_tile(0, 0)
        self.assertIn((0, 0), self.game.flipped_tiles)

    def test_check_match(self):
        # Fuerza una coincidencia en el tablero y comprueba el emparejamiento
        self.game.grid[0][0] = 1
        self.game.grid[0][1] = 1
        self.game.select_tile(0, 0)
        self.game.select_tile(0, 1)
        self.assertIn((0, 0), self.game.matched_tiles)
        self.assertIn((0, 1), self.game.matched_tiles)

    def test_no_match(self):
        # Fuerza una no coincidencia y verifica que las fichas no se emparejan
        self.game.grid[0][0] = 1
        self.game.grid[0][1] = 2
        self.game.select_tile(0, 0)
        self.game.select_tile(0, 1)
        self.assertNotIn((0, 0), self.game.matched_tiles)
        self.assertNotIn((0, 1), self.game.matched_tiles)

    def test_is_game_over(self):
        # Verifica la condición de fin de juego cuando todas las fichas están emparejadas
        self.game.matched_tiles = [(r, c) for r in range(4) for c in range(4)]
        self.assertTrue(self.game.is_game_over())

if __name__ == "__main__":
    unittest.main()
