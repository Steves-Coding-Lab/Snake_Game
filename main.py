import pygame
import random

# Initialize Pygame
pygame.init()

# Set the screen dimensions
screen_width = 640
screen_height = 480

# Set the colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

# Set the initial position and size of the snake
snake_pos = [[100, 50], [90, 50], [80, 50]]
snake_size = 10

# Set the initial direction of the snake
direction = "RIGHT"

# Set the initial position of the food
food_pos = [random.randrange(1, screen_width // 10) * 10,
            random.randrange(1, screen_height // 10) * 10]
food_spawned = True

# Set the clock to control the frame rate
clock = pygame.time.Clock()

# Set the font for displaying the score
font_style = pygame.font.SysFont(None, 30)


def display_score(score):
    score_text = font_style.render("Score: " + str(score), True, white)
    screen.blit(score_text, [10, 10])


def game_over():
    message = font_style.render("Game Over", True, white)
    screen.blit(message, [screen_width // 2 - 60, screen_height // 2 - 30])
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()


# Create the game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Start the game loop
score = 0
game_over_flag = False

while not game_over_flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over_flag = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    if direction == "UP":
        snake_pos[0][1] -= snake_size
    elif direction == "DOWN":
        snake_pos[0][1] += snake_size
    elif direction == "LEFT":
        snake_pos[0][0] -= snake_size
    elif direction == "RIGHT":
        snake_pos[0][0] += snake_size

    if snake_pos[0][0] < 0 or snake_pos[0][0] >= screen_width or \
            snake_pos[0][1] < 0 or snake_pos[0][1] >= screen_height:
        game_over()

    if snake_pos[0] in snake_pos[1:]:
        game_over()

    if snake_pos[0] == food_pos:
        score += 1
        food_spawned = False
    else:
        snake_pos.pop()

    if not food_spawned:
        food_pos = [random.randrange(1, screen_width // 10) * 10,
                    random.randrange(1, screen_height // 10) * 10]
        food_spawned = True

    screen.fill(black)

    for pos in snake_pos:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], snake_size, snake_size))

    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], snake_size, snake_size))

    display_score(score)

    pygame.display.flip()

    clock.tick(20)

# Quit the game
pygame.quit()

