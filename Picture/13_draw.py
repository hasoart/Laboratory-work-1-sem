import pygame
import pygame.draw as draw

import draw_objects as dr_obj
import colors

pygame.init()

clock = pygame.time.Clock()
finished = False

FPS = 60
WINDOW_SIZE = (400, 600)
window = pygame.display.set_mode(WINDOW_SIZE)
sky = pygame.Surface((800, 670))

screen = pygame.Surface((800, 1200))
sky.fill(colors.sky_color)

ground = pygame.Surface((800, 730))
ground.fill(colors.ground_color)

while not finished:
    
    screen.blit(sky, (0, 0))
    screen.blit(ground, (0, 670))

    dr_obj.draw_object(dr_obj.get_hedgehog(), screen, 350, 752, 1)
    dr_obj.draw_object(dr_obj.hedgehog, screen, 250, 600, 0.5, 10)
    dr_obj.draw_object(dr_obj.hedgehog, screen, 10, 900, 0.5, -10)

    dr_obj.draw_object(dr_obj.mushroom, screen, 700, 1000, 1/3)
    dr_obj.draw_object(dr_obj.mushroom, screen, 750, 990, 0.5, 9)
    dr_obj.draw_object(dr_obj.mushroom, screen, 720, 990, 0.5, -3)
    dr_obj.draw_object(dr_obj.mushroom, screen, 620, 950, 1, -7)

    pillars = [(0  , 0,  65, 730),
               (102, 0, 205, 800),
               (560, 0,  70, 725),
               (730, 0,  50, 820)]
    for pillar in pillars:
        draw.rect(screen, colors.pillar_color, pillar)

    screen_scaled = pygame.transform.scale(screen, WINDOW_SIZE)
    window.blit(screen_scaled, (0, 0))

    pygame.display.update()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()