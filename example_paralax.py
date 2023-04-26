import pygame
import random

# initialize pygame
pygame.init()

# set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Parallax Background")

# set up the clock
clock = pygame.time.Clock()

# load background images
bg1 = pygame.image.load("bg1.png").convert()
bg2 = pygame.image.load("bg2.png").convert()
bg3 = pygame.image.load("bg3.png").convert()

# set up variables for scrolling and parallax effect
scroll_speed = 5
parallax_speeds = [3, 2, 1]
parallax_offsets = [0, 0, 0]

# set up game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # scroll the backgrounds
    for i in range(3):
        parallax_offsets[i] += parallax_speeds[i]
        if parallax_offsets[i] > bg1.get_width():
            parallax_offsets[i] = 0

    # draw the backgrounds with parallax effect
    screen.blit(bg3, (-parallax_offsets[2], 0))
    screen.blit(bg2, (-parallax_offsets[1], 0))
    screen.blit(bg1, (-parallax_offsets[0], 0))

    # update the display
    pygame.display.update()

    # limit the frame rate
    clock.tick(60)

# quit pygame
pygame.quit()