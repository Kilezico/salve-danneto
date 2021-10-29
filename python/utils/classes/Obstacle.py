from utils.classes.Heitor import Heitor
from utils.settings import *
import pygame

class Obstacle:
    def __init__(self, x, y, w, h, color=BLACK):
        self.position = pygame.Vector2()
        self.position.xy = x, y
        self.width = w
        self.height = h
        self.color = color

        
        self.last_player_state = tuple()

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.position.x, self.position.y, self.width, self.height))
    
    def update(self, h: Heitor):
        player_state = (
            h.position.x + h.width < self.position.x,  # Left
            h.position.y + h.height < self.position.y,  # Up
            h.position.y > self.position.y + self.height,  # Down
            h.position.x > self.position.x + self.width)  # Right
        
        if not any(player_state):  # Colidindo
            if self.last_player_state[0]:  # Left
                h.position.x = self.position.x - h.width
                h.stop_moving()
            elif self.last_player_state[1]:  # Up
                h.position.y = self.position.y - h.height
                h.land()
            elif self.last_player_state[2]:  # Down
                h.position.y = self.position.y + self.height + 1
                h.velocity.y = 0
            elif self.last_player_state[3]:  # Right
                h.position.x = self.position.x + self.width
                h.stop_moving()
        else:  # Não colidindo
            self.last_player_state = player_state
