import pygame
import random
import sys

# Configuración inicial
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 5
BULLET_SPEED = 7
ENEMY_SPEED = 2
ENEMY_DROP = 40

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Inicializa Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

# Clase del jugador
class Player:
    def __init__(self):
        self.image = pygame.Surface((50, 30))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(midbottom=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 30))
        self.speed = PLAYER_SPEED
        self.bullets = []

    def move(self, direction):
        if direction == "left" and self.rect.left > 0:
            self.rect.x -= self.speed
        elif direction == "right" and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        self.bullets.append(bullet)

    def update_bullets(self):
        for bullet in self.bullets[:]:
            bullet.move()
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)

# Clase de los disparos
class Bullet:
    def __init__(self, x, y):
        self.image = pygame.Surface((5, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = BULLET_SPEED

    def move(self):
        self.rect.y -= self.speed

# Clase de los enemigos
class Enemy:
    def __init__(self, x, y):
        self.image = pygame.Surface((40, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = ENEMY_SPEED

    def move(self, direction):
        if direction == "right":
            self.rect.x += self.speed
        elif direction == "left":
            self.rect.x -= self.speed

# Clase principal del juego
class SpaceInvaders:
    def __init__(self):
        self.player = Player()
        self.enemies = self.create_enemies()
        self.direction = "right"
        self.score = 0
        self.lives = 3

    def create_enemies(self):
        enemies = []
        for row in range(3):
            for col in range(8):
                x = col * 60 + 50
                y = row * 50 + 50
                enemy = Enemy(x, y)
                enemies.append(enemy)
        return enemies

    def move_enemies(self):
        # Mueve enemigos y baja cuando alcanzan los bordes
        move_down = False
        for enemy in self.enemies:
            enemy.move(self.direction)
            if enemy.rect.right >= SCREEN_WIDTH or enemy.rect.left <= 0:
                move_down = True

        if move_down:
            self.direction = "left" if self.direction == "right" else "right"
            for enemy in self.enemies:
                enemy.rect.y += ENEMY_DROP

    def check_collisions(self):
        for bullet in self.player.bullets[:]:
            for enemy in self.enemies[:]:
                if bullet.rect.colliderect(enemy.rect):
                    self.player.bullets.remove(bullet)
                    self.enemies.remove(enemy)
                    self.score += 10
                    break

    def check_game_over(self):
        for enemy in self.enemies:
            if enemy.rect.bottom >= SCREEN_HEIGHT:
                self.lives -= 1
                self.enemies = self.create_enemies()
                if self.lives <= 0:
                    return True
        return False

    def draw(self):
        screen.fill(BLACK)
        screen.blit(self.player.image, self.player.rect)
        for bullet in self.player.bullets:
            screen.blit(bullet.image, bullet.rect)
        for enemy in self.enemies:
            screen.blit(enemy.image, enemy.rect)
        
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, WHITE)
        lives_text = font.render(f"Lives: {self.lives}", True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (SCREEN_WIDTH - 120, 10))

    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.shoot()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.player.move("left")
            if keys[pygame.K_RIGHT]:
                self.player.move("right")

            # Actualiza lógica del juego
            self.player.update_bullets()
            self.move_enemies()
            self.check_collisions()

            if self.check_game_over():
                print("Game Over")
                break

            # Dibuja en pantalla
            self.draw()
            pygame.display.flip()
            clock.tick(60)

if __name__ == "__main__":
    game = SpaceInvaders()
    game.run()
