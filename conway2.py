import pygame
import numpy as np

# Define the size of the grid
width, height = 640, 480
cell_size = 10

# Initialize the pygame module
pygame.init()

# Create the game window
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Conway's Game of Life")

# Create a numpy array to represent the grid
grid = np.zeros((height // cell_size, width // cell_size), dtype=np.uint8)

# Define the starting structure
grid[5:8, 5:8] = 1
grid[6, 6] = 0


# Define the rules of the game
def evolve(grid):
    # Create a new grid to hold the next state
    new_grid = np.zeros_like(grid)

    # Iterate over each cell in the grid
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            # Count the number of live neighbors
            num_neighbors = np.sum(grid[max(0, i - 1):min(grid.shape[0], i + 2),
                                   max(0, j - 1):min(grid.shape[1], j + 2)]) - grid[i, j]

            # Apply the rules of the game
            if grid[i, j] == 1 and (num_neighbors == 2 or num_neighbors == 3):
                new_grid[i, j] = 1
            elif grid[i, j] == 0 and num_neighbors == 3:
                new_grid[i, j] = 1

    # Return the new grid
    return new_grid


# Define the main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the grid
    grid = evolve(grid)

    # Clear the window
    window.fill((255, 255, 255))

    # Draw the cells
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == 1:
                pygame.draw.rect(window, (0, 0, 0), (j * cell_size, i * cell_size, cell_size, cell_size))

    # Update the display
    pygame.display.flip()

# Clean up the pygame module
pygame.quit()