import pygame
import time
import random
import sys

# Initialize Pygame
pygame.init()

# Define colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
yellow = (255, 255, 102)
purple = (128, 0, 128)

# Define screen width and height
dis_width = 600
dis_height = 400

# Create the game window
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by ChatGPT')

# Set the clock for controlling the game's frame rate
clock = pygame.time.Clock()

# Snake block size
snake_block = 10

# Font styles
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


# Functions to display score
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


# Function to draw the snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


# Message function for end of the game
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


# Function for the game loop
def gameLoop():
    game_over = False
    game_close = False

    # Snake speed moved inside gameLoop
    snake_speed = 10

    # Starting position
    x1 = dis_width / 2
    y1 = dis_height / 2

    # Movement
    x1_change = 0
    y1_change = 0

    # Snake body list
    snake_List = []
    Length_of_snake = 1

    # Food Position
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    # Starting movement direction
    direction = 'RIGHT'
    change_to = direction

    while not game_over:

        while game_close:
            dis.fill(purple)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            # Event handling after game over
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != 'RIGHT':
                    x1_change = -snake_block
                    y1_change = 0
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    x1_change = snake_block
                    y1_change = 0
                    direction = 'RIGHT'
                elif event.key == pygame.K_UP and direction != 'DOWN':
                    y1_change = -snake_block
                    x1_change = 0
                    direction = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    y1_change = snake_block
                    x1_change = 0
                    direction = 'DOWN'

        # If snake hits boundary
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(purple)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # If snake collides with itself
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        # Snake eats food
        if x1 == foodx and y1 == foody:
            foodx = round(
                random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(
                random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            snake_speed += 0.5  # Increase speed as snake grows (Optional)

        clock.tick(snake_speed)

    pygame.quit()
    sys.exit()


# Start the game
gameLoop()
