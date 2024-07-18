import random
import torch
import numpy as np

import direction
from snake_ai import SnakeAI, SnakeAITrainer
from collections import deque


class Agent:
    def __init__(self, game, max_memory=100_000, exploration_initial_chances=80, batch_size=1000):
        self.game = game
        self.max_memory = max_memory
        self.batch_size = batch_size
        self.n_games = 0
        self.epsilon = 0
        self.gamma = 0.9
        self.exploration_initial_chances = exploration_initial_chances
        self.memory = deque(maxlen=self.max_memory)
        self.model = SnakeAI(15, 256, 3)
        self.trainer = SnakeAITrainer(self.model, lr=0.001, gamma=self.gamma)

    def train_long_memory(self):
        if len(self.memory) > self.batch_size:
            mini_sample = random.sample(self.memory, self.batch_size)
        else:
            mini_sample = self.memory

        states, actions, rewards, next_states, dones = zip(*mini_sample)
        self.trainer.train_step(states, actions, rewards, next_states, dones)

    def remember(self, state, action, reward, next_state, game_over):
        self.memory.append((state, action, reward, next_state, game_over))

    def train_short_memory(self, state, action, reward, next_state, done):
        self.trainer.train_step(state, action, reward, next_state, done)

    def get_state(self):
        head = self.game.snake.head_pos()
        posibility_l = [head[0] - 1, head[1] - 1]
        posibility_r = [head[0] + 1, head[1]]
        posibility_t = [head[0], head[1] - 1]
        posibility_b = [head[0], head[1] + 1]

        dir_l = self.game.snake.direction == direction.LEFT
        dir_r = self.game.snake.direction == direction.RIGHT
        dir_t = self.game.snake.direction == direction.TOP
        dir_b = self.game.snake.direction == direction.BOTTOM

        state = [
            # Danger straight
            (dir_l and self.game.snake.is_snake_body(posibility_l)) or
            (dir_r and self.game.snake.is_snake_body(posibility_r)) or
            (dir_t and self.game.snake.is_snake_body(posibility_t)) or
            (dir_b and self.game.snake.is_snake_body(posibility_b)),

            # Danger right
            (dir_l and self.game.snake.is_snake_body(posibility_t)) or
            (dir_r and self.game.snake.is_snake_body(posibility_b)) or
            (dir_t and self.game.snake.is_snake_body(posibility_r)) or
            (dir_b and self.game.snake.is_snake_body(posibility_l)),

            # Danger left
            (dir_l and self.game.snake.is_snake_body(posibility_b)) or
            (dir_r and self.game.snake.is_snake_body(posibility_t)) or
            (dir_t and self.game.snake.is_snake_body(posibility_l)) or
            (dir_b and self.game.snake.is_snake_body(posibility_r)),

            # Move direction
            dir_l,
            dir_r,
            dir_t,
            dir_b,

            # Food location
            self.game.food.position[0] < head[0],  # food left
            self.game.food.position[0] > head[0],  # food right
            self.game.food.position[1] < head[1],  # food up
            self.game.food.position[1] > head[1],  # food down

            self.game.food.position[0] - head[0],  # food left distance
            self.game.food.position[0] - head[0],  # food right distance
            self.game.food.position[1] - head[1],  # food up distance
            self.game.food.position[1] - head[1]  # food down distance
        ]

        return np.array(state, dtype=int)

    def get_action(self, state):
        # tradeoff: exploration & exploitation
        self.epsilon = self.exploration_initial_chances - self.n_games
        action = [0, 0, 0]
        if random.randint(0, 200) < self.epsilon:
            move = random.randint(0, 2)
            action[move] = 1
        else:
            t_state = torch.tensor(state, dtype=torch.float)
            prediction = self.model(t_state)
            move = torch.argmax(prediction).item()
            action[move] = 1

        return action
