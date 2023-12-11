# СОЗДАНИЕ КАРТЫ


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


class Map:
    def __init__(self, width, height, left, top, cell_size):
        self.width = width
        self.height = height
        self.map = [[0] * self.width for _ in range(height)]
        self.left = left
        self.top = top
        self.cell_size = cell_size


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    map = Map(WIDTH, HEIGHT, LEFT, TOP, CELL_SIZE)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    screen.fill(BG_COLOR)
    pygame.display.flip()
