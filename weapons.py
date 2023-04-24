import pygame

class cls_bullet:
    def __init__(self, x, y, direction, image):
        bullet_image = image
        self.image = bullet_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = .05
        self.direction = direction

    def update(self):
        pass

class cls_weapon:
    def __init__(self, x, y, capacity, image, bullet_image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.bullets = []
        self.fire_sound = pygame.mixer.Sound("fire_sound.wav")
        self.reload_sound = pygame.mixer.Sound("reload.mp3")
        self.reload_sound.set_volume(1.5)
        self.capacity = capacity
        self.ammo_count = capacity
        self.ammo_total = self.capacity * 3
        self.mode = 'Single_Shot'
        self.bullet_image = bullet_image


    def update(self, player_rect):
        self.rect.centerx = player_rect.centerx
        self.rect.bottom = player_rect.top+48

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def shoot(self, direction):
        modes = {1:'Single_Shot', 2:'Buck_Shot'}
        if self.ammo_count == 0:
            self.reload()
        else:
            if self.mode == modes[1]:
                bullet = cls_bullet(self.rect.centerx, self.rect.top, direction, self.bullet_image)
                self.bullets.append(bullet)
            elif self.mode == modes[2]:
                num_bullets = 5  # Change the number of bullets as per your requirement
                angle = 10  # Change the angle as per your requirement
                for i in range(num_bullets):
                    bullet_direction = list(direction)
                    bullet_direction[0] += (i - num_bullets // 2) * angle
                    bullet_direction = tuple(bullet_direction)
                    bullet = cls_bullet(self.rect.centerx, self.rect.top, bullet_direction, self.bullet_image)
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

        self.reload_sound.play()
