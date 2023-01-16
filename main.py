import pygame as pg
import sys
from tests import run_tests
from map import GameField, Map
from settings import *


class Game:
    """Description will be later ... maybe"""

    # __NEW_GAME = None
    #
    # def __new__(cls, *args, **kwargs):
    #     if cls.__NEW_GAME is None:
    #         cls.__NEW_GAME = super().__new__(cls)
    #     return cls.__NEW_GAME

    def __init__(self):
        pg.init()
        pg.display.set_caption(GAME_TITLE)
        self.screen = pg.display.set_mode(RES)
        self.map = Map(self.screen)
        self.map.draw_field()
        self.game = GameField(AMOUNT_OF_CELLS, AMOUNT_OF_MINES, self)

    def new_game(self):
        self.map.draw_field()
        self.game = GameField(AMOUNT_OF_CELLS, AMOUNT_OF_MINES, self)

    @staticmethod
    def update():
        pg.display.update()

    @staticmethod
    def end_game():
        pg.quit()
        sys.exit()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.end_game()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == LEFT_MB:
                    self.game.check_coords(event.pos, event.button)
                if event.button == RIGHT_MB:
                    self.game.check_coords(event.pos, event.button)

    def run(self):
        while True:
            self.check_events()
            self.update()


def main():
    # run_tests()
    game = Game()
    game.run()


if __name__ == '__main__':
    main()
