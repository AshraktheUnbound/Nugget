import pygame

# Initialize Pygame
# Set the game window dimensions
# Create the game window
# Set the game window caption

pygame.init()
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('To the Man Who Sold the World')

# Load the music files and start background music
pygame.mixer.music.load('1982.mp3')
click = pygame.mixer.Sound("click.wav")
#pygame.mixer.music.play()

# Load the JPEG image
# Scale the image to fit the window
bg_image = pygame.image.load("world3.jpg")
bg_image = pygame.transform.scale(bg_image, (window_width, window_height))



# Define some colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set the game clock
clock = pygame.time.Clock()

# Define the menu items
menu_items = [
    {'text': 'New Game', 'position': (window_width // 2, window_height // 4),'action': pygame.display.toggle_fullscreen},
    {'text': 'Load Save', 'position': (window_width // 2, window_height // 2),'action': None},
    {'text': 'Exit', 'position': (window_width // 2, 3 * window_height // 4),'action': None}
]

# Define the menu font
menu_font = pygame.font.Font(None, 36)

# Start the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for item in menu_items:
                if item['rect'].collidepoint(event.pos):
                    print(item['text'])
                    # Play sound file
                    click.play()
                    pygame.time.wait(int(click.get_length() * 1000))
                    item['action']()

    # Draw the menu items
    window.fill(black)
    # Blit the image onto the window surface
    window.blit(bg_image, (0, 0))
    for item in menu_items:
        item_text = menu_font.render(item['text'], True, white)
        item_rect = item_text.get_rect()
        item_rect.center = item['position']
        item['rect'] = item_rect
        pygame.draw.rect(window, red, item_rect, 2)
        window.blit(item_text, item_rect)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()