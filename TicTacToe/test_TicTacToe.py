# test_TicTacToe.py
import unittest
from TicTacToe import TicTacToe

class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        # Configuración inicial para cada test
        self.game = TicTacToe()

    def test_initial_board(self):
        # Verifica que el tablero esté vacío al inicio
        self.assertEqual(self.game.board, [' ' for _ in range(9)])

    def test_make_move_valid(self):
        # Verifica que se pueda hacer un movimiento válido
        result = self.game.make_move(0)
        self.assertTrue(result)
        self.assertEqual(self.game.board[0], self.game.current_player)

    def test_make_move_invalid(self):
        # Verifica que no se pueda hacer un movimiento en una posición ocupada
        self.game.make_move(0)
        result = self.game.make_move(0)
        self.assertFalse(result)

    def test_switch_player(self):
        # Verifica que el cambio de turno funcione correctamente
        initial_player = self.game.current_player
        self.game.switch_player()
        self.assertNotEqual(self.game.current_player, initial_player)

    def test_check_winner_row(self):
        # Simula una victoria en la primera fila
        self.game.board = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
        winner = self.game.check_winner()
        self.assertEqual(winner, 'X')

    def test_check_winner_column(self):
        # Simula una victoria en la primera columna
        self.game.board = ['O', ' ', ' ', 'O', ' ', ' ', 'O', ' ', ' ']
        winner = self.game.check_winner()
        self.assertEqual(winner, 'O')

    def test_check_winner_diagonal(self):
        # Simula una victoria en una de las diagonales
        self.game.board = ['X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X']
        winner = self.game.check_winner()
        self.assertEqual(winner, 'X')

    def test_is_draw(self):
        # Simula un empate con todas las posiciones llenas
        self.game.board = ['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'X']
        draw = self.game.is_draw()
        self.assertTrue(draw)

    def test_no_winner_no_draw(self):
        # Verifica que no haya ganador o empate al inicio
        winner = self.game.check_winner()
        draw = self.game.is_draw()
        self.assertIsNone(winner)
        self.assertFalse(draw)

if __name__ == "__main__":
    unittest.main()
