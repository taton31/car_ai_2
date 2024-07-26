from config import GRID_WIDTH, GRID_HEIGHT, PATH_SAVED_MAP


class Map():
    def __init__(self):
        self.map = [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.count_roads = 0

    def save(self):
        with open(PATH_SAVED_MAP, 'w') as file:
            file.write(str(self.map))
            

    def load(self, roadblock):
        with open(PATH_SAVED_MAP, 'r') as file:
            self.map = eval(file.read())

        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if not self.map[y][x] is None:
                    roadblock(self.map[y][x][0], (x, y), in_grid=True, transforms=self.map[y][x][1])
                    self.count_roads += 1
                    

    def insert_road(self, type, transforms, new_pos, old_pos):
        if old_pos[0] and old_pos[0] < GRID_WIDTH:
            self.map[old_pos[1]][old_pos[0]] = None
            self.count_roads -= 1
        if new_pos[0] < GRID_WIDTH:
            self.map[new_pos[1]][new_pos[0]] = [type, transforms]
            self.count_roads += 1

    def remove_road(self, pos):
        if pos[0] and pos[0] < GRID_WIDTH:
            self.map[pos[1]][pos[0]] = None
            self.count_roads -= 1