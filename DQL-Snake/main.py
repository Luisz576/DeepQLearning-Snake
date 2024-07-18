from game import Game
from agent import Agent

game = Game()
agent = Agent(game)

record = -1

while True:
    old_state = agent.get_state()
    action = agent.get_action(old_state)
    reward, done, score = game.step_loop(action)
    new_state = agent.get_state()

    agent.train_short_memory(old_state, action, reward, new_state, done)
    agent.remember(old_state, action, reward, new_state, done)

    if done:
        game.reset()
        agent.n_games += 1
        agent.train_long_memory()

        if score > record:
            record = score
            print("====> New Record: ", score, "<====")

        print("Game", agent.n_games, "- Score: ", score)
