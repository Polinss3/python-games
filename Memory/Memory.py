import pygame
import random
import sys
import time

# Configuración inicial
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
GRID_SIZE = 4  # Tablero de 4x4
TILE_SIZE = 100
FONT_SIZE = 48
BACKGROUND_COLOR = (30, 30, 30)
TILE_COLOR = (255, 255, 255)
FLIPPED_COLOR = (200, 200, 200)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Memory Game")
font = pygame.font.Font(None, FONT_SIZE)

# Clase del juego de memoria
class MemoryGame:
    def __init__(self):
        self.grid = []
        self.flipped_tiles = []
        self.matched_tiles = []
        self.waiting_for_flip_back = False
        self.last_flip_time = None
        self.create_grid()
        self.shuffle_tiles()

    def create_grid(self):
        # Crear pares de números del 1 al 8 (2 veces cada uno para un total de 16 tiles en un tablero de 4x4)
        numbers = list(range(1, 9)) * 2
        self.grid = [numbers[i * GRID_SIZE:(i + 1) * GRID_SIZE] for i in range(GRID_SIZE)]

    def shuffle_tiles(self):
        # Aplana la lista, mezcla y vuelve a dividir en una matriz de 4x4
        flat_list = [num for row in self.grid for num in row]
        random.shuffle(flat_list)
        self.grid = [flat_list[i * GRID_SIZE:(i + 1) * GRID_SIZE] for i in range(GRID_SIZE)]

    def select_tile(self, row, col):
        # Solo permite seleccionar si no estamos esperando el tiempo de visualización de la segunda carta
        if not self.waiting_for_flip_back and (row, col) not in self.flipped_tiles and (row, col) not in self.matched_tiles:
            self.flipped_tiles.append((row, col))
            if len(self.flipped_tiles) == 2:
                self.check_match()

    def check_match(self):
        # Verifica si las dos fichas volteadas coinciden
        r1, c1 = self.flipped_tiles[0]
        r2, c2 = self.flipped_tiles[1]
        if self.grid[r1][c1] == self.grid[r2][c2]:
            self.matched_tiles.extend([self.flipped_tiles[0], self.flipped_tiles[1]])
            self.flipped_tiles = []
        else:
            # Si no coinciden, inicia un temporizador de espera
            self.waiting_for_flip_back = True
            self.last_flip_time = pygame.time.get_ticks()

    def update(self):
        # Si estamos esperando para voltear las fichas de nuevo, verifica el tiempo
        if self.waiting_for_flip_back:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_flip_time > 2000:  # 2000 ms = 2 segundos
                self.flipped_tiles = []  # Voltea las fichas de nuevo
                self.waiting_for_flip_back = False

    def is_game_over(self):
        return len(self.matched_tiles) == GRID_SIZE * GRID_SIZE

    def draw(self):
        screen.fill(BACKGROUND_COLOR)
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                x = col * TILE_SIZE
                y = row * TILE_SIZE
                rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
                
                if (row, col) in self.flipped_tiles or (row, col) in self.matched_tiles:
                    # Dibuja la ficha descubierta
                    pygame.draw.rect(screen, FLIPPED_COLOR, rect)
                    text = font.render(str(self.grid[row][col]), True, (0, 0, 0))
                    screen.blit(text, text.get_rect(center=rect.center))
                else:
                    # Dibuja la ficha oculta
                    pygame.draw.rect(screen, TILE_COLOR, rect)

                # Borde de las fichas
                pygame.draw.rect(screen, BACKGROUND_COLOR, rect, 3)

    def reset(self):
        self.flipped_tiles = []
        self.matched_tiles = []
        self.shuffle_tiles()
        self.waiting_for_flip_back = False

def main():
    game = MemoryGame()
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row, col = y // TILE_SIZE, x // TILE_SIZE
                if row < GRID_SIZE and col < GRID_SIZE:
                    game.select_tile(row, col)

        # Actualiza el estado del juego y maneja la lógica de tiempo para el volteo
        game.update()
        game.draw()
        
        if game.is_game_over():
            print("Congratulations! You've matched all pairs.")
            pygame.time.wait(1000)
            game.reset()

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
