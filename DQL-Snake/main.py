import pygame
from snake import Snake
import colors

class Game:
    def __init__(self, title="DQL-Snake", map_dimentions=(10, 10)):
        pygame.init()
        pygame.display.set_caption(title)
        self.map_dimentions = map_dimentions
        self.screen = pygame.display.set_mode(self.map_dimentions)
        self.snake = Snake(self)

    def step(self):
        pass

    def render(self):
        self.screen.fill(colors.BLACK)
        self.snake.render()
