import direction

class Snake:
    def __init__(self, game):
        self.game = game
        self.is_alive = True
        # set body
        self.head = [game.map_dimentions[0], game.map_dimentions[1]]
        self.body = [(game.map_dimentions[0], game.map_dimentions[1]-1)]

    def kill(self):
        self.is_alive = False

    def __eated_self(self):
        pass

    def step(self, action):
        if self.is_alive:
            if action == direction.LEFT:
                x = self.head[0] - 1
                if x < 0:
                    self.kill()
                self.head[0] = x
            elif action == direction.TOP:
                y = self.head[1] - 1
                if y < 0:
                    self.kill()
                self.head[1] = y
            elif action == direction.RIGHT:
                x = self.head[0] + 1
                if x >= self.game.map_dimentions[0]:
                    self.kill()
                self.head[0] = x
            else:
                y = self.head[1] + 1
                if y >= self.game.map_dimentions[1]:
                    self.kill()
                self.head[1] = y
            self.__eated_self()

    def render(self):
        pass
