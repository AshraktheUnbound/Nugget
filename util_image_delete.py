import os
import pygame
import shutil

# Set up Pygame
pygame.init()

# Set up the display window
screen_width = 1200
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Image Viewer")

# Set up fonts
font = pygame.font.Font(None, 40)

# Set up colors
white = (255, 255, 255)
black = (0, 155, 255)
red = (255, 0, 0)

# Set up directories
image_dir = r"C:/Users/danie/Downloads/image//"
trash_dir = r"C:/Users/danie/Downloads/image/trash//"

# Load images from the image directory
images = []
for filename in os.listdir(image_dir):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        image_path = os.path.join(image_dir, filename)
        image = pygame.image.load(image_path)
        images.append(image)

# Set up variables
current_image_index = 0
num_images = len(images)
keep_button_rect = pygame.Rect(screen_width / 2 - 200, screen_height - 100, 150, 50)
delete_button_rect = pygame.Rect(screen_width / 2 + 50, screen_height - 100, 150, 50)

# Main loop
while True:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if keep_button_rect.collidepoint(mouse_pos):

                # Show the next image
                current_image_index += 1
                if current_image_index >= num_images:
                    pygame.quit()
                    quit()
            elif delete_button_rect.collidepoint(mouse_pos):
                # Move the image to the "Trash" directory
                if current_image_index >= num_images:
                    pygame.quit()
                    quit()
                current_image_path = os.path.join(image_dir, os.listdir(image_dir)[current_image_index])
                shutil.move(current_image_path, trash_dir)
                # Show the next image
                current_image_index += 1
                if current_image_index >= num_images:
                    pygame.quit()
                    quit()

    # Show the current image
    current_image = images[current_image_index]
    #current_image = pygame.transform.scale(current_image, (screen_width*.75, screen_height*.75))
    current_image = pygame.transform.scale(current_image, (256, 256))
    screen.fill(white)
    screen.blit(current_image,
                (screen_width / 2 - current_image.get_width() / 2, screen_height / 2 - current_image.get_height() / 2))

    # Draw the buttons
    pygame.draw.rect(screen, black, keep_button_rect, 2)
    pygame.draw.rect(screen, black, delete_button_rect, 2)
    keep_button_text = font.render("Keep", True, black)
    delete_button_text = font.render("Delete", True, black)
    screen.blit(keep_button_text, (keep_button_rect.x + keep_button_rect.width / 2 - keep_button_text.get_width() / 2,
                                   keep_button_rect.y + keep_button_rect.height / 2 - keep_button_text.get_height() / 2))
    screen.blit(delete_button_text, (
    delete_button_rect.x + delete_button_rect.width / 2 - delete_button_text.get_width() / 2,
    delete_button_rect.y + delete_button_rect.height / 2 - delete_button_text.get_height() / 2))

    pygame.display.update()
