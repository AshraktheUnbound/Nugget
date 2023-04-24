import pygame
from random import randint as rand
from player import cls_player
from weapons import cls_weapon
from enemies import cls_enemy, cls_super_enemy

def load_music():
    pygame.mixer.music.load('7000RPM.mp3')
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
    return enemy

def load_enemies(images,WINDOW_WIDTH, WINDOW_HEIGHT):
    enemies = []

    for x in range(8):
        enemies.append(generate_enemy(cls_enemy, images.enemy_image,WINDOW_WIDTH, WINDOW_HEIGHT))

    for x in range(3):
        enemy = generate_enemy(cls_super_enemy, images.big_enemy_image,WINDOW_WIDTH, WINDOW_HEIGHT)
        enemy.child = images.enemy_image
        enemies.append(enemy)

    return enemies

def load_flowers(images,WINDOW_WIDTH, WINDOW_HEIGHT):
    flowers = []
    for x in range(10):
        flower_x = rand(0, WINDOW_WIDTH - 64)
        flower_y = rand(0, WINDOW_HEIGHT - 64)
        flower = cls_flower(flower_x, flower_y, images.flower_image)
        flowers.append(flower)
    for x in range(250):
        grass_x = rand(0, WINDOW_WIDTH - 64)
        grass_y = rand(0, WINDOW_HEIGHT - 64)
        grass = cls_flower(grass_x, grass_y, images.grass_image)
        flowers.append(grass)

    return flowers

class load_images():
    def __init__(self):
        self.bullet_image = load_image('bullet.png', (16, 16))
        self.weapon_image = load_image('weapon.png', (48, 24))
        self.player_image = load_image('char.jpg', (64, 64))
        self.player_image = pygame.transform.flip(self.player_image, True, False)
        self.enemy_image = load_image('enemy.png', (48, 48))
        self.flower_image = load_image('flower.jpg', (40, 40))
        self.grass_image = load_image('grass.png', (16, 16))
        self.big_enemy_image = load_image('enemy_2.png', (100, 100))

class cls_flower:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        '''
        image = pygame.image.load('pyramid.png')
        image = pygame.transform.scale(image, (WINDOW_WIDTH, WINDOW_HEIGHT))
        alpha = 0
        running = True
        while running:
            alpha += .5
            if alpha > 255:
                alpha = 255
            image.set_alpha(alpha)
            game_window.blit(image, (0, 0))
            pygame.display.update()
            clock.tick(60)
            if alpha == 255:
                running = False'''