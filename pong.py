#Copyright 2018 by Michał Gibas

from paddle import Paddle
from ball import Ball
import pygame, sys, time

class Game:
    def __init__(self):
        pygame.init()
        self._window = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pong")
        self.deltaTime = 0.0
        self.player = Paddle()
        self.ball = Ball()
    def run(self):
        while True:
            start = time.time()
            self.handle_events()
            self.update()
            self.render()
            end = time.time()
            self.deltaTime = end - start
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move(-self.deltaTime*250.0, 0.0)
        elif keys[pygame.K_RIGHT]:
            self.player.move(self.deltaTime*250.0, 0.0)
        self.ball.update(self.deltaTime, self.player)

    def render(self):
        self._window.fill((0,0,0))
        self.player.draw(self._window)
        self.ball.draw(self._window)
        pygame.display.update()
        

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

game = Game()
game.run()