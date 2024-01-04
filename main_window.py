# СОЗДАНИЕ ГЛАВНОГО МЕНЮ
from PIL import Image
import pygame
import levels

pygame.mixer.pre_init(44100, -16, 1, 512)
import os
import sys

# КОНСТАНТЫ
SIZE = WIDTH, HEIGHT = 1400, 788
BACKROUND_IMAGE = "Images/backround.gif"
BACKROUND_MUSIC = "Music/backround_music.mp3"
PLAY_BUTTON = "play_button.png"
CLICK_SOUND = "Music/click.mp3"


def load_image(name, colorkey=None):
    fullname = os.path.join('Images', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


# Класс главного меню
class Menu:
    def __init__(self, size, bg_image):  # объект принимает размеры окна, фоновое изображение и фоновую музыку
        # Параметры окна
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Santa Race")

        # Всякие нужные значения
        self.x, self.y = self.size = size
        self.bg_image = bg_image
        self.im = Image.open(self.bg_image)
        self.bg = pygame.image.load(self.bg_image)
        self.sound = pygame.mixer.Sound(BACKROUND_MUSIC)

    def load_bg(self):
        # Загрузка заднего фона
        self.screen.blit(self.bg, (0, 0))

    def play_music(self):
        # Проигрыватель музыки главного меню
        self.sound.play(-1)
        self.sound.set_volume(0.4)


all_sprites = pygame.sprite.Group()


class Play(pygame.sprite.Sprite):
    button_play = load_image(PLAY_BUTTON)

    def __init__(self, group):
        super().__init__(group)
        self.image = Play.button_play
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


if __name__ == '__main__':
    pygame.init()

    menu = Menu(SIZE, BACKROUND_IMAGE)
    menu.play_music()
    menu.load_bg()
    button_play = Play(all_sprites)
    all_sprites.draw(menu.screen)
    running = True

    image = load_image("cursor.png")
    arrow = pygame.sprite.Sprite(all_sprites)
    arrow.image = image
    arrow.rect = arrow.image.get_rect()
    pygame.mouse.set_visible(False)

    while running:
        all_sprites.update()
        all_sprites.draw(menu.screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                all_sprites.update(event)
                if button_play.flag1:
                    running = False

                    levels.level_choice()

            if event.type == pygame.MOUSEMOTION:
                arrow.rect.topleft = event.pos

        pygame.display.flip()
        menu.load_bg()
