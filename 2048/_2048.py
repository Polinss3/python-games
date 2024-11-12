import pygame
import random
import sys

# Configuración inicial
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
GRID_SIZE = 4
TILE_SIZE = 80
TILE_MARGIN = 10
FONT_SIZE = 32
BACKGROUND_COLOR = (187, 173, 160)
TILE_COLORS = {
    0: (204, 192, 179),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
}

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2048")
font = pygame.font.Font(None, FONT_SIZE)

# Clase del juego
class Game2048:
    def __init__(self):
        self.grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
        self.score = 0
        self.add_new_tile()
        self.add_new_tile()

    def add_new_tile(self):
        empty_cells = [(r, c) for r in range(GRID_SIZE) for c in range(GRID_SIZE) if self.grid[r][c] == 0]
        if empty_cells:
            r, c = random.choice(empty_cells)
            self.grid[r][c] = 4 if random.random() > 0.9 else 2

    def move_left(self):
        moved = False
        for row in self.grid:
            compressed, score_increase = self.compress(row)
            if row != compressed:
                moved = True
            row[:] = compressed
            self.score += score_increase
        return moved

    def move_right(self):
        moved = False
        for row in self.grid:
            reversed_row = row[::-1]
            compressed, score_increase = self.compress(reversed_row)
            if row != compressed[::-1]:
                moved = True
            row[:] = compressed[::-1]
            self.score += score_increase
        return moved

    def move_up(self):
        moved = False
        for col in range(GRID_SIZE):
            column = [self.grid[row][col] for row in range(GRID_SIZE)]
            compressed, score_increase = self.compress(column)
            if [self.grid[row][col] for row in range(GRID_SIZE)] != compressed:
                moved = True
            for row in range(GRID_SIZE):
                self.grid[row][col] = compressed[row]
            self.score += score_increase
        return moved

    def move_down(self):
        moved = False
        for col in range(GRID_SIZE):
            column = [self.grid[row][col] for row in range(GRID_SIZE)][::-1]
            compressed, score_increase = self.compress(column)
            if [self.grid[row][col] for row in range(GRID_SIZE)] != compressed[::-1]:
                moved = True
            for row in range(GRID_SIZE):
                self.grid[row][col] = compressed[::-1][row]
            self.score += score_increase
        return moved

    def compress(self, row):
        new_row = [value for value in row if value != 0]
        score_increase = 0
        for i in range(len(new_row) - 1):
            if new_row[i] == new_row[i + 1]:
                new_row[i] *= 2
                score_increase += new_row[i]
                new_row[i + 1] = 0
        new_row = [value for value in new_row if value != 0]
        return new_row + [0] * (GRID_SIZE - len(new_row)), score_increase

    def check_game_over(self):
        if any(2048 in row for row in self.grid):
            return "WIN"
        if any(0 in row for row in self.grid):
            return None
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE - 1):
                if self.grid[r][c] == self.grid[r][c + 1] or self.grid[c][r] == self.grid[c + 1][r]:
                    return None
        return "LOSE"

    def draw(self):
        screen.fill(BACKGROUND_COLOR)
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                value = self.grid[r][c]
                color = TILE_COLORS.get(value, (60, 58, 50))
                rect = pygame.Rect(c * (TILE_SIZE + TILE_MARGIN) + TILE_MARGIN, r * (TILE_SIZE + TILE_MARGIN) + TILE_MARGIN, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(screen, color, rect)
                if value != 0:
                    text = font.render(str(value), True, (0, 0, 0) if value <= 4 else (255, 255, 255))
                    text_rect = text.get_rect(center=rect.center)
                    screen.blit(text, text_rect)

    def reset(self):
        self.grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
        self.score = 0
        self.add_new_tile()
        self.add_new_tile()

def main():
    game = Game2048()
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                moved = False
                if event.key == pygame.K_LEFT:
                    moved = game.move_left()
                elif event.key == pygame.K_RIGHT:
                    moved = game.move_right()
                elif event.key == pygame.K_UP:
                    moved = game.move_up()
                elif event.key == pygame.K_DOWN:
                    moved = game.move_down()

                if moved:
                    game.add_new_tile()
                    game_state = game.check_game_over()
                    if game_state == "WIN":
                        print("Congratulations! You've won the game.")
                        pygame.time.wait(2000)
                        game.reset()
                    elif game_state == "LOSE":
                        print("Game Over! You've lost the game.")
                        pygame.time.wait(2000)
                        game.reset()

        game.draw()
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
