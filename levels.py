import pygame
import sys
import os

SIZE = WIDTH, HEIGHT = 1400, 788


def load_image(name, colorkey=None):
    fullname = os.path.join('Images', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Levels(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)


all_sprites = pygame.sprite.Group()


def level_choice():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    bg = pygame.image.load("Images/backround.gif")
    screen.blit(bg, (0, 0))
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

            if event.type == pygame.MOUSEMOTION:
                arrow.rect.topleft = event.pos

        pygame.display.flip()
        screen.blit(bg, (0, 0))


