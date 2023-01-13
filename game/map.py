import pygame as pg
from cell import Cell
from random import randint
from settings import *


class GameField:
    """Playing field filled with cells (matrix representation)"""

    def __init__(self, n: int, m: int, game):
        """
        Initialization of a field of given sizes, where
        n -> amount of cells horizontally and vertically
        m -> amount of mines on the playing field.
        """

        self.N = n    # amount of rows and cols
        self.M = m    # amount of mines
        self.game = game
        self.field = [[Cell(0, False, row, col) for col in range(self.N)] for row in range(self.N)]

        mines = self.generate_random_mines(self.N, self.M)

        for cell in mines:
            row, col = cell
            self.field[row][col].mine = True

        for row in range(self.N):
            for col in range(self.N):
                self.field[row][col].around_mines = self.sum_around_mines(row, col)

    @staticmethod
    def generate_random_mines(n, m):
        result = []
        while len(result) < m:
            mine_cell = (randint(0, n-1), randint(0, n-1))
            if mine_cell not in result:
                result.append(mine_cell)
        return result

    def sum_around_mines(self, r, c):
        total_around_mines = 0
        for row in range(r-1, r+2):
            if row == -1 or row > self.N-1:
                continue
            for col in range(c-1, c+2):
                if col == -1 or col > self.N-1:
                    continue
                if row == r and col == c:
                    continue
                total_around_mines += self.field[row][col].mine
        return total_around_mines

    def check_coords(self, pos: tuple, click: int):
        row = int(pos[0] // CELL_SIZE)
        col = int(pos[1] // CELL_SIZE)
        cell = self.field[row][col]
        if cell.open is not True:
            if click == 1:
                cell.open = True
                self.try_to_open_cell(cell)
            elif click == 3:
                cell.open = True
                self.cell_mark_mine(cell)

    def try_to_open_cell(self, cell):
        if cell.mine:
            self.game.new_game()
        elif cell.around_mines == 0:
            self.game.map.draw_cell(cell.rect_coords,
                                    around_mines=False)
            self.open_around_cells(cell)
        else:
            self.game.map.draw_cell(cell.rect_coords,
                                    image_path=number_images_dict.get(cell.around_mines,
                                                                      IMAGE_ERROR))

    def open_cell(self, cell):
        if cell.open is not True:
            cell.open = True
            if cell.around_mines == 0:
                self.game.map.draw_cell(cell.rect_coords,
                                        around_mines=False)
                self.open_around_cells(cell)
            else:
                self.game.map.draw_cell(cell.rect_coords,
                                        image_path=number_images_dict.get(cell.around_mines,
                                                                          IMAGE_ERROR))

    def open_around_cells(self, cell):
        for row in range(cell.row - 1, cell.row + 2):
            if row == -1 or row > self.N - 1:
                continue
            for col in range(cell.col - 1, cell.col + 2):
                if col == -1 or col > self.N - 1:
                    continue
                if row == cell.row and col == cell.col:
                    continue
                self.open_cell(self.field[row][col])

    def cell_mark_mine(self, cell):
        rect_coords = (
            cell.row * CELL_SIZE,
            cell.col * CELL_SIZE,
            CELL_SIZE,
            CELL_SIZE
        )
        self.game.map.draw_cell(rect_coords,
                                image_path=IMAGE_MINE)


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
                         width=3)

            pg.draw.line(self.screen,
                         LINE_COLOR,
                         (0, i * CELL_SIZE),
                         (WIDTH, i * CELL_SIZE),
                         width=3)

    def draw_field(self):
        self.screen.fill(SCR_FILL_COLOR)
        self.draw_map_net()

    def draw_cell(self, r_coords, image_path=IMAGE_ERROR, around_mines=True):
        rect = pg.Rect(r_coords)
        pg.draw.rect(self.screen, RECT_COLOR, rect, 0)

        if around_mines:
            image = pg.image.load(image_path)
            image_rect = image.get_rect()
            image_rect.centerx = rect.centerx
            image_rect.centery = rect.centery
            self.screen.blit(image, image_rect)
