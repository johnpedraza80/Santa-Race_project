# СОЗДАНИЕ КАРТЫ
import os

import pygame

# параметры окна и карты
WIND_WIDTH = 800
WIND_HEIGHT = 600
CELL_SIZE = 50
SIZE = WIND_WIDTH, WIND_HEIGHT
WIDTH = WIND_WIDTH // CELL_SIZE
HEIGHT = WIND_HEIGHT // CELL_SIZE
LEFT = 0
TOP = 0
BG_COLOR = pygame.Color(0, 0, 0)
MAP_PICT = "map.png"


# загрузка картинки (она должна быть в том же файле что и этот код)

def picture(flag=True, name=MAP_PICT):
    if flag:
        fullname = os.path.join('Images', name)
        image = pygame.image.load(fullname)
        return image


class Map(pygame.sprite.Sprite):
    image = picture()

    def __init__(self, width, height, left, top, cell_size):
        super().__init__(all_sprites)
        self.width = width
        self.height = height
        self.map = [[0] * self.width for _ in range(height)]
        self.left = left
        self.top = top
        self.cell_size = cell_size
        self.image = Map.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.number = 4000

    # обновление экрана (картинка сдвигается << на 10)
    def update(self, num=-10):
        if True:
            self.rect = self.rect.move(num, 0)
            self.number -= 10


all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    map = Map(WIDTH, HEIGHT, LEFT, TOP, CELL_SIZE)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        screen.fill(pygame.Color("black"))
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
        clock.tick(50)
    pygame.display.flip()
