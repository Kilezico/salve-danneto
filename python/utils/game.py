import pygame
from . import *

daniel = Rect(686, -10, 128, 129)

won = False

obstacles = list()

obstacles = [
    Obstacle(0, WINDOW_HEIGHT - 100, WINDOW_WIDTH, 100),
    Obstacle(0, 372, 71, 37),
    Obstacle(129, 261, 71, 37),
    Obstacle(0, 118, 71, 37),
    Obstacle(196, 147, 43, 258),
    Obstacle(352, 162, 140, 33),
    Obstacle(595, 127, 205, 33)
]

def draw(win, game, heitor):
    win.blit(game, (0, 0))
    
    heitor.draw(win)

def events(event):
    pass

def update(heitor):
    global won
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        heitor.move_left()
    if keys[pygame.K_d]:
        heitor.move_right()
    if keys[pygame.K_w]:
        heitor.jump()
    heitor.update()

    for obstacle in obstacles:
        obstacle.update(heitor)

    if check_colisions(heitor, daniel):
        won = True

    return won

def reset():
    global won
    won = False