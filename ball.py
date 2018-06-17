#Copyright 2018 by Michał Gibas

import pygame, random, sys

class Ball:
    def __init__(self):
        self.x = 380.0
        self.y = 280.0
        self.radius = 20
        self.velocityX = 0.0
        self.velocityY = 0.0
        self.speed = 150.0
    def draw(self, window):
        pygame.draw.circle(window, (255, 255, 255), (int(self.x), int(self.y)), self.radius, 0)
    def update(self, deltaTime, player):
        if self.velocityX == 0 and self.velocityY == 0:
            direction = random.randint(0, 3)
            if direction == 1:
                self.velocityX = -self.speed
                self.velocityY = self.speed
            if direction == 2:
                self.velocityY = self.speed
            if direction == 3:
                self.velocityX = self.speed
                self.velocityY = self.speed
        self._check_bounds(player)
        self.x += self.velocityX*deltaTime
        self.y += self.velocityY*deltaTime
        if (self.y+self.radius) >= 600:
            print("You lost!")
            pygame.quit()
            sys.exit()

    def _check_bounds(self, player):
        if (self.x-self.radius) <= 0:
            self.velocityX = -self.velocityX
        if (self.x+self.radius) >= 800:
            self.velocityX = -self.velocityX
        if (self.y-self.radius) <= 0:
            self.velocityY = -self.velocityY
        if (self.y+self.radius) >= 560:
            if ((self.x+self.radius) >= player.x) and ((self.x-self.radius) <= player.x+150):
                self.velocityY = -self.velocityY

        