from pygame import Surface, Rect, draw
from config import GRID_SIZE, GRID_WIDTH, GRID_HEIGHT, BLACK, WHITE, LIGHT_GREY

from app import window

class Grid(Surface):
    pos = (0, 0)
    def __init__(self):
        super().__init__((GRID_WIDTH * GRID_SIZE, GRID_HEIGHT * GRID_SIZE))
        self.fill(LIGHT_GREY)
        for x in range(0, GRID_WIDTH):
            for y in range(0, GRID_HEIGHT):
                rect = Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
                draw.rect(self, BLACK, rect, 1)
        window.blit(self, self.pos)

    def draw(self):
        window.blit(self, self.pos)

    



