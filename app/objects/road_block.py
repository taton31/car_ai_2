from pygame import sprite, image
from config import ROAD_IMAGES, PATH_ROAD_IMAGES, GRID_SIZE, GRID_WIDTH
from app import group_roads

loaded_images = [image.load(PATH_ROAD_IMAGES + img) for img in ROAD_IMAGES]

class RoadBlock(sprite.Sprite):
    # pos  - int (number of col and row)
    dragging_image = None
    dragging_offset = (0, 0)
    selected_image = None
    type = None

    was_moved = False


    def __init__(self, type, pos):
        super().__init__()
        self.type = type
        self.image = loaded_images[type]
        self.init_pos = pos
        self.rect = self.image.get_rect()
        self.rect.x = GRID_WIDTH * GRID_SIZE
        self.rect.y = self.init_pos[1] * GRID_SIZE
        group_roads.add(self)

    def check_click(self, mouse):
        return self.rect.collidepoint(mouse)
    
    def move(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.was_moved = True

    def copy(self):
        if not self.was_moved:
            RoadBlock(self.type, self.init_pos)
            print(1)
        
        # titles.blit(self.image, self.pos)

    # def blit(self):
    #     if self.on_grid:
    #         grid.blit(self.image, self.pos)
    #     else:
    #         titles.blit(self.image, self.pos)
            

    # image_positions = []
    # for i in range(len(images)):
    #     image_positions += [(IMAGE_POSITION_X, GRID_SIZE * i)]
    # dragging_image = None
    # dragging_offset = (0, 0)
    # selected_image = None
    # def __init__():


