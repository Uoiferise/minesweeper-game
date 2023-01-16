# game settings
GAME_TITLE = 'Minesweeper game'.upper()
RES = WIDTH, HEIGHT = 800, 800

AMOUNT_OF_CELLS = 10
AMOUNT_OF_MINES = 12

CELL_SIZE = WIDTH / AMOUNT_OF_CELLS
LINE_WIGHT = 3

LINE_COLOR = (50, 50, 50)
RECT_COLOR = (150, 150, 150)
RECT_COLOR_FLAG = (249, 199, 79)
RECT_COLOR_MINE = (239, 35, 60)
SCR_FILL_COLOR = (0, 0, 0)

number_images_dict = {
    0: 'images/number_0.png',
    1: 'images/number_1.png',
    2: 'images/number_2.png',
    3: 'images/number_3.png',
    4: 'images/number_4.png',
    5: 'images/number_5.png',
    6: 'images/number_6.png',
    7: 'images/number_7.png',
    8: 'images/number_8.png',

}
IMAGE_MINE = 'images/mine.png'
IMAGE_ERROR = 'images/error.png'
IMAGE_FLAG = 'images/flag.png'

# game control
LEFT_MB = 1
RIGHT_MB = 3
