import pygame

from weapons import cls_bullet, cls_weapon
from locks import cls_locks

class cls_player:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.jump_power = 64 / 4
        self.is_jumping = False
        self.weapon = []
        self.weapon_facing_right = True
        self.player_facing_right = True
        self.kills = 0
        self.hit_points = 3

    def update(self, screen_mode, enemies):
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

        if (keys[pygame.K_c] or keys[pygame.K_i]):
            screen_mode = 2



        # handle player jumping
        if self.is_jumping:
            self.rect.y += self.vel_y
            self.vel_y += 1
            if self.rect.bottom >= 900:
                self.rect.bottom = 900
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
