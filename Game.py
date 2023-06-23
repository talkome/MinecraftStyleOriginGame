from ursina import Ursina
from Player import Player
from Sky import Sky
from World import World


class Game:
    def __init__(self):
        self.app = Ursina()
        self.world = World()
        self.player = Player()
        self.sky = Sky()
        self.app.run()


if __name__ == '__main__':
    new_game = Game()
