import pygame
from random import randint as rand

class cls_enemy:
    def __init__(self, image, x, y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.death_sound = pygame.mixer.Sound("death_sound.mp3")

        self.target_x = 0
        self.target_y = 0
        self.set_target()
        self.speed = 1.5


    def update(self, player, enemies):
        if self.rect.x > self.target_x:
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
        if self.rect.y > self.target_y:
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

        if (abs(self.rect.x - self.target_x) <= 5) and (abs(self.rect.y - self.target_y) <= 5):
            self.set_target()
            self.target_x = player.rect.x
            self.target_y = player.rect.y

        # Check for collisions with other enemies and adjust position
        for enemy in enemies:
            if enemy != self and self.rect.colliderect(enemy.rect):
                if self.rect.centerx < enemy.rect.centerx:
                    self.rect.x -= self.speed
                else:
                    self.rect.x += self.speed
                if self.rect.centery < enemy.rect.centery:
                    self.rect.y -= self.speed
                else:
                    self.rect.y += self.speed

    def set_target(self):
        self.target_x = self.rect.x + rand(-100,100)
        self.target_y = self.rect.y + rand(-100,100)

class cls_super_enemy(cls_enemy):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        self.timer = 0
        self.child = []

    def action(self, enemies):
        self.timer += 1
        if self.timer == 100:
            self.timer = 0

            enemy_x = self.rect.x + rand(-128,128)
            enemy_y = self.rect.y + rand(-128,128)
            enemy = cls_enemy(self.child, enemy_x, enemy_y)
            enemies.append(enemy)

    def update(self, player, enemies):
        super().update(player, enemies)
        self.action(enemies)

def load_enemies():
    pass