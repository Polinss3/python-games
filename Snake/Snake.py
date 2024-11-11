import pygame
import random
import sys

# Configuración inicial
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BLOCK_SIZE = 20  # Tamaño de cada bloque de la serpiente
FPS = 10         # Velocidad inicial

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]
        self.direction = (BLOCK_SIZE, 0)  # Comienza moviéndose a la derecha
        self.growing = False

    def move(self):
        head_x, head_y = self.body[0]
        delta_x, delta_y = self.direction
        new_head = (head_x + delta_x, head_y + delta_y)
        
        # Añadir nueva cabeza
        self.body = [new_head] + self.body
        # Si no está creciendo, elimina la última parte
        if not self.growing:
            self.body.pop()
        else:
            self.growing = False

    def grow(self):
        # Al hacer crecer la serpiente, mantendrá la última parte
        self.growing = True

    def set_direction(self, direction):
        # Evita que la serpiente se mueva en dirección opuesta a su movimiento actual
        opposite_direction = (-self.direction[0], -self.direction[1])
        if direction != opposite_direction:
            self.direction = direction

    def check_collision(self):
        # Colisión con bordes
        head_x, head_y = self.body[0]
        if head_x < 0 or head_x >= SCREEN_WIDTH or head_y < 0 or head_y >= SCREEN_HEIGHT:
            return True
        # Colisión con sí misma
        if self.body[0] in self.body[1:]:
            return True
        return False

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.spawn()

    def spawn(self):
        # Genera una nueva posición para la comida
        x = random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.position = (x, y)

    def draw(self, screen):
        pygame.draw.rect(screen, RED, pygame.Rect(self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE))

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.running = True

    def handle_events(self):
        # Maneja los eventos de teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.set_direction((0, -BLOCK_SIZE))
                elif event.key == pygame.K_DOWN:
                    self.snake.set_direction((0, BLOCK_SIZE))
                elif event.key == pygame.K_LEFT:
                    self.snake.set_direction((-BLOCK_SIZE, 0))
                elif event.key == pygame.K_RIGHT:
                    self.snake.set_direction((BLOCK_SIZE, 0))

    def update(self):
        # Actualiza el estado del juego
        self.snake.move()
        # Verifica si la serpiente ha comido la comida
        if self.snake.body[0] == self.food.position:
            self.snake.grow()
            self.food.spawn()
            self.score += 1
            # Incrementa la velocidad cada 5 puntos para hacerlo más desafiante
            if self.score % 5 == 0:
                global FPS
                FPS += 2
        # Verifica colisiones
        if self.snake.check_collision():
            self.running = False  # Ahora, esto termina el juego al detectar una colisión

    def draw_elements(self):
        # Dibuja los elementos en pantalla
        self.screen.fill(BLACK)
        for segment in self.snake.body:
            pygame.draw.rect(self.screen, GREEN, pygame.Rect(segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))
        self.food.draw(self.screen)
        self.draw_score()

    def draw_score(self):
        # Dibuja el puntaje en la pantalla
        font = pygame.font.Font(None, 36)
        text = font.render(f'Score: {self.score}', True, WHITE)
        self.screen.blit(text, (10, 10))

    def run(self):
        # Ejecuta el bucle principal del juego
        while self.running:
            self.handle_events()
            self.update()
            self.draw_elements()
            pygame.display.flip()
            self.clock.tick(FPS)
        
        # Al terminar el juego
        self.game_over()

    def game_over(self):
        # Pantalla de Game Over
        self.screen.fill(BLACK)
        font = pygame.font.Font(None, 48)
        text = font.render('Game Over', True, WHITE)
        self.screen.blit(text, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 - 24))
        score_text = font.render(f'Score: {self.score}', True, WHITE)
        self.screen.blit(score_text, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 + 24))
        pygame.display.flip()
        pygame.time.wait(2000)  # Espera 2 segundos antes de cerrar
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
