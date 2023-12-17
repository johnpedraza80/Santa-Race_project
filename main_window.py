# СОЗДАНИЕ ГЛАВНОГО МЕНЮ
from PIL import Image
import pygame

# КОНСТАНТЫ
SIZE = WIDTH, HEIGHT = 1400, 788
BACKROUND_IMAGE = "Images/backround.gif"
BACKROUND_MUSIC = "Music/backround_music.mp3"


# Класс главного меню
class Menu:
    def __init__(self, size, bg_image, sound):  # объект принимает размеры окна, фоновое изображение и фоновую музыку
        # Параметры окна
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Santa Race")

        # Всякие нужные значения
        self.x, self.y = self.size = size
        self.bg_image = bg_image
        self.sound = sound
        self.im = Image.open(self.bg_image)
        self.bg = pygame.image.load(self.bg_image)

    def load_bg(self):
        # Загрузка заднего фона
        self.screen.blit(self.bg, (0, 0))

    def play_music(self):
        # Проигрыватель музыки главного меню
        pygame.mixer.music.load(self.sound)
        pygame.mixer.music.play(-1, 0.5)


if __name__ == '__main__':
    pygame.init()
    menu = Menu(SIZE, BACKROUND_IMAGE, BACKROUND_MUSIC)
    menu.play_music()
    menu.load_bg()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
