import pygame, time
from random import randint as rand
from enemies import cls_enemy, cls_super_enemy
from player import cls_player
from weapons import cls_weapon, cls_bullet
from images import load_image



class cls_flower:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# initialize pygame
pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Nugget')
TILE_SIZE = 64
menu_font = pygame.font.Font(None, 36)

pygame.mixer.music.load('7000RPM.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()

weapon_image = load_image('weapon.png', (48,24))
player_image = load_image('char.jpg', (64,64))
player_image = pygame.transform.flip(player_image, True, False)
enemy_image = load_image('enemy.png', (48,48))
flower_image = load_image('flower.jpg', (40,40))
grass_image = load_image('grass.png', (16,16))
big_enemy_image = load_image('enemy_2.png', (100,100))

player = cls_player(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, player_image)
weapon = cls_weapon(player.rect.centerx, player.rect.top, 15, weapon_image)
player.weapon = weapon

enemies = []

def generate_enemy(class_used, image):
    x = rand(0, WINDOW_WIDTH - 64)
    y = rand(0, WINDOW_HEIGHT - 64)
    enemy = class_used(image, x, y)
    return enemy

for x in range(2):
    enemies.append(generate_enemy(cls_enemy, enemy_image))

for x in range(1):
    enemy = generate_enemy(cls_super_enemy, big_enemy_image)
    enemy.child = enemy_image
    enemies.append(enemy)

flowers = []
for x in range(10):
    flower_x = rand(0, WINDOW_WIDTH - TILE_SIZE)
    flower_y = rand(0, WINDOW_HEIGHT - TILE_SIZE)
    flower = cls_flower(flower_x, flower_y, flower_image)
    flowers.append(flower)
for x in range(250):
    grass_x = rand(0, WINDOW_WIDTH - TILE_SIZE)
    grass_y = rand(0, WINDOW_HEIGHT - TILE_SIZE)
    grass = cls_flower(grass_x, grass_y, grass_image)
    flowers.append(grass)


clock = pygame.time.Clock()
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0]:  # left mouse button
                direction = (mouse_pos[0] - player.rect.centerx, mouse_pos[1] - player.rect.centery)
                player.weapon.shoot(direction)
            elif pygame.mouse.get_pressed()[2]:  # left mouse button
                player.weapon.reload()

    # draw game world
    game_window.fill((0, 0, 0))
    player.update(enemies)

    for flower in flowers:
        game_window.blit(flower.image, flower.rect)

    for enemy in enemies:
        enemy.update(player, enemies)
        game_window.blit(enemy.image, enemy.rect)

        if player.rect.colliderect(enemy):
            print('Collision!')
            player.hit_points += -1

            enemy.death_sound.play()
            enemies.remove(enemy)
            player.kills += 1

            enemy_x = rand(0, WINDOW_WIDTH - TILE_SIZE)
            enemy_y = rand(0, WINDOW_HEIGHT - TILE_SIZE)
            enemy = cls_enemy(enemy_image, enemy_x, enemy_y)
            enemies.append(enemy)

            if player.hit_points < 1:
                running = False

        for bullet in player.weapon.bullets:
            if bullet.rect.colliderect(enemy):
                player.weapon.bullets.remove(bullet)
                #enemy.death_sound.play()
                enemies.remove(enemy)
                player.kills += 1

                if rand(1,2) > 1:
                    enemy_x = rand(0, WINDOW_WIDTH - TILE_SIZE)
                    enemy_y = rand(0, WINDOW_HEIGHT - TILE_SIZE)
                    enemy = cls_enemy(enemy_image, enemy_x, enemy_y)
                    enemies.append(enemy)

    for bullet in player.weapon.bullets:
        bullet.rect.x += bullet.speed * bullet.direction[0]
        bullet.rect.y += bullet.speed * bullet.direction[1]
        if bullet.rect.left > WINDOW_WIDTH or bullet.rect.right < 0 or bullet.rect.top > WINDOW_HEIGHT or bullet.rect.bottom < 0:
            player.weapon.bullets.remove(bullet)
        else:
            game_window.blit(bullet.image, bullet.rect)

    player.draw(game_window)

    item_text = menu_font.render(f'KILLS: {player.kills} - HITPOITS: {player.hit_points} - AMMO:({player.weapon.ammo_count}/{player.weapon.ammo_total})', True, (255,255,255))
    item_rect = item_text.get_rect()
    game_window.blit(item_text, item_rect)
    # update game window
    pygame.display.update()

    # set frame rate
    clock.tick(60)

# quit game
pygame.quit()

