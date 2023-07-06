import pygame
import random
from collections import deque

# Initialize Pygame
pygame.init()

# Set the screen dimensions
screen_width = 640
screen_height = 480
grid_size = 20

# Set the colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

# Set the initial direction of the snake
direction = "RIGHT"

# Set the initial position of the food or Snake
def random_pos():
    return [random.randrange(1, screen_width // grid_size) * grid_size,
            random.randrange(1, screen_height // grid_size) * grid_size]

def display_score(score):
    score_text = font_style.render("Score: " + str(score), True, white)
    screen.blit(score_text, [10, 10])

def game_over():
    message = font_style.render("Game Over", True, white)
    screen.blit(message, [screen_width // 2 - 60, screen_height // 2 - 30])
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()



# Set the initial position of the snake
snake_pos = deque([[screen_width // 2, screen_height // 2]])

#Food Position and Snake position cannot be the same
while True:
    food_pos = random_pos()
    if food_pos != snake_pos[0]:
        break
    
food_spawned = True

# Set the clock to control the frame rate
clock = pygame.time.Clock()

# Set the font for displaying the score
font_style = pygame.font.SysFont(None, 30)




# Create the game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Start the game loop
score = 0
game_in_play = True

while game_in_play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_in_play = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    #Shift snake body elements along by one
    snake_pos.rotate(1)
    
    #Now update the snake's head pos
    if direction == "UP":
        snake_pos[0][1] -= grid_size
    elif direction == "DOWN":
        snake_pos[0][1] += grid_size
    elif direction == "LEFT":
        snake_pos[0][0] -= grid_size
    elif direction == "RIGHT":
        snake_pos[0][0] += grid_size

    #If Snake collides with walls --> Game over
    if snake_pos[0][0] < 0 or snake_pos[0][0] >= screen_width or \
            snake_pos[0][1] < 0 or snake_pos[0][1] >= screen_height:
        game_over()

    #If snake hits own body --> Game Over
    if snake_pos[0] in list(snake_pos)[1:]:
        game_over()

    if snake_pos[0] == food_pos:
        score += 1
        food_spawned = False
        #Need to append new tail as snake grows
        

    if not food_spawned:
        food_pos = random_pos()
        food_spawned = True

    screen.fill(black)

    for pos in snake_pos:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], grid_size, grid_size))

    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], grid_size, grid_size))

    display_score(score)

    pygame.display.flip()

    clock.tick(5)

# Quit the game
pygame.quit()

