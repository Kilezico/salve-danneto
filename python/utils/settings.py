import pygame
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARK_RED = (125, 0, 0)
DARK_GREEN = (0, 125, 0)
DARK_BLUE = (0, 0, 125)


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_RECT = pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
FLOOR_HEIGHT = 100
FPS = 60

GRAVITY = 1

font = pygame.font.SysFont(None, 80)

class Rect:
    def __init__(self, x, y, w, h):
        self.position = pygame.Vector2()
        self.position.xy = x, y
        self.width = w
        self.height = h


def check_colisions(obj1, obj2):
    if obj1.position.x + obj1.width > obj2.position.x:
        if obj1.position.x < obj2.position.x + obj2.width:
            if obj1.position.y + obj1.height > obj2.position.y:
                if obj1.position.y < obj2.position.y + obj2.height:
                    return True
    return False


