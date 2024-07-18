import pygame
from snake import Snake
from food import Food
import colors


DEATH_REWARD = -10
EAT_REWARD = 10
NOTHING_REWARD = 0


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
        self.score = 0

        self.reset()

    def reset(self):
        self.snake.reset()
        self.food.reset()
        self.score = 0

    def is_space_free_for_food(self, position):
        if self.snake.head_pos()[0] == position[0] or self.snake.head_pos()[1] == position[1]:
            return False
        return not self.snake.is_snake_body(position)

    def step_loop(self, action):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        self.snake.step(action)
        self.update()

        game_over = False
        reward = NOTHING_REWARD

        if not self.snake.is_alive or self.snake.power <= 0:
            game_over = True
            reward = DEATH_REWARD
            return reward, game_over, self.score

        if self.food.was_eaten(self.snake.head_pos()):
            reward = EAT_REWARD
            self.score += 1
            self.snake.eat()
            self.food.eat()

        self.render()

        self.clock.tick(self.clock_tick)

        return reward, game_over, self.score

    def update(self):
        self.snake.update()

    def render(self):
        self.screen.fill(colors.BLACK)

        self.snake.render()
        self.food.render()

        pygame.display.flip()
