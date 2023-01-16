import pygame as pg
from settings import *


class Map:
    """Playing map filled with cells (drawing matrix cells into 2D objects)"""

    def __init__(self, screen):
        self.screen = screen

    def draw_map_net(self):
        for i in range(1, AMOUNT_OF_CELLS):
            pg.draw.line(self.screen,
                         LINE_COLOR,
                         (i * CELL_SIZE, 0),
                         (i * CELL_SIZE, HEIGHT),
                         width=LINE_WIGHT)

            pg.draw.line(self.screen,
                         LINE_COLOR,
                         (0, i * CELL_SIZE),
                         (WIDTH, i * CELL_SIZE),
                         width=LINE_WIGHT)

    def draw_field(self):
        self.screen.fill(SCR_FILL_COLOR)
        self.draw_map_net()

    def draw_cell(self, r_coords: tuple, image_path: str = IMAGE_ERROR, around_mines=True):
        rect = pg.Rect(r_coords)
        pg.draw.rect(self.screen, RECT_COLOR, rect, 0)

        if around_mines:
            image = pg.image.load(image_path)
            image_rect = image.get_rect()
            image_rect.centerx = rect.centerx
            image_rect.centery = rect.centery
            self.screen.blit(image, image_rect)
