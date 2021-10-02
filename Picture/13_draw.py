import pygame
from pygame.draw import *
from random import *

pygame.init()

FPS = 60
sc = pygame.display.set_mode((800, 1200))

#Фон
sky = pygame.Surface((800, 670))
sky.fill((44, 160, 90))
ground = pygame.Surface((800, 730))
ground.fill((108, 93, 83))
sc.blit(sky, (0, 0))
sc.blit(ground, (0, 670))

#Еж
#Тело ежика
ej = pygame.Surface((600, 600), pygame.SRCALPHA)
ellipse(ej, (72, 55, 55), [0, 150, 40, 20])
ellipse(ej, (143, 139, 138), [0,150, 40, 20], 2)
ellipse(ej, (72, 55, 55), [265, 155, 25, 15])
ellipse(ej, (143, 139, 138), [265, 155, 25, 15], 2)
ellipse(ej, (72, 55, 55), [10, 100, 270, 90])
ellipse(ej, (143, 139, 138), [10, 100, 270, 90], 2)
ellipse(ej, (72, 55, 55), [25, 165, 40, 20])
ellipse(ej, (143, 139, 138), [25, 165, 40, 20], 2)
ellipse(ej, (72, 55, 55), [238, 170, 40, 20])
ellipse(ej, (143, 139, 138), [238, 170, 40, 20], 2)
ellipse(ej, (72, 55, 55), [244, 122, 72, 40])
ellipse(ej, (143, 139, 138), [244, 122, 72, 40], 2)
#Глаза и нос
circle(ej, (0, 0, 0), (281, 134), 5)
circle(ej, (143, 139, 138), (281, 134), 5, 1)
circle(ej, (0, 0, 0), (296, 130), 5)
circle(ej, (143, 139, 138), (296, 130), 5, 1)
circle(ej, (0, 0, 0), (315, 138), 3)
circle(ej, (143, 139, 138), (315, 138), 3, 1)


#Мухомор

mh = pygame.Surface((100, 100), pygame.SRCALPHA)
ellipse(mh, (255, 255, 255), (40, 20, 20, 60))
ellipse(mh, (255, 0, 0), (20, 10, 60, 20))
ellipse(mh, (255, 255, 255), (40, 20, 10, 5))
ellipse(mh, (255, 255, 255), (32, 13, 10, 5))
ellipse(mh, (255, 255, 255), (60, 15, 10, 5))




#Иглы

ig = pygame.Surface((28, 80), pygame.SRCALPHA)

polygon(ig, (0, 0, 0), ((7, 0), (0, 80), (14, 80)))
polygon(ig, (120, 39, 70), ((7, 0), (0, 80), (14, 80)), 1)
polygon(ig, (0, 0, 0), ((21, 0), (14, 80), (28, 80)))
polygon(ig, (43, 39, 38), ((7, 0), (0, 80), (14, 80)), 1)

for i in range(70):
    if i == 55:
        ej.blit(pygame.transform.rotate(mh, 20), (40, 20))
        ej.blit(pygame.transform.rotate(mh, -10), (130, 25))
        circle(ej, (200, 170, 10), (40, 70), 30)
    turn = randint(-20, 40)
    x = randint(5, 220)
    y = randint(20, 100)    
    ej.blit(pygame.transform.rotate(ig, turn), (x, y))

sc.blit(ej, (350, 752))

#еж под прямоугольничком)
minej = pygame.transform.scale(ej, (ej.get_width()//2, ej.get_height()//2))
sc.blit(pygame.transform.rotate(minej, 10), (250, 600))

#еж в углу)
sc.blit(pygame.transform.rotate(minej, -10), (10, 900))

#минимухоморчики
minimh = pygame.transform.scale(mh, (mh.get_width()//2, mh.get_height()//2))
miniminimh = pygame.transform.scale(mh, (mh.get_width()//3, mh.get_height()//3))

sc.blit(miniminimh, (700, 1000))
sc.blit(pygame.transform.rotate(minimh, 9), (750, 990))
sc.blit(pygame.transform.rotate(minimh, -3), (720, 990))
sc.blit(pygame.transform.rotate(mh, -7), (620, 950))

#Прямоугольнички? (Чтобы все ежики были под ними)
rect(sc, (212, 170, 0), (0, 0, 65, 730))
rect(sc, (212, 170, 0), (102, 0, 205, 800))
rect(sc, (212, 170, 0), (560, 0, 70, 725))
rect(sc, (212, 170, 0), (730, 0, 50, 820))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()