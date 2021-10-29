import pygame
from utils.settings import *

class Button:
    def __init__(self, x, y, text, size, color=RED):
        self.position = pygame.Vector2()
        self.position.xy = x, y

        self.text = text
        self.text_size = size
        self.text_surf = font.render(self.text, True, self.text_size)
        self.text_rect = self.text_surf.get_rect()
        self.width, self.height = self.text_rect.width, self.text_rect.height

        self.color = color
        self.released_color = color
        self.pressed_color = [c - 100 for c in color]
        for i in range(len(self.pressed_color)):
            if self.pressed_color[i] < 0:
                self.pressed_color[i] = 0
    
    def draw(self, win):
        regex = 5
        rect = (self.position.x - regex, self.position.y - regex, self.width + 2*regex, self.height + 2*regex)
        curv = min(self.width, self.height) // 6
        pygame.draw.rect(win, self.color, rect, 0, curv)
        win.blit(self.text_surf, self.text_rect)

    def press(self):
        self.color = self.pressed_color
    
    def release(self):
        self.color = self.released_color

    def is_pressed(self):
        return self.color == self.pressed_color

    def is_inside(self, x, y):
        if x > self.position.x and x < self.position.x + self.width:
            if y > self.position.y and y < self.position.y + self.height:
                return True

    def set_center(self, x, y):
        self.position.x = x - self.width // 2
        self.position.y = y - self.height // 2
        self.text_rect.center = x, y