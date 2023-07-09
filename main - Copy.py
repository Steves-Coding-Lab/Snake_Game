import pygame, sys, os, math
import random
import copy

# Initialize Pygame
pygame.init()

# Set the screen dimensions
screen_width = 880
screen_height = 640
grid_size = 40

# Set the colors
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
grass = pygame.Color(77, 87, 43)

current_dir = os.path.dirname(__file__)
snake_image_path = os.path.join(current_dir, "img", "snake-head.png")
body_image_path = os.path.join(current_dir, "img", "snake-body.png")

# Load your PNG image
snake_image = pygame.image.load(snake_image_path)
body_image = pygame.image.load(body_image_path)
# Resize the image
snake_image = pygame.transform.scale(snake_image, (45,45))
snake_image = pygame.transform.rotate(snake_image, -90) 
# Set the initial direction of the snake
direction = "RIGHT"
head_angle = 90 #facing right
body_image = pygame.transform.scale(body_image, (45,45))

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
    sys.exit()

#Food cannot be spawned inside Snake
def spawn_food():
    while True:
        food_pos = random_pos()
        if food_pos not in snake_pos:
            return food_pos

# Set the initial position of the snake
snake_pos = [[screen_width // 2, screen_height // 2]]



food_pos = spawn_food()
food_spawned = True

# Set the clock to control the frame rate
clock = pygame.time.Clock()

# Set the font for displaying the score
font_style = pygame.font.SysFont(None, 30)

# Create the game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

score = 0 #initialise score
# Start the game loop
while True:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
                if head_angle == 90:
                    snake_image = pygame.transform.rotate(snake_image, 90)
                else:
                    snake_image = pygame.transform.rotate(snake_image, -90)
                head_angle = 0
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
                if head_angle == 90:
                    snake_image = pygame.transform.rotate(snake_image, -90)
                else:
                    snake_image = pygame.transform.rotate(snake_image, 90)
                head_angle = 180
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
                if head_angle == 0:
                    snake_image = pygame.transform.rotate(snake_image, 90)
                else:
                    snake_image = pygame.transform.rotate(snake_image, -90)
                head_angle = 270
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"
                if head_angle == 0:
                    snake_image = pygame.transform.rotate(snake_image, -90)
                else:
                    snake_image = pygame.transform.rotate(snake_image, 90)
                head_angle = 90
        
    prev_head = copy.copy(snake_pos[0]) #must make a copy since variables are references to objects
   
    #Now update the snake's head pos
    if direction == "UP":
        snake_pos[0][1] -= grid_size
    elif direction == "DOWN":
        snake_pos[0][1] += grid_size
    elif direction == "LEFT":
        snake_pos[0][0] -= grid_size
    elif direction == "RIGHT":
        snake_pos[0][0] += grid_size

    # Update snake's tail position
    if len(snake_pos) > 1:
        #If snake hits own body --> Game Over
        if snake_pos[0] in snake_pos[1:]:
            game_over()
        snake_pos.pop()
        snake_pos.insert(1, prev_head)

    #If Snake collides with walls --> Game over
    if snake_pos[0][0] < 0 or snake_pos[0][0] >= screen_width or \
            snake_pos[0][1] < 0 or snake_pos[0][1] >= screen_height:
        game_over()

    if snake_pos[0] == food_pos:
        score += 1
        food_spawned = False
        #Need to append new tail as snake grows
        snake_pos.append(prev_head)

    if not food_spawned:
        food_pos = spawn_food()
        food_spawned = True

    screen.fill(grass)

    
    screen.blit(snake_image, snake_pos[0])
    for pos in snake_pos[1:]:
        screen.blit(body_image, pos)
    
    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], grid_size, grid_size))

    display_score(score)

    pygame.display.flip()

    clock.tick(6)