import glob, os
path = r"C:\Users\Bob Boberson\downloads\nameless\basic\\"

def get_results():
    pattern = path + "*.jpg"
    return glob.glob(pattern)


def cleanse():
    result = get_results()

    # Iterating the list with the count
    count = 1
    for file_name in result:
        old_name = file_name
        new_name = path + str(count) + ".jpg"
        os.rename(old_name, new_name)
        count = count + 1
    print('File Cleansing is complete'.format())

def contest():
    screen_width = 800
    screen_height = 600
    row = 1
    col = 1

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))


    tiles = pygame.image.load('resources/tiles/' + tile_name + '.png')

    for row in range(len(map_key)):
        for col in range(len(map_key[row])):

#cleanse()
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the window
WIDTH = 800
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Round Robin Contest")

# Load the images
images = []
for i in range(1, 81):
    image = pygame.image.load(f"{i}.jpg")
    images.append(image)

# Create a dictionary to keep track of votes
votes = {}
for i in range(1, 81):
    votes[i] = 0

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the clock
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the position of the mouse click
            pos = pygame.mouse.get_pos()
            # Check which image was clicked on
            if pos[0] < WIDTH // 2:
                # Left image was clicked
                votes[current_images[0]] += 1
            else:
                # Right image was clicked
                votes[current_images[1]] += 1

    # Choose two random images
    current_images = random.sample(range(1, 81), 2)

    # Display the images
    SCREEN.blit(images[current_images[0] - 1], (0, 0))
    SCREEN.blit(images[current_images[1] - 1], (WIDTH // 2, 0))

    # Display the vote count
    vote_text = font.render(f"Votes: {sum(votes.values())}", True, (255, 255, 255))
    SCREEN.blit(vote_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Tick the clock
    clock.tick(60)

# Print the final results
print("Results:")
for i in range(1, 81):
    print(f"{i}: {votes[i]} votes")