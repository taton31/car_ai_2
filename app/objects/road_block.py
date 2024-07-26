from pygame import sprite, image, transform
from config import ROAD_IMAGES, PATH_ROAD_IMAGES, GRID_SIZE, GRID_WIDTH
from app import group_roads, map

loaded_images = [image.load(PATH_ROAD_IMAGES + img).convert_alpha() for img in ROAD_IMAGES]

class RoadBlock(sprite.Sprite):
    # pos  - int (number of col and row)
    dragging_image = None
    dragging_offset = (0, 0)
    selected_image = None
    type = None

    was_moved = False

    grid_pos = (None, None)

    def __init__(self, type, pos, in_grid = False, transforms=[]):
        super().__init__()
        self.type = type
        self.image = loaded_images[type]
        self.init_pos = pos
        self.rect = self.image.get_rect()
        self.transforms = transforms

        if in_grid:
            self.rect.x = pos[0] * GRID_SIZE
            self.rect.y = pos[1] * GRID_SIZE
            self.grid_pos = pos
            self.was_moved = True
        else:
            self.rect.x = GRID_WIDTH * GRID_SIZE
            self.rect.y = self.init_pos[1] * GRID_SIZE
        
        for i in transforms:
            if i == 0:
                self.image = transform.rotate(self.image, 90)
            elif i == 1:
                self.image = transform.flip(self.image, True, False)


        group_roads.add(self)

    def check_click(self, mouse):
        return self.rect.collidepoint(mouse)
    
    def move(self, x, y, save_position=False):
        # if x >= GRID_SIZE * (GRID_WIDTH - 1): 
        #     x = GRID_SIZE * (GRID_WIDTH - 1)
        self.rect.x = x
        self.rect.y = y
        self.was_moved = True
        if save_position:
            old_pos = self.grid_pos
            self.grid_pos = (self.rect.x // GRID_SIZE, self.rect.y // GRID_SIZE)
            map.insert_road(self.type, self.transforms, self.grid_pos, old_pos)

    def copy(self):
        if not self.was_moved:
            return RoadBlock(self.type, self.init_pos, in_grid = False, transforms=[])
        

    def kill(self):
        map.remove_road(self.grid_pos)
        super().kill()



