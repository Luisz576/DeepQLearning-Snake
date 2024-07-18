import pygame.draw

import colors
import direction


class Snake:
    def __init__(self, game, full_power=100):
        self.game = game
        self.is_alive = True
        self.full_power = full_power
        self.direction = direction.LEFT
        self.body = []
        self.last_tail_position = []
        self.power = self.full_power

        self.reset()

    def kill(self):
        self.is_alive = False

    def __eated_self(self):
        if self.is_snake_body(self.head_pos(), verify_head=False):
            self.kill()

    def reset(self):
        self.body = [[self.game.map_dimentions[0] / 2, self.game.map_dimentions[1] / 2],
                     [self.game.map_dimentions[0] / 2, self.game.map_dimentions[1] / 2 - 1]]
        self.last_tail_position = [self.game.map_dimentions[0] / 2, self.game.map_dimentions[1] / 2 - 1]
        self.is_alive = True
        self.refull_power()

    def refull_power(self):
        self.power = self.full_power

    def is_snake_body(self, position, verify_head=True):
        a = len(self.body)
        b = len(self.body)
        if not verify_head:
            a -= 1
        for i in range(a):
            if self.body[b-i-1][0] == position[0] and self.body[b-i-1][1] == position[1]:
                return True
        return False

    def step(self, action):
        if self.is_alive:
            if action[0]:
                self.direction = direction.new_direction_based_on_turn_left_or_right(self.direction, True)
            elif action[1]:
                self.direction = direction.new_direction_based_on_turn_left_or_right(self.direction, False)

    def update(self):
        if self.is_alive:
            self.__move_body()
            self.__eated_self()
            self.power -= 1
            if self.power < 0:
                self.kill()

    def __move_body(self):
        last_body_index = len(self.body) - 1

        self.last_tail_position = [self.body[last_body_index][0], self.body[last_body_index][1]]
        for i in range(last_body_index):
            self.body[last_body_index - i] = [self.body[last_body_index - i - 1][0],
                                              self.body[last_body_index - i - 1][1]]

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

    def eat(self):
        self.body.append([self.last_tail_position[0], self.last_tail_position[1]])
        self.refull_power()

    def head_pos(self):
        return self.body[0]

    def render(self):
        for i in range(len(self.body)):
            pygame.draw.rect(self.game.screen, colors.GREEN, pygame.Rect(self.body[i][0] * self.game.pixel_resolution,
                                                                         self.body[i][1] * self.game.pixel_resolution,
                                                                         self.game.pixel_resolution,
                                                                         self.game.pixel_resolution))
