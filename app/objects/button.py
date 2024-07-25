from pygame import Surface, font
from config import BLACK, MENU_WIDTH, MENU_HEIGHT, LIGHT_GREY, HIGHLIGHT_COLOR, MENU_ELEMENT_HEIGHT, WINDOW_SIZE, GRID_SIZE

from app import window, map, RoadBlock

class Buttons(Surface):
    pos = (0, 0)
    font = font.Font(None, MENU_ELEMENT_HEIGHT)
    items = ["Сохр трэк", "Загр трэк"]
    position = (WINDOW_SIZE[0] - GRID_SIZE, WINDOW_SIZE[1] - MENU_HEIGHT)
    selected_road = None


    def __init__(self):
        super().__init__((MENU_WIDTH, MENU_HEIGHT))
        
        self.fill(LIGHT_GREY)


    def draw(self):
        self.fill(LIGHT_GREY)
        for index, item in enumerate(self.items):
            color = BLACK
            text = self.font.render(item, True, color)
            self.blit(text, (10, index * MENU_ELEMENT_HEIGHT))
        window.blit(self, self.position)


    def handle_action(self, action):
        if action == "Сохр трэк":
            map.save()
        elif action == "Загр трэк":
            map.load(RoadBlock)


