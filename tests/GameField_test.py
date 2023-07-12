import unittest

from game import GameField
from game.settings import AMOUNT_OF_CELLS, AMOUNT_OF_MINES


class GameFieldTest(unittest.TestCase):

    def amount_of_mines(self):
        test_field = GameField(AMOUNT_OF_CELLS, AMOUNT_OF_MINES, None)
        total_mines = 0
        for row in range(test_field.N):
            for col in range(test_field.N):
                cell = test_field.field[row][col]
                total_mines += cell.mine
                if cell.row != row or cell.col != col:
                    raise ValueError('Cell was assigned an invalid row or column index')

        self.assertEqual(total_mines, AMOUNT_OF_MINES)


if __name__ == '__main__':
    unittest.main()
