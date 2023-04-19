import pygame

pygame.init()

# Set screen dimensions
screen_width = 800
screen_height = 600

# Create screen surface
screen = pygame.display.set_mode((screen_width, screen_height))

# Load PNG images and store them in a dictionary based on map key
images = {}
images['g'] = pygame.image.load("resources/tiles/bg_grass.png")
images['t'] = pygame.image.load("resources/tiles/bg_tree.png")
images['w'] = pygame.image.load("resources/tiles/bg_water.png")
images['s'] = pygame.image.load("resources/tiles/bg_sand.png")
images['p'] = pygame.image.load("resources/tiles/bg_pavement.png")
images['h'] = pygame.image.load("resources/tiles/bg_house.png")
images['r'] = pygame.image.load("resources/tiles/bg_grock.png")

images['0'] = pygame.image.load("resources/tiles/bg_road_lr.png")
images['1'] = pygame.image.load("resources/tiles/bg_road_ud.png")
images['2'] = pygame.image.load("resources/tiles/bg_road_dr.png")
images['3'] = pygame.image.load("resources/tiles/bg_road_dl.png")
images['4'] = pygame.image.load("resources/tiles/bg_road_lu.png")
images['5'] = pygame.image.load("resources/tiles/bg_road_ur.png")

# ... add more images and keys as needed

# Define the map using a 2D list of keys
map_key = [
    ['g', 'g', '1', 't', 't', 'g', 'g', 's', 'w', 'w', 'w', 'w', 'w'],
    ['g', 'g', '1', 't', 't', 'g', 'g', 's', 'w', 'w', 'w', 'w', 'w'],
    ['g', 'g', '5', '3', 'g', 'g', 'g', 's', 'w', 'w', 'w', 's', 'w'],
    ['g', 't', 't', '1', 'g', 'g', 's', 's', 'w', 'w', 'w', 's', 'w'],
    ['g', 't', 't', '1', 'g', 'g', 's', 'w', 'w', 'w', 'w', 'w', 'w'],
    ['r', 'r', 'g', '1', 'g', 's', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
    ['r', 'r', 'g', '1', 'g', 's', 's', 's', 'w', 'w', 'w', 'w', 'w'],
    ['g', 'h', 'p', '1', 'g', 'r', 'g', 't', 's', 'w', 'w', 'w', 'w'],
    ['t', 'g', 't', '1', 'g', 't', 'g', 'g', 's', 's', 'w', 'w', 'w'],
    ['g', 'g', 'g', '1', 'g', 't', 'g', 'g', 'g', 's', 's', 'w', 'w'],
    ['g', 'g', 'g', '1', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 's', 's'],
    ['g', 't', 'g', '1', 'r', 'g', 'g', 't', 'g', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'g', '1', 'g', 't', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],
    ['p', 'p', 'p', '1', 'g', 'g', 'g', 'g', 's', 's', 'g', 'g', 'g'],
    ['t', 'g', 'g', '1', 't', 'g', 'g', 'g', 's', 's', 'g', 'r', 'g'],
    ['g', 'g', 'g', '1', 'g', 'g', 'g', 's', 's', 's', 'g', 'g', 'g'],
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