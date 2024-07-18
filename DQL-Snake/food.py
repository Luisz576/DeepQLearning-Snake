import random
import colors
import pygame


class Food:
    def __init__(self, game):
        self.game = game
        self.position = []

        self.reset()

    def reset(self):
        self.position = self._random_position()

    def was_eaten(self, pos):
        return self.position[0] == pos[0] and self.position[1] == pos[1]

    def _random_position(self):
        new_position = [random.randint(0, self.game.map_dimentions[0]-1),
                        random.randint(0, self.game.map_dimentions[1]-1)]
        while not self.game.is_space_free_for_food(new_position):
            new_position = [random.randint(0, self.game.map_dimentions[0]-1),
                            random.randint(0, self.game.map_dimentions[1]-1)]
        return new_position

    def update(self):
        pass

    def eat(self):
        self.position = self._random_position()

    def render(self):
        pygame.draw.rect(self.game.screen, colors.RED, pygame.Rect(self.position[0] * self.game.pixel_resolution,
                                                                   self.position[1] * self.game.pixel_resolution,
                                                                   self.game.pixel_resolution,
                                                                   self.game.pixel_resolution))
