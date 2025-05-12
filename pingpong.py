
import pygame
import sys
from pygame.locals import *

pygame.init()

# Definir dimensões da janela
WIDTH, HEIGHT = 640, 480
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ping Pong Game')
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([10, 100])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move_up(self):
        self.rect.y -= 5

    def move_down(self):
        self.rect.y += 5

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2
        self.rect.y = HEIGHT // 2
        self.speed_x = 3
        self.speed_y = 3

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.y <= 0 or self.rect.y >= HEIGHT - 10:
            self.speed_y = -self.speed_y

        if self.rect.x <= 0 or self.rect.x >= WIDTH - 10:
            self.speed_x = -self.speed_x
paddle_left = Paddle(20, HEIGHT // 2 - 50)
paddle_right = Paddle(WIDTH - 30, HEIGHT // 2 - 50)
ball = Ball()

all_sprites = pygame.sprite.Group()
all_sprites.add(paddle_left)
all_sprites.add(paddle_right)
all_sprites.add(ball)
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[K_w]:
        paddle_left.move_up()
    if keys[K_s]:
        paddle_left.move_down()
    if keys[K_UP]:
        paddle_right.move_up()
    if keys[K_DOWN]:
        paddle_right.move_down()

    all_sprites.update()

    window.fill(BLACK)
    all_sprites.draw(window)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
