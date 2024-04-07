#Импортируем модуль в файл — в первой строке пишем:
import pygame
#Для автоматической инициализации всех модулей Pygame пишем:
pygame.init()

#Создаём окно с определёнными размерами, с заголовком:

window_size = (800, 600)

screen = pygame.display.set_mode(window_size)

pygame.display.set_caption("Тестовый проект")
#здаём переменную для изображения
image = pygame.image.load("pngegg.png")
#Создаём переменную для хитбокса:
image_rect = image.get_rect()
#Задаём скорость:
speed = 100

#Для создания игрового цикла создаём переменную и задаём цикл:
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
#Этот блок сделает так, чтобы при нажатии на крестик в окне игры программа
# завершалась, а не зависала.

#Задаём управление хитбокса клавишами со стрелками направления движения курсора
#    keys = pygame.key.get_pressed()
#    if keys[pygame.K_LEFT]:
#       image_rect.x -= speed
#    if keys[pygame.K_RIGHT]:
#        image_rect.x += speed
#    if keys[pygame.K_UP]:
#        image_rect.y -= speed
#    if keys[pygame.K_DOWN]:
#        image_rect.y += speed
#Настраиваем движение за курсором:
    if event.type == pygame.MOUSEMOTION:
        mouseX, mouseY = pygame.mouse.get_pos()
#       image_rect.x = mouseX
#       image_rect.y = mouseY
#Если хотим расположить курсор в середине изображения, то
# дополняем строки:
        image_rect.x = mouseX - 40
        image_rect.y = mouseY - 40
# Заполняем цвет фоном — внутри блока while run пишем:
    screen.fill((0,240,200))
#Для появления персонажа пишем после определения фона:
    screen.blit(image, image_rect)
#Чтобы обновлять содержимое зкрана внктри блока while run пишем:
    pygame.display.flip()

# В конце программы используем команду выхода:
pygame.quit()

#Мы создали основу для написания игры, программы, чего угодно.
#Все изменения на экране видны благодаря функции pygame.display.flip.