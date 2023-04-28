import pygame
from load_assets import load_music
from load_assets import cls_map
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

        self.screen_mode = 0
        self.locks = cls_locks()
        load_music()

        bg_image = pygame.image.load(self.image_path + "pyramid.png")
        self.bg_image = pygame.transform.scale(bg_image, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        width = self.SCREEN_WIDTH
        height = self.SCREEN_HEIGHT
        self.main_menu_items = [
            {'text': 'New Game', 'position': (width // 2, height // 4),
             'action': self.start_game},
            {'text': 'Load Save', 'position': (width // 2, height // 2),
             'action': None},
            {'text': 'Exit', 'position': (width // 2, 3 * height // 4),
             'action': self.end_program}
        ]
        self.main_menu_font = pygame.font.Font(None, 72)

        self.main_loop()

    def end_program(self, num):
        self.loop_running = False

    def set_mode(self, mode):
        self.screen_mode = mode

    def start_game(self, num):
        self.map = cls_map(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.set_mode(num)

    def main_loop(self):
        self.map = cls_map(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.mouse_down = False
        self.loop_running = True
        while self.loop_running:
            self.handle_events()

            if self.screen_mode == 0:
                self.render_main_menu()
            elif self.screen_mode == 1:
                self.main_display_movements()
                self.main_display_collisions()
                self.render_main_display()
            elif self.screen_mode == 2:
                self.render_inventory_display()

            # Frame Rate
            self.clock.tick(60)

            # End Game Conditions - DEAD or NO ENEMIES
            if len(self.map.enemies) == 0 or self.map.player.hit_points < 1:
                self.screen_mode = 0

    def render_main_menu(self):
        self.SCREEN.blit(self.bg_image, (0, 0))
        for item in self.main_menu_items:
            item_text = self.main_menu_font.render(item['text'], True, white)
            item_rect = item_text.get_rect()
            item_rect.center = item['position']
            item['rect'] = item_rect

            pygame.draw.rect(self.SCREEN, white, item_rect, 2)
            self.SCREEN.blit(item_text, item_rect)

        # Update the display
        pygame.display.update()
    def render_main_display(self):
        menu_font = pygame.font.Font(None, 72)
        self.SCREEN.fill((0, 55, 0))

        for flower in self.map.flowers:
            self.SCREEN.blit(flower.image, flower.rect)
        for building in self.map.buildings:
            self.SCREEN.blit(building.image, building.rect)
            door = pygame.Surface((building.door_rect[2], building.door_rect[3]))
            door.fill(white)
            self.SCREEN.blit(door, building.door_rect)
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

    def render_inventory_display(self):
        self.SCREEN.fill((200, 200, 200))
        pygame.display.update()

    def main_display_movements(self):
        self.map.player.update(self.locks, self.map.enemies)
        for enemy in self.map.enemies:
            enemy.update(self.map.player, self.map.enemies)
        for bullet in self.map.player.weapon.bullets:
            bullet.rect.x += bullet.speed * bullet.direction[0]
            bullet.rect.y += bullet.speed * bullet.direction[1]

    def main_display_collisions(self):
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
                # print(f'Building rect {building.rect}')
                # print(f'Door Rect {building.door_rect}')
                self.start_game(1)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if self.screen_mode == 0:
                if event.type == pygame.KEYDOWN:
                    pass
                elif event.type == pygame.KEYUP:
                    pass
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for item in self.main_menu_items:
                        if item['rect'].collidepoint(event.pos):
                            print(item['text'])
                            item['action'](1)
                elif event.type == pygame.MOUSEBUTTONUP:
                    pass
            if self.screen_mode == 1:
                if event.type == pygame.KEYDOWN:
                    pass
                elif event.type == pygame.KEYUP:
                    pass
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:  # left mouse button
                        self.mouse_down = True
                    elif pygame.mouse.get_pressed()[2]:  # right mouse button
                        self.map.player.weapon.reload()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:  # left mouse button
                        self.mouse_down = False

                if self.mouse_down:
                    mouse_pos = pygame.mouse.get_pos()
                    direction = (
                    mouse_pos[0] - self.map.player.rect.centerx, mouse_pos[1] - self.map.player.rect.centery)
                    self.map.player.weapon.shoot(direction)

            if self.screen_mode == 2:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_i or event.key == pygame.K_c:
                        if not self.locks.get_key_state(event.key):
                            self.screen_mode = 1
                            self.locks.set_key_state(event.key, True)
                    else:
                        self.locks.set_key_state(event.key, False)
                elif event.type == pygame.KEYUP:
                    self.locks.set_key_state(event.key, False)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pass
                elif event.type == pygame.MOUSEBUTTONUP:
                    pass
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_i or event.key == pygame.K_c:
                        if not self.locks.get_key_state(event.key):
                            self.screen_mode = 1
                            self.locks.set_key_state(event.key, True)
                    else:
                        self.locks.set_key_state(event.key, False)

##########################################
game = cls_game()

'''def main_display_event_handler(self):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            self.loop_running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:  # left mouse button
                self.mouse_down = True
            elif pygame.mouse.get_pressed()[2]:  # right mouse button
                self.map.player.weapon.reload()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # left mouse button
                self.mouse_down = False
    if self.mouse_down:
        mouse_pos = pygame.mouse.get_pos()
        direction = (mouse_pos[0] - self.map.player.rect.centerx, mouse_pos[1] - self.map.player.rect.centery)
        self.map.player.weapon.shoot(direction)

def inventory_event_handler(self):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            self.loop_running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i or event.key == pygame.K_c:
                if not self.locks.key_pressed:
                    self.locks.inventory_toggle()
                    self.locks.key_pressed = True
            else:
                self.locks.key_pressed = False
        elif event.type == pygame.KEYUP:
            self.locks.key_pressed = False'''
