from game_field import GameField
from settings import *


def run_tests():
    # tests for class GameField
    test_field = GameField(AMOUNT_OF_CELLS, AMOUNT_OF_MINES, None)
    total_mines = 0
    for row in range(test_field.N):
        for col in range(test_field.N):
            cell = test_field.field[row][col]
            total_mines += cell.mine
            if cell.row != row or cell.col != col:
                raise ValueError('Cell was assigned an invalid row or column index')
    if total_mines != AMOUNT_OF_MINES:
        raise ValueError('Incorrect number of mines on the playing field')
