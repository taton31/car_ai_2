from config import GRID_WIDTH, GRID_HEIGHT, PATH_SAVED_MAP


class Map():
    def __init__(self):
        self.map = [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

    def save(self):
        with open(PATH_SAVED_MAP, 'w') as file:
            file.write(str(self.map))

    def load(self, roadblock):
        with open(PATH_SAVED_MAP, 'r') as file:
            self.map = eval(file.read())

        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if not self.map[y][x] is None:
                    roadblock(self.map[y][x], (x, y), in_grid=True)
                    

    def insert_road(self, type, new_pos, old_pos):
        if old_pos[1]:
            self.map[old_pos[1]][old_pos[0]] = 0
        self.map[new_pos[1]][new_pos[0]] = type