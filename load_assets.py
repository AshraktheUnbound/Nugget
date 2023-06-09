import pygame
from random import randint as rand
from player import cls_player
from weapons import cls_weapon
from enemies import cls_enemy, cls_super_enemy

def load_music():
    pygame.mixer.music.load('resources/7000RPM.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()

def load_image(file_name, size):
    image = pygame.image.load(file_name).convert()
    transparent_color = (255, 255, 255)
    image.set_colorkey(transparent_color)
    image = pygame.transform.scale(image, (size[0], size[1]))
    return image

def load_player(x, y, images):
    player = cls_player(x,y, images.player_image)
    weapon = cls_weapon(player.rect.centerx, player.rect.top, 15, images.weapon_image, images.bullet_image)
    player.weapon = weapon
    return player

def generate_enemy(class_used, image,WINDOW_WIDTH, WINDOW_HEIGHT):
    x = rand(0, WINDOW_WIDTH - 64)
    y = rand(0, WINDOW_HEIGHT - 64)
    enemy = class_used(image, x, y)
    enemy.loot = cls_ammo
    enemy.loot_image = []
    return enemy

def load_enemies(images,WINDOW_WIDTH, WINDOW_HEIGHT):
    enemies = []

    for x in range(1):
        enemies.append(generate_enemy(cls_enemy, images.enemy_image,WINDOW_WIDTH, WINDOW_HEIGHT))

    for x in range(1):
        enemy = generate_enemy(cls_super_enemy, images.big_enemy_image,WINDOW_WIDTH, WINDOW_HEIGHT)
        enemy.child = images.enemy_image
        enemies.append(enemy)

    return enemies

def load_flowers(images,WINDOW_WIDTH, WINDOW_HEIGHT):
    flowers = []
    for x in range(10):
        flower_x = rand(0, WINDOW_WIDTH - 64)
        flower_y = rand(0, WINDOW_HEIGHT - 64)
        flower = cls_map_object(flower_x, flower_y, images.flower_image)
        flowers.append(flower)
    for x in range(500):
        grass_x = rand(0, WINDOW_WIDTH - 64)
        grass_y = rand(0, WINDOW_HEIGHT - 64)
        choice = rand(0,3)
        grass = cls_map_object(grass_x, grass_y, images.grass_images[choice])
        flowers.append(grass)
    for x in range(1):
        puddle_x = rand(0, WINDOW_WIDTH - 512)
        puddle_y = rand(0, WINDOW_HEIGHT - 512)
        puddle = cls_map_object(puddle_x, puddle_y, images.puddle_image)
        flowers.append(puddle)


    return flowers

def load_buildings(images, WINDOW_WIDTH, WINDOW_HEIGHT):
    buildings = []

    for x in range(1):
        cave_x = rand(0, WINDOW_WIDTH - 512)
        cave_y = rand(0, WINDOW_HEIGHT - 512)
        cave = cls_building(cave_x, cave_y, images.cave_image)
        buildings.append(cave)

    return buildings

class load_images():
    def __init__(self):
        self.bullet_image = load_image('resources/images/bullet.png', (16, 16))
        self.weapon_image = load_image('resources/images/gungun.png', (90, 24))
        self.player_image = load_image('resources/images/char_2.png', (96, 96))
        self.player_image = pygame.transform.flip(self.player_image, True, False)
        self.enemy_image = load_image('resources/images/enemy.png', (48, 48))
        self.flower_image = load_image('resources/images/glow_flower.png', (64,64))
        self.grass_image = load_image('resources/images/grass.png', (16, 16))
        self.big_enemy_image = load_image('resources/images/enemy_2.png', (100, 100))
        #self.ammo_image = load_image('ammo.png', (64, 32))

        #self.grass_images = load_split_image('resources')
        self.grass_images = []
        self.grass_images.append(load_image('resources/images/grass.png', (16, 16)))
        self.grass_images.append(load_image('resources/images/grass_2.png', (16, 16)))
        self.grass_images.append(load_image('resources/images/grass_3.png', (16, 16)))
        self.grass_images.append(load_image('resources/images/grass_4.png', (16, 16)))

        self.puddle_image = load_image('resources/images/tree.png', (256, 382))
        self.cave_image = load_image('resources/images/cave.png', (512, 512))

class cls_map_object:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class cls_building(cls_map_object):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        self.door_rect = pygame.Rect(x+220,y+280,40,40)



class cls_ammo:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def gitty_get(self, player):
        player.weapon.ammo_total += player.weapon.capacity


def load_split_image(filename):
    image = pygame.image.load(filename)

    # Split the image into four 32x32 images
    images = []
    for i in range(4):
        rect = pygame.Rect(i * 32, 0, 32, 32)
        sub_image = image.subsurface(rect)
        images.append(sub_image)

    return images

class cls_map:
    def __init__(self, w, h):
        WIDTH = w
        HEIGHT = h
        self.images = load_images()
        self.player = load_player(WIDTH // 2, HEIGHT // 2, self.images)
        self.enemies = load_enemies(self.images, WIDTH, HEIGHT)
        self.flowers = load_flowers(self.images, WIDTH, HEIGHT)
        self.buildings = load_buildings(self.images, WIDTH, HEIGHT)
