import pygame

width, height = 800, 600
radius = 25

pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
run = True

x, y = 400, 300

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("BYE BYE !")
            run = False
    
    screen.fill((255, 255, 255))

    pressed = pygame.key.get_pressed()
 
    # HINT: ELIF for make only for one direction

    if pressed[pygame.K_UP] and y > radius: y -= 20
    if pressed[pygame.K_DOWN] and y < height - radius: y += 20
    if pressed[pygame.K_LEFT] and x > radius: x -= 20
    if pressed[pygame.K_RIGHT] and x < width - radius: x += 20

    # print(f"x = {x} and y = {y}")

    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)

    pygame.display.flip()
    clock.tick(60)
