
import pygame
import random

# Устанавливаем размеры окна и цвета
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)

# Инициализируем игру и создаем окно
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Push Off Game")

# Определяем скорость движения первого объекта и начальные позиции
speed1 = random.randint(1, 3)
x1, y1 = 0, HEIGHT // 2

# Устанавливаем количество очков и создаем текстовое отображение
score1 = 0
score2 = 0
font = pygame.font.Font(None, 36)

# Создаем второй объект (курсор мыши)
x2, y2 = 0, HEIGHT // 2
object2 = pygame.mouse.get_pos()

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновляем позицию первого объекта
    x1 += speed1
    if x1 >= WIDTH:
        x1 = 0
        score1 += 1

    # Обновляем позицию второго объекта (курсор мыши)
    x2, y2 = pygame.mouse.get_pos()

    # Проверяем столкновение объектов
    if x2 >= x1 and x2 <= x1 + 50:
        score2 += 1
        x1 = 0

    # Очищаем экран
    screen.fill(WHITE)

    # Рисуем первый объект
    pygame.draw.rect(screen, (255, 0, 0), (x1, y1, 50, 50))

    # Отображаем количество очков для каждого объекта
    text1 = font.render(f"Player 1 Score: {score1}", True, (0, 0, 0))
    text2 = font.render(f"Player 2 Score: {score2}", True, (0, 0, 0))
    screen.blit(text1, (10, HEIGHT - 40))
    screen.blit(text2, (WIDTH - 200, HEIGHT - 40))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()


#Этот код создает игру, в которой первый объект перемещается случайным образом
# слева направо, а второй объект перемещается мышкой в правой части окна.
# Если первый объект достигает левой стороны окна, второй объект получает
# очко. Если второй объект сталкивается с первым, первый объект получает
# очко. Количество набранных очков отображается в углах окна для каждого объекта.
# Приятной игры!