DEBUG = False

ROAD_IMAGES = ['a0.png', 'a1.png', 'a2.png', 'a3.png', 'a4.png', 'a5.png']
PATH_ROAD_IMAGES = 'app/source/title_road/'
CAR_IMAGE = 'app/source/car.png'
PATH_SAVED_MAP = 'app/saved_map/map.txt'

PATH_NEAT_CONFIG = 'config.txt'

GRID_SIZE = 128
GRID_WIDTH = 10
GRID_HEIGHT = 7
WINDOW_SIZE = (GRID_SIZE * (GRID_WIDTH + 1), GRID_SIZE * GRID_HEIGHT)
IMAGE_POSITION_X = WINDOW_SIZE[0] - GRID_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GREY = (199, 199, 199)
HIGHLIGHT_COLOR = (100, 100, 255)


MENU_WIDTH = 150
MENU_HEIGHT = 100
MENU_ELEMENT_HEIGHT = 30

VECTORS_LEN = 250

CARS_NUMBER = 50
MAX_FITNESS = 50