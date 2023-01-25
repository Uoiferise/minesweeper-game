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

    def draw_cell(self, r_coords: tuple, rect_color, line_color, image_path: str = IMAGE_ERROR, around_mines=True):
        rect = pg.Rect(r_coords)
        pg.draw.rect(self.screen, rect_color, rect, 0)
        pg.draw.rect(self.screen, line_color, rect, 1)

        if around_mines:
            image = pg.image.load(image_path)
            image_rect = image.get_rect()
            image_rect.centerx = rect.centerx
            image_rect.centery = rect.centery
            self.screen.blit(image, image_rect)

    def draw_cell_with_number(self, cell):
        self.draw_cell(cell.rect_coords,
                       rect_color=RECT_COLOR,
                       line_color=LINE_COLOR,
                       image_path=number_images_dict.get(cell.around_mines, IMAGE_ERROR))

    def cell_mark_mine(self, cell):
        self.draw_cell(cell.rect_coords,
                       rect_color=RECT_COLOR_FLAG,
                       line_color=LINE_COLOR,
                       image_path=IMAGE_FLAG)

    def cell_remark_mine(self, cell):
        self.draw_cell(cell.rect_coords,
                       rect_color=SCR_FILL_COLOR,
                       line_color=LINE_COLOR,
                       image_path=IMAGE_ERROR,
                       around_mines=False)

    def draw_cell_correct_mark(self, cell):
        self.draw_cell(cell.rect_coords,
                       rect_color=RECT_COLOR_FLAG_CORRECT,
                       line_color=LINE_COLOR,
                       image_path=IMAGE_FLAG)

    def draw_mine(self, cell):
        self.draw_cell(cell.rect_coords,
                       rect_color=RECT_COLOR_MINE,
                       line_color=LINE_COLOR,
                       image_path=IMAGE_MINE)

    def draw_cell_zero_mine_around(self, cell):
        self.draw_cell(cell.rect_coords,
                       rect_color=RECT_COLOR,
                       line_color=LINE_COLOR,
                       around_mines=False)
