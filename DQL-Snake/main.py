from game import Game
from agent import Agent

game = Game()
agent = Agent(game)

while True:
    old_state = agent.get_state()

    action = agent.get_action(old_state)

    reward, done, score = game.step_loop(action)
