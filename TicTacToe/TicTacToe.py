class TicTacToe:
    def __init__(self):
        # Inicializa el tablero y establece el jugador inicial
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def display_board(self):
        # Método para mostrar el tablero de forma legible
        for row in [self.board[i:i+3] for i in range(0, 9, 3)]:
            print('|'.join(row))
            print('-' * 5)
    
    def make_move(self, position):
        # Coloca el símbolo del jugador actual en la posición si es válida
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            return True
        return False

    def check_winner(self):
        # Comprobación de combinaciones ganadoras
        win_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Filas
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columnas
            (0, 4, 8), (2, 4, 6)              # Diagonales
        ]
        for (a, b, c) in win_combinations:
            if self.board[a] == self.board[b] == self.board[c] != ' ':
                return self.board[a]
        return None

    def is_draw(self):
        # Verifica si hay empate (si el tablero está lleno y no hay ganador)
        return ' ' not in self.board

    def switch_player(self):
        # Cambia el turno del jugador
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play(self):
        # Método principal para ejecutar el juego en la consola
        print("Bienvenido al Tres en Raya")
        self.display_board()
        while True:
            # Captura de la posición del jugador
            try:
                position = int(input(f"Jugador {self.current_player}, elige una posición (0-8): "))
                if position not in range(9):
                    print("Posición inválida. Intente de nuevo.")
                    continue
            except ValueError:
                print("Entrada no válida. Intente de nuevo.")
                continue

            if self.make_move(position):
                self.display_board()
                winner = self.check_winner()
                if winner:
                    print(f"¡El jugador {winner} gana!")
                    break
                elif self.is_draw():
                    print("¡Es un empate!")
                    break
                else:
                    self.switch_player()
            else:
                print("Movimiento inválido. Intente de nuevo.")


if __name__ == "__main__":
    game = TicTacToe()
    game.play()
