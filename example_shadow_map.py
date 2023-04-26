import pygame
import numpy as np

pygame.init()
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# create the shadow map texture
shadow_map_size = 500
shadow_map = pygame.Surface((shadow_map_size, shadow_map_size), pygame.SRCALPHA)

# create a white pixel
white = (255, 255, 255)
pixel_size = 5
pixel = pygame.Surface((pixel_size, pixel_size))
pixel.fill(white)

# light source position and color
light_pos = np.array([100, 100])
light_color = np.array([255, 255, 255])

# grass position and color
grass_pos = np.array([125, 125])
grass_color = np.array([0, 255, 0])

# render the scene from the perspective of the light source and store the depth values in the shadow map texture
shadow_map.fill((0, 0, 0, 255))

for y in range(screen_height):
    for x in range(screen_width):
        # compute the distance from the light source to the pixel
        dist = np.linalg.norm(np.array([x, y]) - light_pos)
        # compute the depth value (normalized distance) and store it in the shadow map texture
        depth = dist / np.sqrt(screen_width ** 2 + screen_height ** 2)
        shadow_map.set_at((x, y), (0, 0, 0, int(depth * 255)))

# render the scene from the camera's perspective and apply shadow mapping
for y in range(screen_height):
    for x in range(screen_width):
        # compute the distance from the light source to the pixel
        dist = np.linalg.norm(np.array([x, y]) - light_pos)
        # compute the depth value (normalized distance)
        depth = dist / np.sqrt(screen_width ** 2 + screen_height ** 2)
        # compute the shadow value by comparing the pixel's depth value with the corresponding value in the shadow map texture
        if x < shadow_map_size and y < shadow_map_size:
            shadow = shadow_map.get_at((x, y))[3] / 255
        else:
            shadow = 1
        # compute the final color by blending the light source color and the grass color based on the shadow value
        color = (1 - shadow) * light_color + shadow * grass_color
        # render the pixel
        pixel.fill(color.astype(int))
        screen.blit(pixel, (x, y))

# update the screen
pygame.display.flip()

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# quit pygame
pygame.quit()
