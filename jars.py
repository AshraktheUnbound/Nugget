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