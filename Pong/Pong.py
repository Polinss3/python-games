import pygame
import sys

# Configuración inicial
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
BALL_SIZE = 20
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 80
PADDLE_SPEED = 7
BALL_SPEED_X = 4
BALL_SPEED_Y = 4

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Clase de la pelota
class Ball:
    def __init__(self):
        self.rect = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
        self.speed_x = BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def check_collision(self, player, opponent):
        # Rebote en la pantalla superior o inferior
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.speed_y *= -1
        
        # Rebote en las paletas
        if self.rect.colliderect(player.rect) or self.rect.colliderect(opponent.rect):
            self.speed_x *= -1

    def reset(self):
        # Restablece la posición y velocidad de la pelota
        self.rect.x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
        self.rect.y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2
        self.speed_x *= -1
        self.speed_y *= -1

# Clase de la paleta (jugador)
class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = 0

    def move(self):
        self.rect.y += self.speed
        # Evita que la paleta salga de los límites de la pantalla
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def reset(self, y):
        self.rect.y = y
        self.speed = 0

# Clase principal del juego
class PongGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Pong Game')
        self.clock = pygame.time.Clock()
        self.player = Paddle(SCREEN_WIDTH - 20, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
        self.opponent = Paddle(10, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
        self.ball = Ball()
        self.player_score = 0
        self.opponent_score = 0
        self.running = True

    def handle_events(self):
        # Maneja los eventos de teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player.speed = -PADDLE_SPEED
                elif event.key == pygame.K_DOWN:
                    self.player.speed = PADDLE_SPEED
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    self.player.speed = 0

    def update(self):
        # Actualiza el movimiento de la pelota y las paletas
        self.player.move()
        self.opponent_ai()
        self.ball.move()
        self.ball.check_collision(self.player, self.opponent)

        # Verificar si la pelota sale de los límites para el puntaje
        if self.ball.rect.left <= 0:
            self.player_score += 1
            self.ball.reset()
        if self.ball.rect.right >= SCREEN_WIDTH:
            self.opponent_score += 1
            self.ball.reset()

    def opponent_ai(self):
        # Movimiento de la paleta del oponente (IA simple)
        if self.opponent.rect.centery < self.ball.rect.centery:
            self.opponent.speed = PADDLE_SPEED
        elif self.opponent.rect.centery > self.ball.rect.centery:
            self.opponent.speed = -PADDLE_SPEED
        else:
            self.opponent.speed = 0
        self.opponent.move()

    def draw_elements(self):
        # Dibuja los elementos en pantalla
        self.screen.fill(BLACK)
        pygame.draw.rect(self.screen, WHITE, self.player.rect)
        pygame.draw.rect(self.screen, WHITE, self.opponent.rect)
        pygame.draw.ellipse(self.screen, WHITE, self.ball.rect)
        pygame.draw.aaline(self.screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))
        self.draw_score()

    def draw_score(self):
        # Dibuja el puntaje en pantalla
        font = pygame.font.Font(None, 36)
        player_text = font.render(f"{self.player_score}", True, WHITE)
        opponent_text = font.render(f"{self.opponent_score}", True, WHITE)
        self.screen.blit(player_text, (SCREEN_WIDTH // 2 + 20, 20))
        self.screen.blit(opponent_text, (SCREEN_WIDTH // 2 - 40, 20))

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw_elements()
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    game = PongGame()
    game.run()
