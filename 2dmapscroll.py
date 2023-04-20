import pygame
from tiles import load_tiles, load_textfile, split_lines, save_map

key_list = 'wgsther0123456789x'

class cls_settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.tile_size = 64
        self.scroll_offset_x = 0
        self.scroll_offset_y = 0
        self.scroll_speed = 64

settings = cls_settings()
# initialize pygame Set screen dimensions and Create screen surface
pygame.init()
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
clock = pygame.time.Clock()

# tiles.py
# Loads tile images for background and then defines the map using a 2d list of keys
images = load_tiles()
map = 'resources/map.txt'
map_key = split_lines(load_textfile(map))
map_txt = load_textfile(map)

# Calculate dimensions of background map (Map width and length in tiles*64)
# Create background map surface
# Blit images onto background map surface based on map key
map_width = len(map_key[0]) * settings.tile_size
map_height = len(map_key) * settings.tile_size
background_map = pygame.Surface((map_width, map_height))
for y in range(len(map_key)):
    for x in range(len(map_key[y])):
        background_map.blit(images[map_key[y][x]], (x * settings.tile_size, y * settings.tile_size))

# Blit background map onto screen surface
# Update display
screen.blit(background_map, (settings.scroll_offset_x, settings.scroll_offset_y))
pygame.display.update()

# Wait for user to close window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_map(map_txt, 'map.txt')
            pygame.quit()
            exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:  # left mouse button
                pos = pygame.mouse.get_pos()
                for row in range(len(map_key)):
                    for col in range(len(map_key[row])):
                        tile_rect = pygame.Rect(col * 64, row * 64, 64, 64)
                        if tile_rect.collidepoint(pos):
                            for x in range(0,len(key_list)):
                                if key_list[x] == map_txt[row+abs(int(settings.scroll_offset_x/64))][col+abs(int(settings.scroll_offset_y/64))]:
                                    print(row,col)
                                    print(key_list[x], ",", key_list[x-1])
                                    print('Offset X:{}, Offset Y:{} X: {}'.format(settings.scroll_offset_x, settings.scroll_offset_y,x))
                                    print(row+abs(int(settings.scroll_offset_x/64)),col+abs(int(settings.scroll_offset_y/64)))
                                    map_txt[row+abs(int(settings.scroll_offset_y/64))] = map_txt[row+abs(int(settings.scroll_offset_y/64))][:col] + key_list[x - 1] + map_txt[row+abs(int(settings.scroll_offset_y/64))][col + 1:]


        # Handle arrow key events
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                settings.scroll_offset_x += settings.scroll_speed
            elif event.key == pygame.K_RIGHT:
                settings.scroll_offset_x -= settings.scroll_speed
            elif event.key == pygame.K_UP:
                settings.scroll_offset_y += settings.scroll_speed
            elif event.key == pygame.K_DOWN:
                settings.scroll_offset_y -= settings.scroll_speed

            elif event.key == pygame.K_a:
                settings.scroll_offset_x += settings.scroll_speed
            elif event.key == pygame.K_d:
                settings.scroll_offset_x -= settings.scroll_speed
            elif event.key == pygame.K_w:
                settings.scroll_offset_y += settings.scroll_speed
            elif event.key == pygame.K_s:
                settings.scroll_offset_y -= settings.scroll_speed

            # Redraw background map with new scroll offset
            screen.blit(background_map, (settings.scroll_offset_x, settings.scroll_offset_y))

            # Update display

    map_key = split_lines(map_txt)
    for y in range(len(map_key)):
        for x in range(len(map_key[y])):
            background_map.blit(images[map_key[y][x]], (x * settings.tile_size, y * settings.tile_size))
    screen.blit(background_map, (settings.scroll_offset_x, settings.scroll_offset_y))
    clock.tick(60)
    pygame.display.update()


