import random

import pygame
import pygame.draw as draw

import colors


def polygon_outlined(surface, colors, coords, width=0):
    """
    polygon_outlined(surface, colors, coords, width=0)
    returns - None

    Draws filled polygon with outline using the coordinates of vertices
    surface(type - pygame.Surface) - surface to draw on
    colors(type - tuple:(fill_color, outline_color)) - colors to use
    coords(list(coordinates) or tuple(coordinates)) - coordinates of polygon vertices
    width(int, optional) - width of outline in pixels
    """

    fill_color, outline_color = colors
    draw.polygon(surface, fill_color, coords)
    draw.polygon(surface, outline_color, coords, width)


def circle_outlined(surface, colors, center, radius, width=0):
    """
    circle_outlined(surface, colors, center, radius, width=0)
    returns - None

    Draws filled circle with outline using center and radius
    surface(type - pygame.Surface) - surface to draw on
    colors(type - tuple:(fill_color, outline_color)) - colors to use
    center(list(coordinates) or tuple(coordinates)) - coordinates of circle center
    radius(int or float) - radius of the circle
    width(int, optional) - width of outline in pixels
    """

    fill_color, outline_color = colors
    draw.circle(surface, fill_color, center, radius)
    draw.circle(surface, outline_color, center, radius, width)


def ellpise_outlined(surface, colors, coords, width=0):
    """
    ellpise_outlined(surface, colors, coords, width=0)
    returns - None

    Draws filled ellipse with outline using coordinates of top-left corner, width and height
    surface(type - pygame.Surface) - surface to draw on
    colors(type - tuple:(fill_color, outline_color)) - colors to use
    coords(list(x, y, w, h) or tuple(x, y, w, h)) - (x,y) coordinates of the top-left corner, (w,h) width/height of ellipse
    width(int, optional) - width of outline in pixels
    """
    fill_color, outline_color = colors
    draw.ellipse(surface, fill_color, coords)
    draw.ellipse(surface, outline_color, coords, width)


def get_mushroom():
    """
    get_mushroom(empty)
    returns - pygame.Surface

    Returns a pygame.Surface with a mushroom drawn on it 
    """

    mushroom = pygame.Surface((100, 100), pygame.SRCALPHA)
    draw.ellipse(mushroom, colors.white, (40, 20, 20, 60))
    draw.ellipse(mushroom, colors.red, (20, 10, 60, 20))
    draw.ellipse(mushroom, colors.white, (40, 20, 10, 5))
    draw.ellipse(mushroom, colors.white, (32, 13, 10, 5))
    draw.ellipse(mushroom, colors.white, (60, 15, 10, 5))

    return mushroom


mushroom = get_mushroom()


def get_hedgehog():
    """
    get_hedgehog(empty)
    returns - pygame.Surface

    Returns a pygame.Surface with a hedgehog drawn on it 
    """

    # Body
    hedgehog = pygame.Surface((315, 600), pygame.SRCALPHA)
    body_ellipses = [[0  , 150, 40 , 20],
                     [265, 155, 25 , 15],
                     [10 , 100, 270, 90],
                     [25 , 165, 40 , 20],
                     [238, 170, 40 , 20],
                     [244, 122, 72 , 40]]
    for ellipse in body_ellipses:
        ellpise_outlined(hedgehog, colors.hedgehog_colors, ellipse, 2)


    # Eyes and nose
    circle_outlined(hedgehog, colors.eye_colors, (281, 134), 5, 1)
    circle_outlined(hedgehog, colors.eye_colors, (296, 130), 5, 1)
    circle_outlined(hedgehog, colors.eye_colors, (315, 138), 3, 1)

    # Needles
    needle = pygame.Surface((28, 80), pygame.SRCALPHA)
    polygon_outlined(needle, colors.needle_colors, ((7, 0), (0, 80), (14, 80)), 1)
    polygon_outlined(needle, colors.needle_colors, ((21, 0), (14, 80), (28, 80)), 1)

    for i in range(70):
        if i == 55:
            hedgehog.blit(pygame.transform.rotate(mushroom, 20), (40, 20))
            hedgehog.blit(pygame.transform.rotate(mushroom, -10), (130, 25))
            draw.circle(hedgehog, colors.apple_color, (40, 70), 30)
        turn = random.randint(-20, 40)
        x = random.randint(5, 220)
        y = random.randint(20, 100)    
        hedgehog.blit(pygame.transform.rotate(needle, turn), (x, y))

    return hedgehog


hedgehog = get_hedgehog()


def draw_object(obj, surface, x0=0, y0=0, scale=1, rotate=0, orient=False):
    """
    draw_object(obj, surface, x0=0, y0=0, scale=1, rotate=0)
    returns - None

    blits obj to surface with given trasformations

    obj(pygame.Surface) - surface to be transformed and blitted
    surface(pygame.Surface) - surface to be blitted on
    x0(float or int, optional) - x-coordinate if top-left corner of obj relative to surface 
    y0(float or int, optional) - y-coordinate if top-left corner of obj relative to surface 
    scale(float or int, optional) - how much obj is scaled before blitting 
    rotate(float or int, optional) - how much(in degrees) obj is rotated before blitting
    orient(bool) - if False nothing is changed, otherwise obj is flipped horizontally
    """

    object_scaled = pygame.transform.scale(obj, (int(obj.get_width() * scale), int(obj.get_height() * scale)))
    object_rotated = pygame.transform.rotate(object_scaled, rotate)
    object_flipped = pygame.transform.flip(object_rotated, orient, 0)
    surface.blit(object_flipped, (x0, y0))