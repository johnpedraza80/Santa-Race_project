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
hp_count = 3
backround_snd = "Music/game_music.mp3"
Santa = pygame.image.load('Images/SantaTexture.png')
GRAVITY = 0.5

PLAYERPOS = 550
PLAYERVELOCITY = 0
PLAYERCHANGE = 0

random.seed(a=None, version=2)

NewWallCoof = 0  # Коэффицент появления новой стены

WALLS_TYPES = [[250, 50], [175, 50], [125, 50]]  # Типы препятствий

WALLS = []  # Список стенок на экране

NEW_WALL_HEIGHT = 0
PlayerColor = 255

DONTLOSE = 1


# загрузка картинки (она должна быть в том же файле что и этот код)

def picture(name):
    fullname = os.path.join('Images', name)
    image = pygame.image.load(fullname)
    return image


class Map(pygame.sprite.Sprite):
    image = picture(random.choice(['map.png', 'map2.png']))

    def __init__(self, all_sprites, num=0):
        super().__init__(all_sprites)
        self.image = Map.image
        self.rect = self.image.get_rect()
        self.rect.x = num

    def update(self):
        if map_flag:
            self.rect = self.rect.move(-5, 0)  # сдвиг картинки
            if self.rect.x == 4000:
                self.image = picture(random.choice(['map2.png', 'map.png']))  # можно добавить другие картинки


class Particle(pygame.sprite.Sprite):
    # частицы разного размера
    fire = [picture("ice_broken.png")]
    for scale in (5, 10, 20):
        fire.append(pygame.transform.scale(fire[0], (scale, scale)))

    def __init__(self, pos, dx, dy):
        super().__init__(all_sprites)
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()
        self.velocity = [dx, dy]
        self.rect.x, self.rect.y = pos
        self.gravity = GRAVITY

    def update(self):
        self.velocity[1] += self.gravity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]


def create_particles(position):
    # количество создаваемых частиц
    particle_count = 30
    # возможные скорости
    numbers = range(-5, 6)
    for _ in range(particle_count):
        Particle(position, random.choice(numbers), random.choice(numbers))


nums = [0, 4000, 8000, 12000]  # кол-во пикселей через которое появляется новая картинка
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
    global NEW_WALL_HEIGHT

    pygame.init()
    screen = pygame.display.set_mode(SIZE)

    font = pygame.font.Font(None, 72)
    sound = pygame.mixer.Sound(backround_snd)
    sound.set_volume(0)
    sound.play()
    lose_flag = False
    Map(all_sprites)
    i = 0
    while i != 0.6:
        i += 0.1
        sound.set_volume(i)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if lose_flag:
                    running = False
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
            WALL_HEIGHT = random.randint(0 + ((1 - NEW_WALL_HEIGHT) * 400), 788 - (NEW_WALL_HEIGHT * 400) -
                                         WALLS_TYPES[TypeOfNewWall][0])  # Определение высоты новой стенки

            WALLS.append([WALLS_TYPES[TypeOfNewWall][0], WALLS_TYPES[TypeOfNewWall][1], 1400, WALL_HEIGHT])
            NEW_WALL_HEIGHT = 1 - NEW_WALL_HEIGHT
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
        del_wall = 100  # число которое больше количества стенок
        if hp_count == 0:
            PlayerColor = 0
            DONTLOSE = 0
            map = Map(all_sprites)
            map_flag = False

            sound.stop()
            font = pygame.font.SysFont("Arial", 72)
            font1 = pygame.font.SysFont("Arial", 30)

            game_over_text = font.render("GAME OVER", True, "red")
            press_text = font1.render("press mouse to countinue", True, "red")

            text_rect = game_over_text.get_rect()
            text_rect.center = (WIND_WIDTH // 2, WIND_HEIGHT // 2)

            text1_rect = press_text.get_rect()
            text1_rect.center = ((WIND_WIDTH // 2), (WIND_HEIGHT // 2) + 50)

            map.image.blit(game_over_text, text_rect)
            map.image.blit(press_text, text1_rect)
            lose_flag = True

        for i in range(len(WALLS)):
            if (WALLS[i][2] < 200 and WALLS[i][2] + 50 >= 188) and WALLS[i][3] < PLAYERPOS + 7 and WALLS[i][3] + \
                    WALLS[i][0] > PLAYERPOS - 7:
                if hp_count != 0:
                    hp_count -= 1
                else:
                    PlayerColor = 0
                    DONTLOSE = 0
                    map_flag = False

                create_particles((200, PLAYERPOS))
                del_wall = i

        if del_wall != 100:
            del WALLS[del_wall]

    pygame.display.flip()



