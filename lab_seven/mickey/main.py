from datetime import datetime
import pygame

w, h = 800, 600
run = True

pygame.init()

screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

background = pygame.image.load("clock.png")
min_hand = pygame.image.load("min_hand.png")
sec_hand = pygame.image.load("sec_hand.png")


original_rect_sh = sec_hand.get_rect(center=(w // 2, h // 2))
original_rect_mh = min_hand.get_rect(center=(w // 2, h // 2))

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            print("BYE BYE !")
    screen.blit(background, (0, 0))

    now = datetime.now()
    seconds = now.second
    minutes = now.minute

    rotated_sh = pygame.transform.rotate(sec_hand, seconds * -6)
    rotated_bh = pygame.transform.rotate(min_hand, minutes * -6)
    rotated_rect_sh = rotated_sh.get_rect(center=original_rect_sh.center)
    rotated_rect_bh = rotated_bh.get_rect(center=original_rect_mh.center)

    screen.blit(rotated_sh, rotated_rect_sh.topleft)
    screen.blit(rotated_bh, rotated_rect_bh.topleft)

    # print(f"seconds = {seconds}")

    pygame.display.flip()
    clock.tick(30)
