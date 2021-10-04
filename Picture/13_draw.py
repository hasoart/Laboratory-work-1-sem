import pygame
import pygame.draw as draw

import draw_objects as dr_obj
import colors

pygame.init()

clock = pygame.time.Clock()
finished = False

FPS = 60
dt = 1/60

WINDOW_SIZE = (800, 1200)
window = pygame.display.set_mode(WINDOW_SIZE)
sky = pygame.Surface((800, 670))

SCREEN_SIZE = (800, 1200)
screen = pygame.Surface(SCREEN_SIZE)
sky.fill(colors.sky_color)

ground = pygame.Surface((800, 730))
ground.fill(colors.ground_color)

hedgehog_count = 3
hedgehog_x = [350, 250, 10]
hedgehog_y = [752, 600, 900]
hedgehog_scale = [1, 0.5, 0.5]
hedgehog_rotate = [0, 10, -10]
hedgehog_orientation = [False, False, False]
hedgehog_velocity = [100, 250, 200]

while not finished:

    screen.blit(sky, (0, 0))
    screen.blit(ground, (0, 670))

    for i in range(hedgehog_count):
        dr_obj.draw_object(dr_obj.hedgehog, screen, hedgehog_x[i], hedgehog_y[i],
                           hedgehog_scale[i], hedgehog_rotate[i], hedgehog_orientation[i])
        hedgehog_x[i] += hedgehog_velocity[i] * dt
        if hedgehog_x[i] <= 0 or hedgehog_x[i] >= SCREEN_SIZE[0]:
            hedgehog_velocity[i] *= -1
            hedgehog_orientation[i] = not hedgehog_orientation[i]

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