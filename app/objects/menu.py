from pygame import Surface, font, transform
from config import BLACK, MENU_WIDTH, MENU_HEIGHT, LIGHT_GREY, HIGHLIGHT_COLOR, MENU_ELEMENT_HEIGHT

from app import window

class Menu(Surface):
    font = font.Font(None, MENU_ELEMENT_HEIGHT)
    items = ["Удалить", "Повернуть", "Отразить"]
    visible = False
    position = (0, 0)
    selected_item = None
    hovered_item = None
    selected_road = None


    def __init__(self):
        super().__init__((MENU_WIDTH, MENU_HEIGHT))
        self.fill(LIGHT_GREY)


    def show(self, position, road):
        self.visible = True
        self.position = position
        self.selected_road = road


    def hide(self):
        self.visible = False
        self.selected_item = None
        self.selected_road = None
        self.hovered_item = None


    def draw(self):
        if self.visible:
            self.fill(LIGHT_GREY)
            for index, item in enumerate(self.items):
                color = HIGHLIGHT_COLOR if index == self.hovered_item else BLACK
                text = self.font.render(item, True, color)
                self.blit(text, (10, index * MENU_ELEMENT_HEIGHT))
            window.blit(self, self.position)


    def handle_action(self, action):
        if action == "Удалить":
            self.selected_road.kill()
        elif action == "Повернуть":
            self.selected_road.image = transform.rotate(self.selected_road.image, 90)
            self.selected_road.transforms.append(0)
        elif action == "Отразить":
            self.selected_road.image = transform.flip(self.selected_road.image, True, False)
            self.selected_road.transforms.append(1)
            



