import pygame


# initialize pygame Set screen dimensions and Create screen surface
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Load PNG images and store them in a dictionary based on map key
images = {}
images['g'] = pygame.image.load("resources/tiles/bg_grass.png")
images['t'] = pygame.image.load("resources/tiles/bg_tree.png")
images['w'] = pygame.image.load("resources/tiles/bg_water.png")
images['s'] = pygame.image.load("resources/tiles/bg_sand.png")
images['p'] = pygame.image.load("resources/tiles/bg_pavement.png")
images['h'] = pygame.image.load("resources/tiles/bg_house.png")
images['e'] = pygame.image.load("resources/tiles/bg_teepee.png")
images['r'] = pygame.image.load("resources/tiles/bg_grock.png")

images['0'] = pygame.image.load("resources/tiles/bg_road_lr.png")
images['1'] = pygame.image.load("resources/tiles/bg_road_ud.png")
images['2'] = pygame.image.load("resources/tiles/bg_road_dr.png")
images['3'] = pygame.image.load("resources/tiles/bg_road_dl.png")
images['4'] = pygame.image.load("resources/tiles/bg_road_lu.png")
images['5'] = pygame.image.load("resources/tiles/bg_road_ur.png")

images['6'] = pygame.image.load("resources/tiles/bg_troad_u.png")
images['7'] = pygame.image.load("resources/tiles/bg_troad_d.png")
images['8'] = pygame.image.load("resources/tiles/bg_troad_l.png")
images['9'] = pygame.image.load("resources/tiles/bg_troad_r.png")

images['x'] = pygame.image.load("resources/tiles/bg_xroad.png")
# ... add more images and keys as needed

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