import pygame
import sys
import os
import map
import music_play

SIZE = WIDTH, HEIGHT = 1400, 788
LEVEL1 = 'level1.png'
CLICK_SOUND = "Music/click.mp3"


def load_image(name, colorkey=None):
    fullname = os.path.join('Images', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Levels(pygame.sprite.Sprite):
    button = load_image(LEVEL1)

    def __init__(self, group):
        super().__init__(group)
        self.image = Levels.button
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2 - 200
        self.rect.y = HEIGHT // 2 - 150
        self.sound = pygame.mixer.Sound(CLICK_SOUND)
        self.flag1 = False

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.flag1 = True
            self.sound.play(0)


all_sprites = pygame.sprite.Group()


def level_choice():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    bg = pygame.image.load("Images/backround.gif")
    screen.blit(bg, (0, 0))
    level = Levels(all_sprites)
    image = load_image("cursor.png")
    arrow = pygame.sprite.Sprite(all_sprites)
    arrow.image = image
    arrow.rect = arrow.image.get_rect()
    pygame.mouse.set_visible(False)
    running = True
    while running:
        all_sprites.update()
        all_sprites.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                all_sprites.update(event)
                if level.flag1:
                    music_play.sound.stop()
                    map.game_scene()

                    running = False

            if event.type == pygame.MOUSEMOTION:
                arrow.rect.topleft = event.pos

        pygame.display.flip()
        screen.blit(bg, (0, 0))
