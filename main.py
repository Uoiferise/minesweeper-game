import pygame as pg
import sys
from map import Map
from game_field import GameField
from settings import *


class Game:
    """Description will be later ... maybe"""

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
            if event.type == pg.QUIT:
                self.end_game()

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button in (LEFT_MB, RIGHT_MB):
                    self.game.check_coords(event.pos, event.button)

            if event.type == pg.KEYDOWN:
                if pg.key.get_pressed()[pg.K_SPACE]:
                    self.new_game()

    def run(self):
        while True:
            self.check_events()
            self.update()


def main():
    game = Game()
    game.run()


if __name__ == '__main__':
    main()
