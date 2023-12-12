# СОЗДАНИЕ ГЛАВНОГО МЕНЮ
from PIL import Image
import pygame

# Параметры окна
SIZE = WIDTH, HEIGHT = 1400, 788


# КЛАСС ДЛЯ СОЗДАНИЯ КНОПОК
class ImageButton:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        im = Image.open(self.image)
        self.width, self.height = im.size

        self.buttons_list = []

    def load_button(self, screen):
        button = pygame.image.load(self.image).convert_alpha()
        screen.blit(button, (self.x, self.y))
        self.buttons_list.append((self.x, self.y, self.width, self.height))


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    BG = pygame.image.load(r"Images/backround.gif").convert_alpha()
    screen.blit(BG, (0, 0))
    play_btn = ImageButton(500, 200, r"Images/play_button.png")
    play_btn.load_button(screen)
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
