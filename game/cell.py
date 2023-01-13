from settings import CELL_SIZE


class Cell:
    """Playing field cell"""

    __size_of_cell = CELL_SIZE

    def __init__(self, around_mines, mine, row, col):
        self.around_mines = around_mines
        self.mine = mine
        self.row = row
        self.col = col
        self.rect_coords = (
            row * CELL_SIZE,
            col * CELL_SIZE,
            CELL_SIZE,
            CELL_SIZE
        )
        self.open = False
