import pygame
from utils.settings import *

class Heitor():
    def __init__(self, x, y, color):
        self.position = pygame.Vector2()
        self.position.xy = (x, y)
        self.width = 64
        self.height = 64

        self.color = color

        self.velocity = pygame.Vector2()
        self.vel = 5

        self.in_air = True

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.position.x, self.position.y, self.width, self.height))
    
    def update(self):
        self.position += self.velocity
        self.velocity.y += GRAVITY
        self.velocity.x = 0

        if self.position.x < 0:
            self.position.x = 0
        if self.position.x > WINDOW_WIDTH - self.width:
            self.position.x = WINDOW_WIDTH - self.width
    
    def reset(self):
        self.position.xy = WINDOW_WIDTH - 100, 200
        self.velocity.xy = 0, 0


    def jump(self):
        if not self.in_air:
            self.velocity.y = -17
            self.in_air = True
    
    def land(self):    
        self.velocity.y = 0
        self.in_air = False

    def move_left(self):
        self.velocity.x = -self.vel

    def move_right(self):
        self.velocity.x = self.vel
    
    def stop_moving(self):
        self.velocity.x = 0

