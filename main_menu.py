import pygame
from load_assets import load_music, load_images, load_player, load_enemies
from load_assets import load_flowers, load_buildings
from locks import cls_locks
from colors import cls_color

white = (255, 255, 255)

class cls_game:
    def __init__(self):
        self.image_path = 'resources/images//'

        pygame.init()
        self.SCREEN_WIDTH = pygame.display.Info().current_w
        self.SCREEN_HEIGHT = pygame.display.Info().current_h
        self.SCREEN = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT),
                                              pygame.FULLSCREEN)
        pygame.display.set_caption('Nugget')
        self.clock = pygame.time.Clock()

        self.locks = cls_locks()

        self.main_menu()

    def end_program(self):
        self.running = False

    def main_menu(self):
        width = self.SCREEN_WIDTH
        height = self.SCREEN_HEIGHT
        bg_image = pygame.image.load(self.image_path + "pyramid.png")
        bg_image = pygame.transform.scale(bg_image, (width, height))
        menu_font = pygame.font.Font(None, 72)
        load_music()

        menu_items = [
            {'text': 'New Game', 'position': (width // 2, height // 4),
             'action': self.main_loop},
            {'text': 'Load Save', 'position': (width // 2, height // 2),
             'action': None},
            {'text': 'Exit', 'position': (width // 2, 3 * height // 4),
             'action': self.end_program}
        ]

        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for item in menu_items:
                        if item['rect'].collidepoint(event.pos):
                            print(item['text'])
                            item['action']()

            self.SCREEN.blit(bg_image, (0, 0))
            for item in menu_items:
                item_text = menu_font.render(item['text'], True, white)
                item_rect = item_text.get_rect()
                item_rect.center = item['position']
                item['rect'] = item_rect

                pygame.draw.rect(self.SCREEN, white, item_rect, 2)
                self.SCREEN.blit(item_text, item_rect)

            # Update the display
            pygame.display.update()

            self.clock.tick(60)

    def main_loop(self):
        self.map = cls_map(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)

        menu_font = pygame.font.Font(None, 72)

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
                        self.map.player.weapon.reload()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:  # left mouse button
                        mouse_down = False
            if mouse_down:
                mouse_pos = pygame.mouse.get_pos()
                direction = (mouse_pos[0] - self.map.player.rect.centerx, mouse_pos[1] - self.map.player.rect.centery)
                self.map.player.weapon.shoot(direction)

            # Movement Logic
            self.map.player.update(self.locks, self.map.enemies)
            for enemy in self.map.enemies:
                enemy.update(self.map.player, self.map.enemies)
            for bullet in self.map.player.weapon.bullets:
                bullet.rect.x += bullet.speed * bullet.direction[0]
                bullet.rect.y += bullet.speed * bullet.direction[1]

            # Collision Logic
            for enemy in self.map.enemies:
                if self.map.player.rect.colliderect(enemy):
                    print('Collision!')
                    self.map.player.hit_points += -1

                    enemy.death_sound.play()
                    self.map.enemies.remove(enemy)
                    self.map.player.kills += 1

            for bullet in self.map.player.weapon.bullets:
                for enemy in self.map.enemies:
                    if bullet.rect.colliderect(enemy):
                        self.map.player.weapon.bullets.remove(bullet)
                        self.map.enemies.remove(enemy)
                        self.map.player.kills += 1
            for building in self.map.buildings:
                if self.map.player.rect.colliderect(building.door_rect):
                    #print(f'Building rect {building.rect}')
                    #print(f'Door Rect {building.door_rect}')
                    running = False


            # DRAW THE FRAME AFTER ALL LOGIC
            self.SCREEN.fill((0, 55, 0))

            for flower in self.map.flowers:
                self.SCREEN.blit(flower.image, flower.rect)
            for building in self.map.buildings:
                self.SCREEN.blit(building.image, building.rect)
                #door = pygame.Surface((building.door_rect[2], building.door_rect[3]))
                #door.fill(white)
                #self.SCREEN.blit(door, building.door_rect)
            for enemy in self.map.enemies:
                self.SCREEN.blit(enemy.image, enemy.rect)
            self.map.player.draw(self.SCREEN)
            for bullet in self.map.player.weapon.bullets:
                if bullet.rect.left > self.SCREEN_WIDTH or bullet.rect.right < 0 or bullet.rect.top > self.SCREEN_HEIGHT or bullet.rect.bottom < 0:
                    self.map.player.weapon.bullets.remove(bullet)
                else:
                    self.SCREEN.blit(bullet.image, bullet.rect)

            item_text = menu_font.render(
                f'KILLS: {self.map.player.kills} - HITPOITS: {self.map.player.hit_points} - AMMO:({self.map.player.weapon.ammo_count}/{self.map.player.weapon.ammo_total})',
                True, (255, 255, 255))
            item_rect = item_text.get_rect()
            self.SCREEN.blit(item_text, item_rect)
            pygame.display.update()

            # Frame Rate
            self.clock.tick(60)

            # End Game Conditions - DEAD or NO ENEMIES
            if len(self.map.enemies) == 0 or self.map.player.hit_points < 1:
                running = False

    def render_main_display(self):
        pass

    def render_inventory(self):
        pass


class cls_map:
    def __init__(self, w, h):
        WIDTH = w
        HEIGHT = h
        self.images = load_images()
        self.player = load_player(WIDTH // 2, HEIGHT // 2, self.images)
        self.enemies = load_enemies(self.images, WIDTH, HEIGHT)
        self.flowers = load_flowers(self.images, WIDTH, HEIGHT)
        self.buildings = load_buildings(self.images, WIDTH, HEIGHT)





game = cls_game()
