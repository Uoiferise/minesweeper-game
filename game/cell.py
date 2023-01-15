from settings import CELL_SIZE


class Cell:
    """Playing field cell"""

    __CELL_SIZE = CELL_SIZE

    __CELL_ATTRIBUTES_ERROR = {
        'around_mines': (int, 'attribute "around_mines" must be int type'),
        'mine': (bool, 'attribute "mine" must be bool type'),
        'row': (int, 'attribute "row" must be int type'),
        'col': (int, 'attribute "col" must be int type'),
        'rect_coords': (tuple, 'attribute "rect_coords" must be tuple type'),
        'open': (bool, 'attribute "open" must be bool type'),
        }

    @classmethod
    def validation_of_types(cls, around_mines: int, mine: bool, row: int, col: int):
        if isinstance(around_mines, cls.__CELL_ATTRIBUTES_ERROR['around_mines'][0]) is not True:
            raise TypeError(cls.__CELL_ATTRIBUTES_ERROR['around_mines'][1])
        if isinstance(mine, cls.__CELL_ATTRIBUTES_ERROR['mine'][0]) is not True:
            raise TypeError(cls.__CELL_ATTRIBUTES_ERROR['mine'][1])
        if isinstance(row, cls.__CELL_ATTRIBUTES_ERROR['row'][0]) is not True:
            raise TypeError(cls.__CELL_ATTRIBUTES_ERROR['row'][1])
        if isinstance(col, cls.__CELL_ATTRIBUTES_ERROR['col'][0]) is not True:
            raise TypeError(cls.__CELL_ATTRIBUTES_ERROR['col'][1])

    def __init__(self, around_mines: int, mine: bool, row: int, col: int):
        self.validation_of_types(around_mines, mine, row, col)

        self.around_mines = around_mines
        self.mine = mine
        self.row = row
        self.col = col
        self.rect_coords = (
            row * self.__CELL_SIZE,
            col * self.__CELL_SIZE,
            self.__CELL_SIZE,
            self.__CELL_SIZE
        )
        self.open = False

    def __setattr__(self, key, value):
        if key not in self.__CELL_ATTRIBUTES_ERROR.keys():
            raise AttributeError('It is forbidden to create new attributes of an object of class "Cell"')
        if isinstance(value, self.__CELL_ATTRIBUTES_ERROR[key][0]) is not True:
            print(key, self.__CELL_ATTRIBUTES_ERROR[key][0], value)
        object.__setattr__(self, key, value)
