import pygame

pygame.init()

# Set screen dimensions
screen_width = 800
screen_height = 600

# Create screen surface
screen = pygame.display.set_mode((screen_width, screen_height))

# Load PNG images and store them in a dictionary based on map key
images = {}
images['g'] = pygame.image.load("bg_grass.bmp")
images['t'] = pygame.image.load("bg_tree.bmp")
images['w'] = pygame.image.load("bg_water.bmp")
images['s'] = pygame.image.load("bg_sand.bmp")
images['p'] = pygame.image.load("bg_pavement.bmp")
images['h'] = pygame.image.load("bg_house.bmp")
images['r'] = pygame.image.load("bg_grock.bmp")
# ... add more images and keys as needed

# Define the map using a 2D list of keys
map_key = [
    ['g', 'g', 'p', 't', 't', 'g', 'g', 's', 'w', 'w', 'w', 'w', 'w'],
    ['g', 'g', 'p', 't', 't', 'g', 'g', 's', 'w', 'w', 'w', 'w', 'w'],
    ['g', 'g', 'p', 'p', 'g', 'g', 'g', 's', 'w', 'w', 'w', 's', 'w'],
    ['g', 't', 't', 'p', 'g', 'g', 's', 's', 'w', 'w', 'w', 's', 'w'],
    ['g', 't', 't', 'p', 'g', 'g', 's', 'w', 'w', 'w', 'w', 'w', 'w'],
    ['r', 'r', 'g', 'p', 'g', 's', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
    ['r', 'r', 'g', 'p', 'g', 's', 's', 's', 'w', 'w', 'w', 'w', 'w'],
    ['g', 'h', 'p', 'p', 'g', 'r', 'g', 't', 's', 'w', 'w', 'w', 'w'],
    ['t', 'g', 't', 'p', 'g', 't', 'g', 'g', 's', 's', 'w', 'w', 'w'],
    ['g', 'g', 'g', 'p', 'g', 't', 'g', 'g', 'g', 's', 's', 'w', 'w'],
    ['g', 'g', 'g', 'p', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 's', 's'],
    ['g', 't', 'g', 'p', 'r', 'g', 'g', 't', 'g', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'g', 'p', 'g', 't', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],
    ['p', 'p', 'p', 'p', 'g', 'g', 'g', 'g', 's', 's', 'g', 'g', 'g'],
    ['t', 'g', 'g', 'p', 't', 'g', 'g', 'g', 's', 's', 'g', 'r', 'g'],
    ['g', 'g', 'g', 'p', 'g', 'g', 'g', 's', 's', 's', 'g', 'g', 'g'],
    ['g', 't', 'g', 'p', 'p', 'p', 'r', 's', 's', 's', 'g', 'g', 'w'],
    ['g', 'r', 'g', 'p', 't', 'p', 's', 's', 's', 's', 's', 'g', 'w'],
    ['g', 'g', 'g', 'p', 'p', 'p', 's', 's', 's', 's', 's', 'g', 'g'],
]

# Calculate dimensions of background map
map_width = len(map_key[0]) * images['g'].get_width()
map_height = len(map_key) * images['g'].get_height()

# Create background map surface
background_map = pygame.Surface((map_width, map_height))

# Blit images onto background map surface based on map key
for y in range(len(map_key)):
    for x in range(len(map_key[y])):
        background_map.blit(images[map_key[y][x]], (x * images['g'].get_width(), y * images['g'].get_height()))

# Define scroll offset and scrolling speed
scroll_offset_x = 0
scroll_offset_y = 0
scroll_speed = 64

# Blit background map onto screen surface
screen.blit(background_map, (scroll_offset_x, scroll_offset_y))

# Update display
pygame.display.update()

# Wait for user to close window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Handle arrow key events
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                scroll_offset_x += scroll_speed
            elif event.key == pygame.K_RIGHT:
                scroll_offset_x -= scroll_speed
            elif event.key == pygame.K_UP:
                scroll_offset_y += scroll_speed
            elif event.key == pygame.K_DOWN:
                scroll_offset_y -= scroll_speed

            # Redraw background map with new scroll offset
            screen.blit(background_map, (scroll_offset_x, scroll_offset_y))

            # Update display
            pygame.display.update()