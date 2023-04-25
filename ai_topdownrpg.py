import pygame, time
from random import randint as rand
from enemies import cls_enemy
from load_assets import load_music, load_images, load_player, load_enemies
from load_assets import load_flowers

window_modes = {'Windowed':1, 'Full Screen':2}
window_mode = 2
pygame.init()
if window_mode == 1:
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
elif window_mode == 2:
    WINDOW_WIDTH = pygame.display.Info().current_w
    WINDOW_HEIGHT = pygame.display.Info().current_h
    game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption('Nugget')
clock = pygame.time.Clock()
menu_font = pygame.font.Font(None, 72)
load_music()
#TILE_SIZE = 64

images = load_images()
player = load_player(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2,images)
enemies = load_enemies(images, WINDOW_WIDTH, WINDOW_HEIGHT)
flowers = load_flowers(images, WINDOW_WIDTH, WINDOW_HEIGHT)

mouse_down = False

running = True
while running:
    # INPUTS - HANDLE EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:  # left mouse button
                mouse_down = True
            elif pygame.mouse.get_pressed()[2]:  # right mouse button
                player.weapon.reload()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # left mouse button
                mouse_down = False
    if mouse_down:
        mouse_pos = pygame.mouse.get_pos()
        direction = (mouse_pos[0] - player.rect.centerx, mouse_pos[1] - player.rect.centery)
        player.weapon.shoot(direction)

    #Movement Logic
    player.update(enemies)
    for enemy in enemies:
        enemy.update(player, enemies)
    for bullet in player.weapon.bullets:
        bullet.rect.x += bullet.speed * bullet.direction[0]
        bullet.rect.y += bullet.speed * bullet.direction[1]

    # Collision Logic
    for enemy in enemies:
        if player.rect.colliderect(enemy):
            print('Collision!')
            player.hit_points += -1

            enemy.death_sound.play()
            enemies.remove(enemy)
            player.kills += 1

            enemy_x = rand(0, WINDOW_WIDTH - 64)
            enemy_y = rand(0, WINDOW_HEIGHT - 64)
            enemy = cls_enemy(images.enemy_image, enemy_x, enemy_y)
            enemies.append(enemy)

    for bullet in player.weapon.bullets:
        for enemy in enemies:
            if bullet.rect.colliderect(enemy):
                player.weapon.bullets.remove(bullet)
                enemies.remove(enemy)
                player.kills += 1

                if rand(1,2) > 1:
                    enemy_x = rand(0, WINDOW_WIDTH - 64)
                    enemy_y = rand(0, WINDOW_HEIGHT - 64)
                    enemy = cls_enemy(images.enemy_image, enemy_x, enemy_y)
                    enemies.append(enemy)

    # DRAW THE FRAME AFTER ALL LOGIC
    game_window.fill((0, 0, 0))

    for flower in flowers:
        game_window.blit(flower.image, flower.rect)
    for enemy in enemies:
        game_window.blit(enemy.image, enemy.rect)
    player.draw(game_window)
    for bullet in player.weapon.bullets:
        if bullet.rect.left > WINDOW_WIDTH or bullet.rect.right < 0 or bullet.rect.top > WINDOW_HEIGHT or bullet.rect.bottom < 0:
            player.weapon.bullets.remove(bullet)
        else:
            game_window.blit(bullet.image, bullet.rect)

    item_text = menu_font.render(f'KILLS: {player.kills} - HITPOITS: {player.hit_points} - AMMO:({player.weapon.ammo_count}/{player.weapon.ammo_total})', True, (255,255,255))
    item_rect = item_text.get_rect()
    game_window.blit(item_text, item_rect)
    pygame.display.update()

    # Frame Rate
    clock.tick(60)

    # End Game Conditions - DEAD or NO ENEMIES
    if len(enemies) == 0 or player.hit_points < 1:
        running = False

pygame.quit()
print('Thank you for playing.')

