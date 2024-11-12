import unittest
from GuessTheNumber import GuessTheNumber

class TestGuessTheNumber(unittest.TestCase):

    def setUp(self):
        # Configura un juego con un rango específico para controlar mejor el test
        self.game = GuessTheNumber(1, 10)
        self.game.target_number = 5  # Forza el número objetivo para pruebas consistentes

    def test_guess_higher(self):
        # Prueba cuando el número es menor que el objetivo
        self.assertEqual(self.game.guess(3), "Higher")

    def test_guess_lower(self):
        # Prueba cuando el número es mayor que el objetivo
        self.assertEqual(self.game.guess(7), "Lower")

    def test_guess_correct(self):
        # Prueba cuando el jugador acierta el número
        self.assertEqual(self.game.guess(5), "Correct!")
        self.assertEqual(self.game.attempts, 1)  # Verifica que solo tomó un intento

    def test_attempts_count(self):
        # Prueba que el contador de intentos aumente con cada intento
        self.game.guess(1)
        self.game.guess(2)
        self.game.guess(3)
        self.assertEqual(self.game.attempts, 3)

    def test_reset_game(self):
        # Prueba que el juego se reinicie correctamente
        self.game.guess(5)  # Adivina el número correcto
        self.game.reset_game()
        self.assertEqual(self.game.attempts, 0)  # El contador de intentos debe resetearse
        self.assertNotEqual(self.game.target_number, 5)  # El nuevo objetivo debe ser diferente

if __name__ == "__main__":
    unittest.main()
