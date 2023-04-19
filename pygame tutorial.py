import pygame
import random

# Initialize Pygame
pygame.init()

# Set the game window dimensions
window_width = 640
window_height = 480

# Create the game window
window = pygame.display.set_mode((window_width, window_height))

# Set the game window caption
pygame.display.set_caption('Simple Game')

# Define some colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set the game clock
clock = pygame.time.Clock()


# Define the player class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed


# Define the enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, window_width - self.rect.width)
        self.rect.y = random.randint(0, window_height - self.rect.height)
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > window_height:
            self.rect.x = random.randint(0, window_width - self.rect.width)
            self.rect.y = random.randint(self.rect.height, 50)
            self.speed = random.randint(1, 3)


# Create the player sprite
player = Player(window_width // 2, window_height // 2)

# Create a group for the enemies
enemies = pygame.sprite.Group()
for i in range(10):
    enemy = Enemy()
    enemies.add(enemy)

# Start the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game objects
    player.update()
    enemies.update()

    # Check for collisions
    if pygame.sprite.spritecollide(player, enemies, False):
        running = False

    # Draw game objects
    window.fill(black)
    pygame.draw.rect(window, white, player.rect)
    enemies.draw(window)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()