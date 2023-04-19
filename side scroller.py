import pygame
import random

# Initialize Pygame
pygame.init()

# Set the game window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Create the game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set the game clock
clock = pygame.time.Clock()

# Load the player image
player_image = pygame.image.load('char1.png')
player_image = pygame.transform.scale(player_image, (64, 64))

# Set the player starting position and speed
player_x = 50
player_y = WINDOW_HEIGHT - player_image.get_height() - 50
player_speed = 5

# Load the background image
background_image = pygame.image.load('bg.png')

# Set the background starting position and speed
background_x = 0
background_speed = 2

# Load the obstacle image
obstacle_image = pygame.image.load('obst2.png')
obstacle_image = pygame.transform.scale(obstacle_image, (64, 64))

# Set the obstacle starting position and speed
obstacle_x = WINDOW_WIDTH
obstacle_y = WINDOW_HEIGHT - obstacle_image.get_height() - 50
obstacle_speed = 8

# Set the game score
score = 0

# Set the game font
font = pygame.font.Font(None, 36)

# Start the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the background
    background_x -= background_speed
    if background_x <= -background_image.get_width():
        background_x = 0

    # Move the obstacle
    obstacle_x -= obstacle_speed
    if obstacle_x <= -obstacle_image.get_width():
        obstacle_x = WINDOW_WIDTH
        obstacle_y = random.randint(50, WINDOW_HEIGHT - obstacle_image.get_height() - 50)
        score += 1

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < WINDOW_HEIGHT - player_image.get_height():
        player_y += player_speed

    # Check for collision between player and obstacle
    if pygame.Rect(player_x, player_y, player_image.get_width(), player_image.get_height()).colliderect(
            pygame.Rect(obstacle_x, obstacle_y, obstacle_image.get_width(), obstacle_image.get_height())):
        running = False

    # Draw the game objects
    window.blit(background_image, (background_x, 0))
    window.blit(background_image, (background_x + background_image.get_width(), 0))
    window.blit(player_image, (player_x, player_y))
    window.blit(obstacle_image, (obstacle_x, obstacle_y))
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    window.blit(score_text, (10, 10))

    # Update the display
    pygame.display.update()

    # Tick the clock
    clock.tick(60)

# Show the game over message
game_over_text = font.render('Game Over', True, (255, 255, 255))
window.blit(game_over_text, ((WINDOW_WIDTH - game_over_text.get_width()) // 2, (WINDOW_HEIGHT - game_over_text.get_height()) // 2))
pygame.display.update()

# Wait for the user to close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()