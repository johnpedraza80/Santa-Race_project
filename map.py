# карта
import os

import pygame

import random

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

PLAYERPOS = 550
PLAYERVELOCITY = 0
PLAYERCHANGE = 0

random.seed(a=None, version=2)

NewWallCoof = 0 #Коэффицент появления новой стены

WALLS_TYPES = [[100, 50], [50, 50], [25, 50]] #Типы препятствий

WALLS = [] #Список стенок на экране


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

            #Двигаем стены
            MoveWalls = 0
            while MoveWalls < (len(WALLS)):
                WALLS[MoveWalls][2] -= 7
                if WALLS[MoveWalls][2] < -50:
                    WALLS.remove(WALLS[MoveWalls])
                    MoveWalls -= 1

                MoveWalls += 1

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
                PLAYERCHANGE = 1

            if event.type == pygame.MOUSEBUTTONUP:
                PLAYERCHANGE = 0

        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        all_sprites.update()
        clock.tick(50)

        #Рисуем персонажа (кружочек)

        pygame.draw.circle(screen, (255, 255, 255), (200, PLAYERPOS), 15)

        #Рисуем стены

        for WallsDraw in range(len(WALLS)):
            pygame.draw.polygon(screen, (255, 255, 255), ((WALLS[WallsDraw][2], WALLS[WallsDraw][3]), (WALLS[WallsDraw][2] + 10, WALLS[WallsDraw][3]), (WALLS[WallsDraw][2] + 10, WALLS[WallsDraw][3] + WALLS[WallsDraw][0]), (WALLS[WallsDraw][2], WALLS[WallsDraw][3] + WALLS[WallsDraw][0])))
        pygame.display.flip()
        #Добавляем новую стену

        WillAppearNewWall = random.randint(0, NewWallCoof)
        if WillAppearNewWall == 0:
            TypeOfNewWall = random.randint(0, 2)
            WALLS.append([WALLS_TYPES[TypeOfNewWall][0], WALLS_TYPES[TypeOfNewWall][1], 800, random.randint(0, 600 - WALLS_TYPES[TypeOfNewWall][0])])
            NewWallCoof = 225 // (400 // WALLS_TYPES[TypeOfNewWall][0])

        else:
            NewWallCoof -= 1

        #Изменение скорости игрока
            if PLAYERCHANGE == 1 and PLAYERPOS > 50:
                PLAYERVELOCITY -= 0.5

            if PLAYERCHANGE == 0 and PLAYERPOS < 550:
                PLAYERVELOCITY += 0.5

            if PLAYERPOS > 585:
                PLAYERPOS = 585
                PLAYERVELOCITY = 0

            if PLAYERPOS < 15:
                PLAYERPOS = 15
                PLAYERVELOCITY = 0

            PLAYERPOS += PLAYERVELOCITY
    pygame.display.flip()
