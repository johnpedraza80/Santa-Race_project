# СОЗДАНИЕ ГЛАВНОГО МЕНЮ


import pygame

# Параметры окна
SIZE = WIDTH, HEIGHT = 800, 600

# Параметры кнопки для игры
X_BUTTON_PLAY, Y_BUTTON_PLAY = 350, 250
WIDTH_BUTTON_PLAY, HEIGHT_BUTTON_PLAY = 100, 50


# КЛАСС ДЛЯ СОЗДАНИЯ КНОПОК
class ImageButton:
    def __init__(self, x, y, width, height, text):
        self.top_rect = pygame.Rect(x, y, width, height)
        self.rect_color = pygame.Color("#475F77")
        self.x = x
        self.y = y
        self.text = text
        self.width = width
        self.height = height

        self.text_surf = pygame.font.Font(None, 30).render(self.text, True, "#FFFFFF")
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self, screen):
        pygame.draw.rect(screen, self.rect_color, self.top_rect)
        screen.blit(self.text_surf, self.text_rect)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    screen.fill("#FFFFFF")
    button_play = ImageButton(X_BUTTON_PLAY, Y_BUTTON_PLAY, WIDTH_BUTTON_PLAY, HEIGHT_BUTTON_PLAY, "PLAY")
    button_play.draw(screen)
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

