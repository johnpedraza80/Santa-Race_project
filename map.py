import os
import random

import pygame

# параметры окна и карты
WIND_WIDTH = 1400
WIND_HEIGHT = 788
CELL_SIZE = 50
SIZE = WIND_WIDTH, WIND_HEIGHT
WIDTH = WIND_WIDTH // CELL_SIZE
HEIGHT = WIND_HEIGHT // CELL_SIZE
LEFT = 0
TOP = 0
BG_COLOR = pygame.Color(0, 0, 0)
map_flag = True
meters = 1
hp_count = 15

Santa = pygame.image.load('Images/SantaTexture.png')

PLAYERPOS = 550
PLAYERVELOCITY = 0
PLAYERCHANGE = 0

random.seed(a=None, version=2)

NewWallCoof = 0  # Коэффицент появления новой стены

WALLS_TYPES = [[250, 50], [175, 50], [125, 50]]  # Типы препятствий

WALLS = []  # Список стенок на экране

PlayerColor = 255

DONTLOSE = 1


# загрузка картинки (она должна быть в том же файле что и этот код)

def picture(name):
    fullname = os.path.join('Images', name)
    image = pygame.image.load(fullname)
    return image


class Map(pygame.sprite.Sprite):
    image = picture(random.choice(['map.png', 'map2.png']))

    def __init__(self, all_sprites, num):
        super().__init__(all_sprites)
        self.image = Map.image
        self.rect = self.image.get_rect()
        self.rect.x = num

    def update(self):
        if map_flag:
            self.rect = self.rect.move(-5, 0)
            if self.rect.x == 4000:
                self.image = picture(random.choice(['map2.png', 'map.png']))  # можно добавить другие картинки


nums = [0, 4000, 8000, 12000]
all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()
for i in range(4):
    Map(all_sprites, nums[i])


def game_scene():
    global PLAYERPOS
    global PLAYERVELOCITY
    global PLAYERCHANGE
    global NewWallCoof
    global PlayerColor
    global DONTLOSE
    global map_flag, meters, hp_count

    pygame.init()
    screen = pygame.display.set_mode(SIZE)

    font = pygame.font.Font(None, 72)

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
        text_hp = font.render(f"{hp_count}", True, (255, 0, 0))
        text = font.render(f"{meters // 5}", True, (100, 100, 100))
        if map_flag:
            meters += 1
        screen.blit(text, (10, 10))
        screen.blit(text_hp, (1300, 10))

        all_sprites.update()
        clock.tick(50)

        # Рисуем персонажа
        if DONTLOSE == 1:
            # pygame.draw.circle(screen, (PlayerColor, PlayerColor, PlayerColor), (200, PLAYERPOS), 15)
            iu = pygame.transform.rotozoom(Santa, -PLAYERVELOCITY * 3, 2)
            iur = iu.get_rect(centerx=200, centery=PLAYERPOS)
            screen.blit(iu, iur)

        # Рисуем стены

        for WallsDraw in range(len(WALLS)):
            pygame.draw.polygon(screen, (200, 255, 55), (
                (WALLS[WallsDraw][2], WALLS[WallsDraw][3]), (WALLS[WallsDraw][2] + 10, WALLS[WallsDraw][3]),
                (WALLS[WallsDraw][2] + 10, WALLS[WallsDraw][3] + WALLS[WallsDraw][0]),
                (WALLS[WallsDraw][2], WALLS[WallsDraw][3] + WALLS[WallsDraw][0])))
        pygame.display.flip()
        # Добавляем новую стену

        WillAppearNewWall = random.randint(0, NewWallCoof)
        if WillAppearNewWall == 0:
            TypeOfNewWall = random.randint(0, 2)
            WALLS.append([WALLS_TYPES[TypeOfNewWall][0], WALLS_TYPES[TypeOfNewWall][1], 1400,
                          random.randint(0, 788 - WALLS_TYPES[TypeOfNewWall][0])])
            NewWallCoof = 50 // (400 // WALLS_TYPES[TypeOfNewWall][0])
        else:
            NewWallCoof -= 1

            # Изменение скорости игрока
            if PLAYERCHANGE == 1 and PLAYERPOS > 50:
                PLAYERVELOCITY -= 0.5

            if PLAYERCHANGE == 0 and PLAYERPOS < 750:
                PLAYERVELOCITY += 0.5

            if PLAYERPOS > 788 - 15:
                PLAYERPOS = 788 - 15
                PLAYERVELOCITY = 0

            if PLAYERPOS < 15:
                PLAYERPOS = 15
                PLAYERVELOCITY = 0

            PLAYERPOS += PLAYERVELOCITY

            # Двигаем стены
            MoveWalls = 0
            while MoveWalls < (len(WALLS)):
                WALLS[MoveWalls][2] -= 10 * DONTLOSE
                if WALLS[MoveWalls][2] < -50:
                    WALLS.remove(WALLS[MoveWalls])
                    MoveWalls -= 1

                MoveWalls += 1

        for i in range(len(WALLS)):
            if (WALLS[i][2] < 200 and WALLS[i][2] + 50 >= 188) and WALLS[i][3] < PLAYERPOS + 7 and WALLS[i][3] + \
                    WALLS[i][0] > PLAYERPOS - 7:
                if hp_count != 0:
                    hp_count -= 1
                else:
                    PlayerColor = 0
                    DONTLOSE = 0
                    map_flag = False

    pygame.display.flip()


game_scene()
