import pygame
import sys
import random
import time
import os 

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BUTTON_COLOR = (0, 128, 255) 

base_path = os.path.dirname(__file__)
background_image_path = os.path.join(base_path, "Tasarm.png")
icon_image_path = os.path.join(base_path, "1.png")

pygame.display.set_caption('Infinite Jump')

if not os.path.exists(icon_image_path):
    print(f"Icon image not found: {icon_image_path}")
    sys.exit()
# if not os.path.exists(background_image_path):
#     print(f"Background image not found: {background_image_path}")
#     sys.exit()

icon_image = pygame.image.load(icon_image_path)
pygame.display.set_icon(icon_image)

# # MUSIC_FILE = r"C:\Users\PC\Desktop\Soul_Echoes_23-05-2024_07-01.wav"
# if not os.path.exists(MUSIC_FILE):
#     print(f"Music file not found: {MUSIC_FILE}")
#     sys.exit()

# background_image = pygame.image.load(background_image_path)
# background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.start_pos = (WIDTH // 2, HEIGHT // 2)
        self.rect.center = self.start_pos
        self.velocity = pygame.math.Vector2(0, 0)
        self.gravity = 0.3
        self.max_velocity = 100
        self.alive = True

    def update(self):
        if self.alive:
            self.velocity.y += self.gravity
            self.rect.move_ip(self.velocity)
            
            if self.rect.left <= 0:
                self.rect.right = WIDTH
            elif self.rect.right >= WIDTH:
                self.rect.left = 0
            elif self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
                self.alive = False

            if abs(self.velocity.x) > self.max_velocity:
                self.velocity.x = self.max_velocity * (self.velocity.x / abs(self.velocity.x))
            if abs(self.velocity.y) > self.max_velocity:
                self.velocity.y = self.max_velocity * (self.velocity.y / abs(self.velocity.y))

    def jump(self, mouse_x, mouse_y):
        target_vector = pygame.math.Vector2(mouse_x - self.rect.centerx, mouse_y - self.rect.centery)
        target_vector.scale_to_length(15)
        self.velocity = target_vector

    def reset(self):
        self.rect.center = self.start_pos
        self.velocity = pygame.math.Vector2(0, 0)
        self.alive = True

class Collectible(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.topleft = (random.randint(0, WIDTH - self.rect.width), random.randint(0, HEIGHT - self.rect.height))

def main_menu(screen):
    font = pygame.font.Font(None, 36)
    

    
    text_play = font.render("Oyna", True, WHITE)
    text_controls = font.render("Kontroller", True, WHITE)
    text_settings = font.render("Ayarlar", True, WHITE)
    text_exit = font.render("Çık", True, WHITE)
    made_by_text = font.render("Made By CyroStar", True, WHITE)

    text_play_rect = text_play.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
    text_controls_rect = text_controls.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
    text_settings_rect = text_settings.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    text_exit_rect = text_exit.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 200))

    # screen.blit(background_image, (0, 0))
    
    pygame.draw.rect(screen, BUTTON_COLOR, text_play_rect.inflate(20, 10))
    pygame.draw.rect(screen, BUTTON_COLOR, text_controls_rect.inflate(20, 10))
    pygame.draw.rect(screen, BUTTON_COLOR, text_settings_rect.inflate(20, 10))
    pygame.draw.rect(screen, BUTTON_COLOR, text_exit_rect.inflate(20, 10))

    pygame.draw.rect(screen, WHITE, text_play_rect.inflate(20, 10), 2)
    pygame.draw.rect(screen, WHITE, text_controls_rect.inflate(20, 10), 2)
    pygame.draw.rect(screen, WHITE, text_settings_rect.inflate(20, 10), 2)
    pygame.draw.rect(screen, WHITE, text_exit_rect.inflate(20, 10), 2)

    screen.blit(text_play, text_play_rect)
    screen.blit(text_controls, text_controls_rect)
    screen.blit(text_settings, text_settings_rect)
    screen.blit(text_exit, text_exit_rect)
    screen.blit(made_by_text, (10, 10))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if text_play_rect.collidepoint(x, y):
                    return True
                elif text_controls_rect.collidepoint(x, y):
                    if controls_menu(screen):
                        return True
                elif text_settings_rect.collidepoint(x, y):
                    if settings_menu(screen):
                        return True
                elif text_exit_rect.collidepoint(x, y):
                    pygame.quit()
                    sys.exit()

def controls_menu(screen):
    font = pygame.font.Font(None, 36)
    text_back = font.render("Geri", True, WHITE)

    text_back_rect = text_back.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
    made_by_text = font.render("Kontroller girilecek", True, WHITE)

    text_line1 = font.render("Zıpla Ve Yemleri topla", True, WHITE)
    text_line1_rect = text_line1.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    text_line2 = font.render("Sakın Enerjin 0 Olmasın", True, WHITE)
    text_line2_rect = text_line2.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))

    text_line3 = font.render("İyi Eğlenceler", True, WHITE)
    text_line3_rect = text_line3.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))

    screen.fill(BLACK)
    screen.blit(text_back, text_back_rect)
    screen.blit(made_by_text, (10, 10))
    screen.blit(text_line1, text_line1_rect)
    screen.blit(text_line2, text_line2_rect)
    screen.blit(text_line3, text_line3_rect)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if text_back_rect.collidepoint(x, y):
                    return True

def settings_menu(screen):
    font = pygame.font.Font(None, 36)
    text_back = font.render("Geri", True, WHITE)
    text_volume_up = font.render("Ses Yükselt", True, WHITE)
    text_volume_down = font.render("Ses Azalt", True, WHITE)
    text_toggle_music = font.render("Müziği Aç/Kapat", True, WHITE)

    text_back_rect = text_back.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
    text_volume_up_rect = text_volume_up.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    text_volume_down_rect = text_volume_down.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
    text_toggle_music_rect = text_toggle_music.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 200))

    screen.fill(BLACK)
    screen.blit(text_back, text_back_rect)
    screen.blit(text_volume_up, text_volume_up_rect)
    screen.blit(text_volume_down, text_volume_down_rect)
    screen.blit(text_toggle_music, text_toggle_music_rect)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if text_back_rect.collidepoint(x, y):
                    return True
                elif text_volume_up_rect.collidepoint(x, y):
                    pygame.mixer.music.set_volume(min(1, pygame.mixer.music.get_volume() + 0.1))
                elif text_volume_down_rect.collidepoint(x, y):
                    pygame.mixer.music.set_volume(max(0, pygame.mixer.music.get_volume() - 0.1))
                elif text_toggle_music_rect.collidepoint(x, y):
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.stop()
                    # else:
                    #     pygame.mixer.music.load(MUSIC_FILE)
                    #     pygame.mixer.music.play(-1)

def restart_screen(screen, collectibles, record_time):
    font = pygame.font.Font(None, 36)
    text_restart = font.render("Tekrar Oyna", True, WHITE)
    text_restart_rect = text_restart.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
    
    text_settings = font.render("Ana Menü", True, WHITE)
    text_settings_rect = text_settings.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    
    text_controls = font.render("Kontroller", True, WHITE)
    text_controls_rect = text_controls.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
    
    text_exit = font.render("Çık", True, WHITE)
    text_exit_rect = text_exit.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 200))
    
    text_record = font.render(f"Rekorun: {record_time:.2f} saniye", True, WHITE)
    text_record_rect = text_record.get_rect(topleft=(10, 10))

    screen.fill(BLACK)
    screen.blit(text_restart, text_restart_rect)
    screen.blit(text_settings, text_settings_rect)
    screen.blit(text_controls, text_controls_rect)
    screen.blit(text_exit, text_exit_rect)
    screen.blit(text_record, text_record_rect)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if text_restart_rect.collidepoint(x, y):
                    for collectible in collectibles:
                        collectible.kill()
                    return True
                elif text_settings_rect.collidepoint(x, y):
                    for collectible in collectibles:
                        collectible.kill()
                    return False 
                elif text_controls_rect.collidepoint(x, y):
                    if controls_menu(screen):
                        return True
                elif text_exit_rect.collidepoint(x, y):
                    pygame.quit()
                    sys.exit()


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Infinite Jump')

    clock = pygame.time.Clock()

    max_clicks = 15
    click_timer = 0
    record_time = 0

    while True:
        if not main_menu(screen):
            break

        player = Player()
        collectibles = pygame.sprite.Group()
        all_sprites = pygame.sprite.Group()
        all_sprites.add(player)

        running = True
        clicks_left = max_clicks
        start_time = time.time()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and clicks_left > 0:
                    if player.alive:
                        x, y = event.pos
                        player.jump(x, y)
                        clicks_left -= 1

            all_sprites.update()

            click_timer += clock.get_time()
            if click_timer >= 2500:
                click_timer = 0
                collectible = Collectible()
                collectibles.add(collectible)
                all_sprites.add(collectible)

            hits = pygame.sprite.spritecollide(player, collectibles, True)
            if hits:
                for hit in hits:
                    clicks_left += 3

            screen.fill(WHITE)
            all_sprites.draw(screen)

            font = pygame.font.Font(None, 24)
            text_clicks = font.render(f"Enerji düzeyi: {clicks_left}", True, BLACK)
            screen.blit(text_clicks, (WIDTH - text_clicks.get_width() - 10, 10))

            elapsed_time = time.time() - start_time
            text_time = font.render(f"Süre: {elapsed_time:.2f}", True, BLACK)
            screen.blit(text_time, (10, 10))

            pygame.display.flip()
            clock.tick(60)

            if not player.alive:
                if elapsed_time > record_time:
                    record_time = elapsed_time
                if not restart_screen(screen, collectibles, record_time):
                    pygame.quit()
                    sys.exit()
                player.reset()
                clicks_left = max_clicks
                start_time = time.time()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
