from settings import *


class Cell:
    """Playing field cell"""

    __CELL_SIZE = CELL_SIZE

    __CELL_ATTRIBUTES_ERROR = {
        'around_mines': {
            'type': int,
            'error': 'attribute "around_mines" must be int type'},
        'mine': {
            'type': bool,
            'error': 'attribute "mine" must be bool type'},
        'row': {
            'type': int,
            'error': 'attribute "row" must be int type'},
        'col': {
            'type': int,
            'error': 'attribute "col" must be int type'},
        'rect_coords': {
            'type': tuple,
            'error': 'attribute "rect_coords" must be tuple type'},
        'open': {
            'type': bool,
            'error': 'attribute "open" must be bool type'},
        'mark': {
            'type': bool,
            'error': 'attribute "mark" must be bool type'},
        }

    @classmethod
    def validation_of_types(cls, key: str, value):
        if isinstance(value, cls.__CELL_ATTRIBUTES_ERROR[key]['type']) is not True:
            raise TypeError(cls.__CELL_ATTRIBUTES_ERROR[key]['error'])

    @staticmethod
    def validation_of_values(key: str, value):
        if key == 'around_mines':
            if value < 0 or value >= 9:
                raise ValueError(f'"{key}" value must be between 0 and 8')
        if key == 'row' or key == 'col':
            if value < 0 or value >= AMOUNT_OF_CELLS:
                raise ValueError(f'"{key}" value must be between 0 and {AMOUNT_OF_CELLS - 1}')
        if key == 'rect_coords':
            if len(value) != 4:
                raise ValueError(f'The number of elements of the tuple must be 4')

    @classmethod
    def validation(cls, key: str, value):
        cls.validation_of_types(key, value)
        cls.validation_of_values(key, value)

    def __init__(self, around_mines: int, mine: bool, row: int, col: int):
        """
        Initialization of a cell, where
        around_mines -> number of mines around this cell
        mine -> the presence of a mine in this cell
        row -> the row of the playing field in which the cell is initialized
        col -> column of the playing field in which the cell is initialized
        rect_coords -> the coordinates of the rectangle that this cell belongs to on the map
        open -> cell open and closed flag
        mark -> cell marked and unmarked flag
        """

        self.validation('around_mines', around_mines)
        self.around_mines = around_mines

        self.validation('mine', mine)
        self.mine = mine

        self.validation('row', row)
        self.row = row

        self.validation('col', col)
        self.col = col

        self.rect_coords = (
            row * self.__CELL_SIZE,
            col * self.__CELL_SIZE,
            self.__CELL_SIZE,
            self.__CELL_SIZE
            )
        self.open = False
        self.mark = False

    def __setattr__(self, key, value):
        if key not in self.__CELL_ATTRIBUTES_ERROR.keys():
            raise AttributeError('It is forbidden to create new attributes of an object of class "Cell"')
        self.validation(key, value)
        object.__setattr__(self, key, value)
