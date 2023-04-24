import pygame, time
from random import randint as rand
from enemies import cls_enemy, cls_super_enemy

def load_image(file_name, size):
        image = pygame.image.load(file_name).convert()
        transparent_color = (255, 255, 255)
        image.set_colorkey(transparent_color)
        image = pygame.transform.scale(image, (size[0], size[1]))
        return image

class cls_bullet:
    def __init__(self, x, y, direction):
        self.image = bullet_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = .05
        self.direction = direction

    def update(self):
        pass

class cls_weapon:
    def __init__(self, x, y, capacity):
        self.image = weapon_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.bullets = []
        self.fire_sound = pygame.mixer.Sound("fire_sound.wav")
        self.capacity = capacity
        self.ammo_count = capacity
        self.ammo_total = self.capacity * 3


    def update(self, player_rect):
        self.rect.centerx = player_rect.centerx
        self.rect.bottom = player_rect.top+48

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def shoot(self, direction):
        if self.ammo_count == 0:
            self.reload()
        else:
            bullet = cls_bullet(self.rect.centerx, self.rect.top, direction)
            self.bullets.append(bullet)
            self.fire_sound.play()
            self.ammo_count -= 1

    def reload(self):
        if self.capacity < self.ammo_total:
            self.ammo_count = self.capacity
            self.ammo_total -= self.capacity
        else:
            self.ammo_count = self.ammo_total
            self.ammo_total = 0

class cls_player:
    def __init__(self, x, y):
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.jump_power = TILE_SIZE / 4
        self.is_jumping = False
        self.weapon = cls_weapon(self.rect.centerx, self.rect.top, 15)
        self.weapon_facing_right = True
        self.player_facing_right = True
        self.kills = 0
        self.hit_points = 3

    def update(self):
        # handle player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.is_jumping = True
            self.vel_y = -self.jump_power
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= 5
            if self.weapon_facing_right == True:
                self.weapon.image = pygame.transform.flip(self.weapon.image, True, False)
                self.image = pygame.transform.flip(self.image, True, False)
                self.weapon_facing_right = not self.weapon_facing_right
                self.player_facing_right = not self.player_facing_right
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += 5
            if self.weapon_facing_right == False:
                self.weapon.image = pygame.transform.flip(self.weapon.image, True, False)
                self.image = pygame.transform.flip(self.image, True, False)
                self.weapon_facing_right = not self.weapon_facing_right
                self.player_facing_right = not self.player_facing_right
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += 5

        # handle player jumping
        if self.is_jumping:
            self.rect.y += self.vel_y
            self.vel_y += 1
            if self.rect.bottom >= WINDOW_HEIGHT:
                self.rect.bottom = WINDOW_HEIGHT
                self.is_jumping = False

        # check for collisions
        for enemy in enemies:
            if self.rect.colliderect(enemy):
                if self.vel_y > 0:
                    self.rect.bottom = enemy.top
                    self.is_jumping = False
                    self.vel_y = 0
                elif self.vel_y < 0:
                    self.rect.top = enemy.bottom
                    self.vel_y = 0
        self.weapon.update(self.rect)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        self.weapon.draw(surface)

class cls_flower:
    def __init__(self, x, y):
        self.image = flower_image
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

#pygame.mixer.music.load('7000RPM.mp3')
#pygame.mixer.music.play()

bullet_image = load_image('bullet.png', (16,16))
weapon_image = load_image('weapon.png', (48,24))
player_image = load_image('char.jpg', (64,64))
player_image = pygame.transform.flip(player_image, True, False)
enemy_image = load_image('enemy.png', (48,48))
flower_image = load_image('flower.jpg', (40,40))
big_enemy_image = load_image('enemy_2.png', (100,100))

player = cls_player(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

enemies = []

def generate_enemy(class_used, image):
    x = rand(0, WINDOW_WIDTH - TILE_SIZE)
    y = rand(0, WINDOW_HEIGHT - TILE_SIZE)
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
    flower = cls_flower(flower_x, flower_y)
    flowers.append(flower)


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
    player.update()

    for flower in flowers:
        game_window.blit(flower.image, flower.rect)

    for enemy in enemies:
        enemy.update(player)
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

