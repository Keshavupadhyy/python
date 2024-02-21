import pygame

import pygame
import time
import random

pygame.init()

# Set up display
width, height = 800, 600
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set up Snake and Apple
snake_block = 10
snake_speed = 15
font = pygame.font.SysFont(None, 35)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, white, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font.render(msg, True, color)
    game_display.blit(mesg, [width / 6, height / 3])

def game_loop():
    game_over = False
    game_close = False

    # Initialize Snake
    snake_list = []
    length_of_snake = 1

    # Initial position and speed of the snake
    lead_x = width / 2
    lead_y = height / 2
    lead_x_change = 0
    lead_y_change = 0

    # Initial position of the apple
    apple_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    apple_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            game_display.fill(black)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -snake_block
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = snake_block
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -snake_block
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = snake_block
                    lead_x_change = 0

        # Update snake position
        lead_x += lead_x_change
        lead_y += lead_y_change

        # Check if the snake hits the boundaries
        if lead_x >= width or lead_x < 0 or lead_y >= height or lead_y < 0:
            game_close = True

        game_display.fill(black)
        pygame.draw.rect(game_display, red, [apple_x, apple_y, snake_block, snake_block])
        our_snake(snake_block, snake_list)

        # Check if the snake eats the apple
        if lead_x == apple_x and lead_y == apple_y:
            apple_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            apple_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        # Update snake body
        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check if the snake collides with itself
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        pygame.display.update()

        pygame.time.Clock().tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
