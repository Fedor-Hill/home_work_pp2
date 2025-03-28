import pygame
import math

pygame.init()

'''
Hot Keys

1 - Brush
2 - Rectangle
3 - Circle 
4 - Square
5 - right triangle
6 - equilateral
7 - rhombus
E - Eraser 

+ or - -- thickness

R - Red color 
G - Green color 
B - Blue color

'''

# CONSTANTS
W, H = 800, 600
SCREEN = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Values
drawing = False
tool = "brush"  # "brush", "rect", "circle", "eraser" and other
color = BLUE
thickness = 5
start_pos = (0, 0)
last_pos = None

background = pygame.Surface((W, H))
background.fill(WHITE)

Art = True
while Art:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Bye Bye !")
            Art = False

        # Check key press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                tool = "brush"
            elif event.key == pygame.K_2:
                tool = "rect"
            elif event.key == pygame.K_3:
                tool = "circle"
            elif event.key == pygame.K_4:
                tool = "square"
            elif event.key == pygame.K_5:
                tool = "triangle"
            elif event.key == pygame.K_6:
                tool = "equilateral"
            elif event.key == pygame.K_7:
                tool = "rhombus"
            elif event.key == pygame.K_e:
                tool = "eraser"
            elif event.key == pygame.K_r:
                color = RED
            elif event.key == pygame.K_g:
                color = GREEN
            elif event.key == pygame.K_b:
                color = BLUE
            elif event.key == pygame.K_w:
                color = WHITE
            elif event.key == pygame.K_EQUALS:
                thickness += 5
                print(thickness)
            elif event.key == pygame.K_MINUS:
                thickness -= 5
                if (thickness < 0): thickness = 5
                print(thickness)

        # UPDATE the mouse action
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                start_pos = event.pos
                last_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and drawing:
                end_pos = event.pos
                x1, y1 = start_pos
                x2, y2 = end_pos

                if tool == "rect":
                    pygame.draw.rect(background, color, pygame.Rect(
                        min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1)), thickness)
                elif tool == "circle":
                    radius = int(math.hypot(x2 - x1, y2 - y1))
                    pygame.draw.circle(background, color, start_pos, radius, thickness)
                elif tool == "square":
                    side = min(abs(x2 - x1), abs(y2 - y1))
                    pygame.draw.rect(background, color, (x1, y1, side, side), thickness)
                elif tool == "triangle":
                    points = [(x1, y2), (x2, y2), (x1, y1)]
                    pygame.draw.polygon(background, color, points, thickness)
                elif tool == "equilateral":
                    height = abs(y2 - y1)
                    base_half = height / math.sqrt(3)
                    points = [(x1, y2), (x1 - base_half, y1), (x1 + base_half, y1)]
                    pygame.draw.polygon(background, color, points, thickness)
                elif tool == "rhombus":
                    width = abs(x2 - x1)
                    height = abs(y2 - y1)
                    points = [(x1, y1 - height // 2), (x1 + width // 2, y1),
                              (x1, y1 + height // 2), (x1 - width // 2, y1)]
                    pygame.draw.polygon(background, color, points, thickness)
                elif tool == "eraser":
                    pygame.draw.circle(background, WHITE, start_pos, thickness)

                drawing = False
    
        if event.type == pygame.MOUSEMOTION and drawing:
            if tool == "eraser":
                pygame.draw.circle(background, WHITE, event.pos, thickness)
            if tool == "brush": 
                if last_pos is not None:
                    pygame.draw.line(background, color, last_pos, event.pos, thickness)
                    last_pos = event.pos

    SCREEN.blit(background, (0, 0))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
