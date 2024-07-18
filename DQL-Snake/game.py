import pygame
from snake import Snake
from food import Food
import colors


class Game:
    def __init__(self, title="DQL-Snake", map_dimentions=(30, 30), pixel_resolution=20, clock_tick=10):
        pygame.init()
        pygame.display.set_caption(title)
        self.clock_tick = clock_tick
        self.pixel_resolution = pixel_resolution
        self.map_dimentions = map_dimentions
        self.screen = pygame.display.set_mode((self.map_dimentions[0] * self.pixel_resolution,
                                               self.map_dimentions[1] * self.pixel_resolution))
        self.clock = pygame.time.Clock()
        self.snake = Snake(self)
        self.food = Food(self)

    def is_space_free_for_food(self, position):
        if self.snake.body[0][0] == position[0] or self.snake.body[0][1] == position[1]:
            return False
        return not self.snake.is_snake_body(position)

    def step_loop(self, action):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        self.snake.step(action)

        ###
        self.update()
        self.render()

        self.clock.tick(self.clock_tick)

    def update(self):
        self.snake.update()

    def render(self):
        self.screen.fill(colors.BLACK)

        self.snake.render()
        self.food.render()

        pygame.display.flip()
