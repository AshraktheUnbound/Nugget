import glob, os, pygame, random
path = r"C:\Users\Bob Boberson\downloads\nameless\basic\test1\\"

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


    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Round Robin Contest")
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()

    #tiles = pygame.image.load('resources/tiles/' + tile_name + '.png')



    # Load the images
    images = []

    total = len(get_results())

    for x in range(1, total + 1):
        image = pygame.image.load(path + f"{x}.jpg")
        image = pygame.transform.scale(image, (256, 256))
        images.append(image)



    votes = []
    for row in range(len(images)):
        new_row = []
        for col in range(len(images)):
            new_row.append(0)
        votes.append(new_row)

    contestant_a = 0
    contestant_b = 1

    # Main game loop
    running = True
    while running:
        # Display the images

        if contestant_b < total:
            screen.blit(images[contestant_a], (0, 0))
            screen.blit(images[contestant_b], (screen_width // 2, 0))
        else:
            running=False
        # Update the display
        pygame.display.flip()
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get the position of the mouse click
                pos = pygame.mouse.get_pos()
                # Check which image was clicked on
                if pos[0] < screen_width // 2:
                    # Left image was clicked
                    votes[contestant_a][contestant_b] += 1
                else:
                    # Right image was clicked
                    votes[contestant_b][contestant_a] += 1

                contestant_b += 1

                if contestant_b > total - 1:
                    contestant_a += 1
                    contestant_b = contestant_a + 1

        # Tick the clock
        clock.tick(60)

    # Print the final results
    print("Results:")
    count = 0
    for row in votes:
        sum = 0
        count += 1
        for number in row:
            sum += number
        print(f'Row #: {count},Total: {sum} ')

cleanse()
contest()