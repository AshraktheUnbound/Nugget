import pygame

def load_image(file_name, size):
    image = pygame.image.load(file_name).convert()
    transparent_color = (255, 255, 255)
    image.set_colorkey(transparent_color)
    image = pygame.transform.scale(image, (size[0], size[1]))
    return image