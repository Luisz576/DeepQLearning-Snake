import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as f


class SnakeAI(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        self.in_layer = nn.Linear(input_size, hidden_size)
        self.out_layer = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        y = f.relu(self.in_layer(x))
        y = self.out_layer(y)
        return y


class SnakeAITrainer:
    def __init__(self, model, lr, gamma):
        self.lr = lr
        self.gamma = gamma
        self.model = model
        self.optimizer = optim.Adam(model.parameters(), lr=self.lr)
        self.criterion = nn.MSELoss()
