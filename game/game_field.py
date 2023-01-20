from cell import Cell
from random import randint
from settings import *


class GameField:
    """Playing field filled with cells (matrix representation)"""

    def __init__(self, n: int, m: int, game):
        """
        Initialization of a field of given sizes, where
        n -> amount of cells horizontally and vertically
        m -> amount of mines on the playing field
        game -> the class Game session for which the playing field is being initialized
        """

        self.N = n    # amount of rows and columns in matrix
        self.M = m    # amount of mines on playing field
        self.game = game
        self.field = [[Cell(0, False, row, col) for col in range(self.N)] for row in range(self.N)]

        self.mines = self.generate_random_mines(self.N, self.M)

        for cell in self.mines:
            row, col = cell
            self.field[row][col].mine = True

        for row in range(self.N):
            for col in range(self.N):
                self.field[row][col].around_mines = self.sum_around_mines(row, col)

    @staticmethod
    def generate_random_mines(n: int, m: int) -> set:
        mines = set()
        while len(mines) < m:
            mine_cell = (randint(0, n-1), randint(0, n-1))
            mines.add(mine_cell)
        return mines

    def sum_around_mines(self, r: int, c: int) -> int:
        total_around_mines = 0
        for row in range(r-1, r+2):
            if row == -1 or row > self.N-1:
                continue
            for col in range(c-1, c+2):
                if col == -1 or col > self.N-1:
                    continue
                if row == r and col == c:
                    continue
                total_around_mines += int(self.field[row][col].mine)
        if total_around_mines < 0 or total_around_mines >= 9:
            raise ValueError('total_around_mines must be between 0 and 8')
        return total_around_mines

    def try_to_open_cell(self, cell):
        if cell.mine:
            self.game.map.draw_mine(cell)
            self.open_all_cell()
        elif cell.around_mines == 0:
            self.game.map.draw_cell_zero_mine_around(cell)
            self.open_around_cells(cell)
        else:
            self.game.map.draw_cell_with_number(cell)

    def check_coords(self, pos: tuple, click: int):
        row = int(pos[0] // CELL_SIZE)
        col = int(pos[1] // CELL_SIZE)
        cell = self.field[row][col]

        if click == LEFT_MB:
            if cell.open is not True:
                self.try_to_open_cell(cell)
                cell.open = True
        elif click == RIGHT_MB:
            if cell.open is not True:
                if cell.mark:
                    self.game.map.cell_remark_mine(cell)
                    cell.mark = False
                    self.check_win_game()
                else:
                    self.game.map.cell_mark_mine(cell)
                    cell.mark = True
                    self.check_win_game()

    def open_cell(self, cell):
        if cell.open is not True:
            cell.open = True
            if cell.around_mines == 0:
                self.game.map.draw_cell_zero_mine_around(cell)
                self.open_around_cells(cell)
            else:
                self.game.map.draw_cell_with_number(cell)

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

    def open_all_cell(self):
        for row in range(self.N):
            for col in range(self.N):
                cell = self.field[row][col]
                if cell.mine:
                    if cell.mark:
                        self.game.map.draw_cell_correct_mark(cell)
                    else:
                        self.game.map.draw_mine(cell)
                else:
                    self.open_cell(cell)

    def check_win_game(self):
        total_score = 0
        for row in range(self.N):
            for col in range(self.N):
                cell = self.field[row][col]
                if cell.mine is not True:
                    if cell.mark:
                        total_score = -1
                        break
                else:
                    if cell.mark:
                        total_score += 1
            if total_score == -1:
                break

        if total_score == self.M:
            self.open_all_cell()
