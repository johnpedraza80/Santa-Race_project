import os
import random

import pygame

file = [int(i) for i in open('money_and_meters.txt', mode='r')]  # файл для хранения метров и денег
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

count_money = 0
count_money_f = file[0]
record_meters = file[1]
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

WALLS_TYPES = [[250, 50], [150, 50], [100, 50]]  # Типы препятствий

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
    image = picture('map.png')

    def __init__(self, num=0):
        super().__init__(all_sprites)
        self.image = Map.image
        self.rect = self.image.get_rect()
        self.rect.x = num

    def update(self):
        if map_flag:
            self.rect = self.rect.move(-5, 0)  # сдвиг картинки
            self.rect.y = 188
            if self.rect.x == -1400:
                self.rect.x = 0
                self.image = picture('map.png')  # можно добавить другие картинки


class Money(pygame.sprite.Sprite):
    money = pygame.transform.scale(picture('money.png'), (20, 20))

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Money.money
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(1000, 1400)  # границы в которых появляются монетки
        self.rect.y = random.randint(50, 728)

    def update(self):
        global count_money
        if map_flag:
            self.rect = self.rect.move(-9, 0)
        self.rect = self.rect.move(random.randrange(3) - 1, random.randrange(3) - 1)
        if self.rect.y in range(int(PLAYERPOS - 30), int(PLAYERPOS + 30)) and self.rect.x in range(170, 230) or not map_flag:
            count_money += 1
            self.kill()


class ParticleBroke(pygame.sprite.Sprite):
    # частицы разного размера
    fire = [picture("ice_broken.png")]
    for scale in (5, 10, 15, 20):
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


class ParticleFly(pygame.sprite.Sprite):
    fire = [picture("snowflake.png")]
    for scale in (5, 10):
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


def create_particles(position, particle='fly'):
    numbers = range(-5, 6)  # возможные скорости
    if particle == 'broke':
        for _ in range(30):
            ParticleBroke(position, random.choice(numbers), random.choice(numbers))
    if particle == 'fly':
        for _ in range(10):
            ParticleFly(position, random.choice(numbers), random.choice(numbers))


nums = [0]  # кол-во пикселей через которое появляется картинка
all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()
for i in range(1):
    Map(nums[i])


def restart():
    global PLAYERPOS
    global PLAYERVELOCITY
    global PLAYERCHANGE
    global NewWallCoof
    global PlayerColor
    global DONTLOSE
    global map_flag, meters, hp_count
    global NEW_WALL_HEIGHT
    global count_money
    global nums
    global all_sprites
    global clock
    global WALLS
    global WALLS_TYPES

    nums = [0]
    all_sprites = pygame.sprite.Group()
    clock = pygame.time.Clock()
    for i in range(1):
        Map(nums[i])

    meters = 1
    map_flag = True
    count_money = 0
    hp_count = 3

    PLAYERPOS = 550
    PLAYERVELOCITY = 0
    PLAYERCHANGE = 0

    random.seed(a=None, version=2)

    NewWallCoof = 0  # Коэффицент появления новой стены
    WALLS_TYPES = [[250, 50], [150, 50], [100, 50]]  # Типы препятствий

    WALLS = []  # Список стенок на экране

    NEW_WALL_HEIGHT = 0
    PlayerColor = 255
    DONTLOSE = 1

    game_scene()


def game_scene():
    global PLAYERPOS
    global PLAYERVELOCITY
    global PLAYERCHANGE
    global NewWallCoof
    global PlayerColor
    global DONTLOSE
    global map_flag, meters, hp_count
    global NEW_WALL_HEIGHT
    global WALLS

    pygame.init()
    screen = pygame.display.set_mode(SIZE)

    font = pygame.font.Font(None, 72)
    sound = pygame.mixer.Sound(backround_snd)
    sound.set_volume(0)
    sound.play()
    lose_flag = False
    win_flag = False

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
                    restart()
                    lose_flag = False
                if win_flag:
                    restart()
                    win_flag = False

                PLAYERCHANGE = 1
                create_particles((200, PLAYERPOS + 10))

            if event.type == pygame.MOUSEBUTTONUP:
                PLAYERCHANGE = 0

        screen.fill((50, 50, 100))
        all_sprites.draw(screen)
        text_hp = font.render(f"{hp_count}", True, (255, 0, 0))
        text = font.render(f"{meters // 5}", True, (100, 100, 100))
        text_money = font.render(f'{count_money}', True, pygame.Color('gold'))
        if map_flag:
            meters += 1
        screen.blit(text, (10, 10))
        screen.blit(text_hp, (1300, 10))
        screen.blit(text_money, (10, 60))
        if lose_flag:
            text_gameover = font.render('GAME OVER', True, (255, 0, 0))
            screen.blit(text_gameover, (500, 300))
        if win_flag:
            text_gameover = font.render('YOU WIN!', True, (255, 0, 0))
            screen.blit(text_gameover, (500, 300))

        all_sprites.update()
        clock.tick(50)

        if random.randint(0, 20) == 7 and map_flag:
            Money()  # появления новых монеток

        # Рисуем персонажа
        if DONTLOSE == 1:
            iu = pygame.transform.rotozoom(Santa, -PLAYERVELOCITY * 3, 2)
            iur = iu.get_rect(centerx=200, centery=PLAYERPOS)
            screen.blit(iu, iur)

        # Рисуем стены

        for WallsDraw in range(len(WALLS)):
            pygame.draw.polygon(screen, (200, 200, 250), (
                (WALLS[WallsDraw][2], WALLS[WallsDraw][3]), (WALLS[WallsDraw][2] + 10, WALLS[WallsDraw][3]),
                (WALLS[WallsDraw][2] + 10, WALLS[WallsDraw][3] + WALLS[WallsDraw][0]),
                (WALLS[WallsDraw][2], WALLS[WallsDraw][3] + WALLS[WallsDraw][0])))

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
            WALLS = []
            PlayerColor = 0
            DONTLOSE = 0
            map_flag = False
            sound.stop()

            lose_flag = True
        if meters // 5 == 600:
            WALLS = []
            PlayerColor = 0
            DONTLOSE = 0
            map_flag = False
            win_flag = True
            sound.stop()

        for i in range(len(WALLS)):
            if (WALLS[i][2] < 200 and WALLS[i][2] + 50 >= 188) and WALLS[i][3] < PLAYERPOS + 7 and WALLS[i][3] + \
                    WALLS[i][0] > PLAYERPOS - 7:
                if hp_count != 0:
                    hp_count -= 1
                else:
                    PlayerColor = 0
                    DONTLOSE = 0
                    map_flag = False

                create_particles((200, PLAYERPOS), particle='broke')
                del_wall = i

        if del_wall != 100:
            del WALLS[del_wall]

        pygame.display.update()

    file_w = open('money_and_meters.txt', mode='w')
    file_w.seek(0)
    if meters < record_meters:
        file_w.write(f'{count_money_f + count_money}\n{record_meters // 5}')
    else:
        file_w.write(f'{count_money_f + count_money}\n{meters // 5}')
    file_w.close()


