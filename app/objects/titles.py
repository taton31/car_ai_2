from pygame import Surface, draw
from config import GRID_SIZE, GRID_WIDTH, GRID_HEIGHT, LIGHT_GREY, BLACK

from app import window

class Titles(Surface):
    pos = (GRID_WIDTH * GRID_SIZE, 0)
    def __init__(self):
        super().__init__((GRID_SIZE, GRID_HEIGHT * GRID_SIZE))
        self.fill(LIGHT_GREY)
        draw.line(self, BLACK, (0, 0), (0, GRID_HEIGHT * GRID_SIZE), width=3)
        window.blit(self, self.pos)

    def draw(self):
        # self.fill(LIGHT_GREY)
        # draw.line(self, BLACK, (0, 0), (0, GRID_HEIGHT * GRID_SIZE), width=3)
        window.blit(self, self.pos)

    



