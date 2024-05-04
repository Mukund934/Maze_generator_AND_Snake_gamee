import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BLOCK_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // BLOCK_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // BLOCK_SIZE

# Set colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set game variables
snake_pos = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
snake_direction = (1, 0)
snake_length = 1
food_pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("AI Snake Game")

# Set clock for controlling the game's frame rate
clock = pygame.time.Clock()

# Function to draw the snake and food
def draw():
    screen.fill(WHITE)
    for pos in snake_pos:
        pygame.draw.rect(screen, GREEN, (pos[0] * BLOCK_SIZE, pos[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, RED, (food_pos[0] * BLOCK_SIZE, food_pos[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    pygame.display.update()

# Function to update the game state
def update():
    global snake_pos, snake_length, food_pos

    # Update snake's position
    head = (snake_pos[0][0] + snake_direction[0], snake_pos[0][1] + snake_direction[1])
    if head in snake_pos or head[0] < 0 or head[0] >= GRID_WIDTH or head[1] < 0 or head[1] >= GRID_HEIGHT:
        pygame.quit()
        quit()
    snake_pos.insert(0, head)

    # Check if snake eats the food
    if snake_pos[0] == food_pos:
        food_pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        snake_length += 1
    else:
        snake_pos.pop()

# Function to move the snake towards the food
def move_towards_food():
    global snake_direction

    # Get current snake head position
    head_x, head_y = snake_pos[0]
    food_x, food_y = food_pos

    # Move towards food
    if food_x > head_x:
        snake_direction = (1, 0)
    elif food_x < head_x:
        snake_direction = (-1, 0)
    elif food_y > head_y:
        snake_direction = (0, 1)
    elif food_y < head_y:
        snake_direction = (0, -1)

# Main game loop
def main():
    while True:
        move_towards_food()
        update()
        draw()
        clock.tick(10)

if __name__ == "__main__":
    main()
