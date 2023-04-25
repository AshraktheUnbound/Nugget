import pygame, time

class cls_bullet:
    def __init__(self, x, y, direction, image):
        bullet_image = image
        self.image = bullet_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = .03
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
        #self.reload_sound = pygame.mixer.Sound("reload.mp3")
        #self.reload_sound.set_volume(1.5)

        self.capacity = capacity
        self.ammo_count = capacity
        self.ammo_total = self.capacity * 2
        self.fire_rate = 250
        self.time_last_fired = 0
        self.reload_timer = 2000
        self.mode = 'Single_Shot'
        self.bullet_image = bullet_image


    def update(self, player_rect):
        self.rect.centerx = player_rect.centerx
        self.rect.bottom = player_rect.top+48

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def shoot(self, direction):
        modes = {1:'Single_Shot', 2:'Buck_Shot'}

        current_time = time.time() * 1000  # Get the current time in milliseconds
        time_since_last_shot = current_time - self.time_last_fired
        if time_since_last_shot >= self.fire_rate:  # Check if enough time has elapsed since the last shot
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
                self.time_last_fired = current_time

    def reload(self):
        if self.capacity < self.ammo_total:
            self.ammo_count = self.capacity
            self.ammo_total -= self.capacity
        else:
            self.ammo_count = self.ammo_total
            self.ammo_total = 0

        self.time_reloaded = time.time() * 1000
        #self.reload_sound.play()
