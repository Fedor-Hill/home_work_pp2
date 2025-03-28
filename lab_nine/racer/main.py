import time
from random import randint

import pygame

pygame.init()

# For Drive Music
pygame.mixer.init()
pygame.mixer.music.load("Kavinsky-Nightcall.mp3")
pygame.mixer.music.play(-1)

# CONSTANTS
W, H = 450, 600
SCREEN = pygame.display.set_mode((W, H))
GREY = (128, 128, 128)
RED = (255, 0, 0)
ROAD_BG = pygame.image.load("assets/road2.png").convert()
COIN_ICON = pygame.image.load("assets/nitro.png")
COIN_ICON_GREEN = pygame.image.load("assets/nitro_green.png")
COIN_ICON_RED = pygame.image.load("assets/nitro_red.png")


# Countable values
speed_enemy = 3
speed_coin = 5
score_enemy = 0
score_coins = 0

# Clock, FPS, Event
clock = pygame.time.Clock()
ENEMY_EVENT = pygame.USEREVENT + 1
COIN_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(ENEMY_EVENT, 1000)
pygame.time.set_timer(COIN_EVENT, 2000)

# Font
font = pygame.font.Font(None, 60)
font_scores = pygame.font.Font(None, 40)
game_over = font.render("Bad Drive", True, (0, 0, 0))

class Coin(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.weight = 1
        self.image = COIN_ICON
        self.rect = self.image.get_rect()
        self.rect.center = (randint(50, W - 50), 0)

    def move(self):
        self.rect.move_ip(0, speed_coin)
        # if self.rect.bottom > h + self.rect.height:
        # self.rect.center = (w - 48, 10)

    def claim(self):
        self.rect.top = H

    # RED - 3 point
    # GREEN - 2 point
    # DEFAULT - 1 point
    def spawn(self):
        self.weight = randint(1, 3)
        self.rect.center = (randint(50, W - 50), 0)
        if self.weight == 1: 
            self.image = COIN_ICON
        elif self.weight == 2: 
            self.image = COIN_ICON_GREEN
        else: 
            self.image = COIN_ICON_RED

    def get_weight(self) -> int: 
        return self.weight


class Enemy(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load("assets/pink.png")
        self.rect = self.image.get_rect()
        self.rect.center = (randint(60, W - 60), 0)

    def move(self):
        self.rect.move_ip(0, speed_enemy)
        if self.rect.bottom > H + self.rect.height:
            global score_enemy
            score_enemy += 1
            self.rect.top = 0
            self.rect.center = (randint(60, W - 60), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load("assets/hornet.png")
        self.rect = self.image.get_rect()
        self.rect.center = (W // 2 - self.rect.width // 2, H - self.rect.height)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 50:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-speed_enemy, 0)
        if self.rect.right < W - 50:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(speed_enemy, 0)


E = Enemy()
P = Player()
C = Coin()

# Sprites group
enemies = pygame.sprite.Group()
enemies.add(E)
coins = pygame.sprite.Group()
coins.add(C)
all_sprites = pygame.sprite.Group()
all_sprites.add(P)
all_sprites.add(E)
all_sprites.add(C)
 
Drive = True

time.sleep(11.5)

while Drive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("BYE BYE !")
            Drive = False

        if event.type == ENEMY_EVENT and speed_enemy < 20:
            speed_enemy += 0.5
            print(speed_enemy)

        if event.type == COIN_EVENT:
            # For random appear time coin
            pygame.time.set_timer(COIN_EVENT, randint(2000, 6000) )
            C.spawn()

            if score_coins % 2 == 0:
                speed_coin += 0.2

            elif score_coins % 3 == 0:
                speed_enemy += 0.5

    SCREEN.blit(ROAD_BG, (0, 0))

    # UPDATE scores
    scores_enemy = font_scores.render(str(score_enemy), True, (0, 0, 0))
    scores_coin = font_scores.render(str(score_coins), True, (0, 0, 0))
    SCREEN.blit(scores_enemy, (5, 10))
    SCREEN.blit(scores_coin, (W - 25, 10))

    # UPDATE postions all sprites
    for thing in all_sprites:
        SCREEN.blit(thing.image, thing.rect)
        thing.move()

    # CHECK collisions
    if pygame.sprite.spritecollideany(P, enemies):
        pygame.mixer.music.unload()
        pygame.mixer.Sound("assets/crash.mp3").play()
        time.sleep(0.5)

        SCREEN.fill(RED)
        SCREEN.blit(game_over, (W // 2 - game_over.get_width() // 2, H // 2))
        pygame.display.update()

        for entity in all_sprites:
            entity.kill()

        time.sleep(2)
        Drive = False

    if pygame.sprite.spritecollideany(P, coins):
         

        for entity in coins:
            entity.claim()
            score_coins += entity.get_weight()

    # UPDATE FPS and display
    pygame.display.update()
    clock.tick(60)

pygame.quit()
