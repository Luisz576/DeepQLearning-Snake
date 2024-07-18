import pygame.draw

import colors
import direction


class Snake:
    def __init__(self, game):
        self.game = game
        self.is_alive = True
        self.direction = direction.LEFT
        # set body
        self.body = [[game.map_dimentions[0], game.map_dimentions[1]],
                     [game.map_dimentions[0], game.map_dimentions[1]-1]]
        self.body = [[2, 2], [0, 1], [0, 2]]

    def kill(self):
        self.is_alive = False

    def __eated_self(self):
        pass

    def is_snake_body(self, position):
        for i in range(len(self.body)):
            if self.body[i][0] == position[0] and self.body[i][1] == position[1]:
                return True
        return False

    def step(self, action):
        if self.is_alive:
            if action[0]:
                self.direction = direction.new_direction_based_on_turn_left_or_right(self.direction, True)
            elif action[1]:
                self.direction = direction.new_direction_based_on_turn_left_or_right(self.direction, False)

    def update(self):
        for i in range(len(self.body) - 1):
            self.body[i+1][0] = self.body[i][0]
            self.body[i+1][1] = self.body[i][1]

        if self.is_alive:
            if self.direction == direction.LEFT:
                x = self.body[0][0] - 1
                if x < 0:
                    self.kill()
                self.body[0][0] = x
            elif self.direction == direction.TOP:
                y = self.body[0][1] - 1
                if y < 0:
                    self.kill()
                self.body[0][1] = y
            elif self.direction == direction.RIGHT:
                x = self.body[0][0] + 1
                if x >= self.game.map_dimentions[0]:
                    self.kill()
                self.body[0][0] = x
            else:
                y = self.body[0][1] + 1
                if y >= self.game.map_dimentions[1]:
                    self.kill()
                self.body[0][1] = y

            self.__eated_self()

    def render(self):
        for i in range(len(self.body)):
            pygame.draw.rect(self.game.screen, colors.GREEN, pygame.Rect(self.body[i][0] * self.game.pixel_resolution,
                                                                         self.body[i][1] * self.game.pixel_resolution,
                                                                         self.game.pixel_resolution,
                                                                         self.game.pixel_resolution))
