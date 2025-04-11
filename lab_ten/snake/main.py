import random
import time
import pygame
import psg

psg.start()

name = str(input("Your name: "))
user = psg.get_user(name)

pygame.init()

w, h = 400, 400
screen = pygame.display.set_mode((w, h))

# Colors
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLUE = pygame.Color(0, 0, 255)

# For control FPS that influence to speed of snake
# snake_speed is limit to clock
clock = pygame.time.Clock()
snake_speed = user.speed

font = pygame.font.Font(None, 24)

# Coordinates of snake body and head
# Movement of snake
snake_head = [user.position[0][0], user.position[0][1]] if user.position != None else [w // 2, h // 2]
snake_body = user.position if user.position != None else [[w//2, h//2], [w//2-10, h//2], [w//2-20, h//2], [w//2-30, h//2]]
direction = user.saved_direction if user.saved_direction != None else "RIGHT"
change_to = direction
# Countable value
score = user.score
level = user.level
foods_eaten = 0

Eating = True
pause = False

def game_over():
    Eating = False
    user.score = 0 
    user.level = 1
    user.speed = 10 
    user.position = None
    user.saved_direction = None
    psg.save_data(user)
    screen.fill(BLACK)
    final_text = font.render(f"Game Over! Your Score: {score}", True, RED)
    screen.blit(final_text, (w // 4, h // 3))
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()


def generate_fruit_position():
    while True:
        pos = [random.randrange(1, (w // 10)) * 10, random.randrange(1, (h // 10)) * 10]
        if pos not in snake_body and 0 < pos[0] < w - 10 and 0 < pos[1] < h - 10:
            return pos

# Fruit options
fruit_pos = generate_fruit_position()
fruit_spawn = True
fruit_weight = 1 # 1 - white, 2 - blue, 3 - red
fruit_color = WHITE
FRUIT_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(FRUIT_EVENT, 3000)

while Eating:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            user.saved_direction = direction
            if snake_head == snake_body[1]:
                snake_body.pop(0)
            user.position = snake_body
            psg.save_data(user)
            print("BYE BYE !")
            Eating = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                change_to = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                change_to = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                change_to = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                change_to = "RIGHT"
            elif event.key == pygame.K_p:
                pause = not pause

        if event.type == FRUIT_EVENT:
            pygame.time.set_timer(FRUIT_EVENT, 3000)
            fruit_spawn = False
            # Check for friut
            if not fruit_spawn:
                fruit_pos = generate_fruit_position()
                fruit_spawn = True
                fruit_weight = random.randint(1, 3)

                if fruit_weight == 1:
                    fruit_color = WHITE
                elif fruit_weight == 2:
                    fruit_color = BLUE
                else:
                    fruit_color = RED

    if pause:
        continue

    direction = change_to

    # Update head
    if direction == "UP":
        snake_head[1] -= 10
    elif direction == "DOWN":
        snake_head[1] += 10
    elif direction == "LEFT":
        snake_head[0] -= 10
    elif direction == "RIGHT":
        snake_head[0] += 10

    # Update body coordinates after movement of head
    snake_body.insert(0, list(snake_head))

    if snake_head == fruit_pos:
        score += 10 * fruit_weight
        user.score = score
        foods_eaten += 1
        pygame.time.set_timer(FRUIT_EVENT, 1)
    else:
        # Delete last useless coordinate
        snake_body.pop()
    
    print(snake_body)
    
    for block in snake_body[1:]:
        if snake_head == block:
            print("DEATH by intersection")
            print(f"DEATH HEAD {snake_head} and block {block}")
            game_over()

    # Check collision for game over
    if (
        snake_head[0] < 0
        or snake_head[0] >= w
        or snake_head[1] < 0
        or snake_head[1] >= h
    ):
        print("DEATH by wall")
        game_over()

   

    # Upd. of score and level
    if foods_eaten > 2:
        level += 1
        snake_speed += 2
        foods_eaten = 0
        user.level = level 
        user.speed = snake_speed

    screen.fill(BLACK)

    # Draw snake by coordinates
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

    # Draw fruit by coordinate
    pygame.draw.rect(
        screen, fruit_color, pygame.Rect(fruit_pos[0], fruit_pos[1], 10, 10)
    )

    

    # Show Countable values
    info_text = font.render(f"Score: {score} Level: {level}", True, WHITE)
    screen.blit(info_text, (10, 10))

    # Update clock and display
    pygame.display.update()
    clock.tick(snake_speed)
