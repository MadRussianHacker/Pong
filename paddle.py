#Copyright 2018 by Michał Gibas
import pygame

class Paddle:
    def __init__(self):
        self.x = 300.0
        self.y = 560.0
    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), (int(self.x), int(self.y), 150, 10))
    def move(self, x, y):
        self.x += x
        self.y += y