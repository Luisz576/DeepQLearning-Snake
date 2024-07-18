import random

import torch

from snake_ai import SnakeAI, SnakeAITrainer
from collections import deque


class Agent:
    def __init__(self, game, max_memory=100_000, exploration_initial_chances=80):
        self.game = game
        self.max_memory = max_memory
        self.n_games = 0
        self.epsilon = 0
        self.gamma = 0.9
        self.exploration_initial_chances = exploration_initial_chances
        self.memory = deque(maxlen=self.max_memory)
        self.model = SnakeAI(11, 256, 3)
        self.trainer = SnakeAITrainer(self.model, lr=0.001, gamma=self.gamma)

    def get_state(self):
        return [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

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
