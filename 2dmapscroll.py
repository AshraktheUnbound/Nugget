import pygame
from tiles import load_tiles

# initialize pygame Set screen dimensions and Create screen surface
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

images = load_tiles()

# Define the map using a 2D list of keys
map_key = [
    ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
    ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
    ['w', 'w', 'w', 'w', 'w', 'w', 's', 's', 'w', 'w', 'w', 'w', 'w', 's', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
    ['w', 'w', 'w', 'w', 'w', 's', 'g', 'g', 's', 'w', 'w', 'w', 's', 'g', 's', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
    ['w', 'w', 'w', 'w', 's', 'g', 'g', 'g', 's', 'w', 'w', 's', 'g', 'g', 'g', 's', 's', 's', 's', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
    ['w', 'w', 'w', 'w', 's', 'g', 'h', 'g', 'g', 's', 's', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 's', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
    ['w', 'w', 'w', 's', 's', 'g', '1', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 't', 'g', 'g', 'g', 'g', 'g', 's', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
    ['w', 'w', 'w', 's', 's', 'g', '5', '0', '0', '0', '0', '3', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 's', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
    ['w', 'w', 'w', 's', 'g', 'g', 'g', 'g', 'g', 'g', 'r', '1', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 's', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
    ['w', 'w', 's', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', '1', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 's', 'w', 'w', 'w', 'w', 'w', 'w'],
    ['w', 'w', 's', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', '5', '0', '0', '3', 'g', 'g', 'g', 't', 'g', 'g', 'g', 'g', 'g', 's', 'w', 'w', 'w', 'w', 'w'],
    ['w', 'w', 'w', 's', 's', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', '1', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 's', 'w', 'w', 'w', 'w', 'w'],
    ['w', 'w', 'w', 'w', 's', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', '1', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 's', 'w', 'w', 'w', 'w'],
    ['w', 'w', 'w', 'w', 's', 'g', 't', 'g', 'g', 'g', 'g', 'g', 'g', 'g', '1', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 's', 'w', 'w', 'w', 'w'],
    ['w', 'w', 'w', 's', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', '1', 'g', 'g', 'g', 'g', 'g', 'g', 't', 'g', 'g', 'g', 's', 'w', 'w', 'w', 'w'],
    ['w', 'w', 'w', 's', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'e', 'g', 'g', '1', 'r', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 's', 'w', 'w', 'w'],
    ['w', 'w', 'w', 'w', 's', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', '5', '0', '0', '0', '0', '0', '0', '3', 'g', 'g', 'g', 'g', 's', 'w', 'w', 'w'],
    ['w', 'w', 'w', 'w', 'w', 's', 'g', 'g', 'g', 'g', 'g', 'w', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', '1', 'g', 'h', 'g', 'g', 's', 'w', 'w', 'w'],
    ['w', 'w', 'w', 'w', 'w', 's', 'g', 'g', 'g', 't', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 't', 'g', 'g', '1', 'g', '1', 'g', 'g', 's', 'w', 'w', 'w'],
    ['w', 'w', 'w', 'w', 'w', 's', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', '5', '0', '4', 'g', 's', 'w', 'w', 'w', 'w'],
    ['w', 'w', 'w', 'w', 'w', 'w', 's', 'g', 't', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 's', 's', 's', 'w', 'w', 'w', 'w', 'w'],
    ['w', 'w', 'w', 'w', 'w', 'w', 's', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 's', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
    ['w', 'w', 'w', 'w', 'w', 'w', 'w', 's', 'g', 'g', 'g', 'g', 's', 'g', 'g', 'g', 'g', 'g', 'g', 's', 's', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
    ['w', 'w', 's', 's', 'w', 'w', 'w', 'w', 's', 'g', 'g', 's', 'w', 's', 'g', 'g', 'r', 'g', 's', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
    ['w', 'w', 's', 's', 'w', 'w', 'w', 'w', 'w', 's', 's', 'w', 'w', 'w', 's', 'g', 'g', 'g', 's', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
    ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 's', 'g', 'g', 's', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
    ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 's', 's', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
    ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
    ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
    ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
]

# Calculate dimensions of background map
# Create background map surface
# Blit images onto background map surface based on map key
map_width = len(map_key[0]) * images['g'].get_width()
map_height = len(map_key) * images['g'].get_height()
background_map = pygame.Surface((map_width, map_height))
for y in range(len(map_key)):
    for x in range(len(map_key[y])):
        background_map.blit(images[map_key[y][x]], (x * images['g'].get_width(), y * images['g'].get_height()))

# Define scroll offset and scrolling speed
# Blit background map onto screen surface
# Update display
scroll_offset_x = 0
scroll_offset_y = 0
scroll_speed = 64
screen.blit(background_map, (scroll_offset_x, scroll_offset_y))
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