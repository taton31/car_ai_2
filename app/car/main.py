from pygame import image, transform, draw
from pygame import K_UP, K_LEFT, K_RIGHT
import math
from app.car.utils import blit_rotate_center #, line_intersection, line_circle_intersection
from config import CAR_IMAGE, DEBUG, GRID_SIZE, VECTORS_LEN, GRID_WIDTH, GRID_HEIGHT, MAX_FITNESS
from app import window

car_image = image.load(CAR_IMAGE)
car_image = transform.scale(car_image, (50, 30))
car_image = transform.rotate(car_image, 90)
car_image.set_alpha(128)

class Car:
    def __init__(self, pos, max_vel, rotation_vel):
        self.img = car_image
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = -90
        self.x, self.y = pos
        self.acceleration = 0.2

        self.alive = True
        self.fitness = 0
        self.fitness_map = [[False for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

        self.flag_update_map = False

        self.ticks = 0


    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self):
        if not self.alive: return

        blit_rotate_center(window, self.img, (self.x, self.y), self.angle)


        # if DEBUG:
        #     center = self.img.get_rect(topleft=(self.x, self.y)).center
        #     angle = -math.radians(self.angle + 90)
        #     x = center[0] + math.cos(angle) * VECTORS_LEN
        #     y = center[1] + math.sin(angle) * VECTORS_LEN
          

    def radars(self, grid):
        # def find_point(x1, y1, x2, y2):  
        #     abs_x = (x2 - x1) / 2
        #     abs_y = (y2 - y1) / 2
        #     if abs(abs_x) + abs(abs_y) < 4:
        #         return (x1, y1)
        #     mid_x = int(abs_x + x1)
        #     mid_y = int(abs_y + y1)
        #     if window.get_at((mid_x, mid_y)) == (255, 255, 255):
        #         return find_point(mid_x, mid_y, x2, y2)
        #     else:
        #         return find_point(x1, y1, mid_x, mid_y)
            
        # x = int(center[0] + (math.cos(angle) * VECTORS_LEN / 2))
        # y = int(center[1] + (math.sin(angle) * VECTORS_LEN / 2))

        # if x < 0: x=0
        # if y < 0: y=0
        # # if x > window.: x=0
        # # if x < 0: x=0

        # if window.get_at((x, y)) == (255, 255, 255):
        #     x = int(center[0] + math.cos(angle) * VECTORS_LEN)
        #     y = int(center[1] + math.sin(angle) * VECTORS_LEN)
        #     if x < 0: x=0
        #     if y < 0: y=0
        #     point = find_point(center[0], center[1], x, y)
        # else:
        #     point = find_point(center[0], center[1], x, y)
                
        def find_point(center, cos, sin, len = 1):
            pic_x = int(center[0] + cos * len)
            pic_y = int(center[1] + sin * len)
            if pic_x <= 0 or pic_y <= 0 or pic_x >= grid.get_width() or pic_y >= grid.get_height():
                return (pic_x, pic_y)

            if grid.get_at((pic_x, pic_y)) == (199, 199, 199, 255) or len > VECTORS_LEN:
                return (pic_x, pic_y)
            return find_point(center, cos, sin, len + 1)

        def line_length(p1, p2):
            a = p1[0] - p2[0]
            b = p1[1] - p2[1]

            return int(math.sqrt(a**2 + b**2))
        
        radar = []
        vision = []
        center = self.img.get_rect(topleft=(self.x, self.y)).center

        angle = - math.radians(self.angle + 90)
        center_new = (center[0] + math.cos(angle) * 25, center[1] + math.sin(angle) * 25)
        point = find_point(center_new, math.cos(angle), math.sin(angle))
        vision.append(line_length(center_new, point))
        radar.append(point)

        angle = -math.radians(self.angle + 55)
        center_new = (center[0] + math.cos(angle) * 24, center[1] + math.sin(angle) * 24)
        point = find_point(center_new, math.cos(angle), math.sin(angle))
        vision.append(line_length(center_new, point))
        radar.append(point)

        angle = -math.radians(self.angle + 25)
        center_new = (center[0] + math.cos(angle) * 15, center[1] + math.sin(angle) * 15)
        point = find_point(center_new, math.cos(angle), math.sin(angle))
        vision.append(line_length(center_new, point))
        radar.append(point)

        angle = -math.radians(self.angle + 125)
        center_new = (center[0] + math.cos(angle) * 24, center[1] + math.sin(angle) * 24)
        point = find_point(center_new, math.cos(angle), math.sin(angle))
        vision.append(line_length(center_new, point))
        radar.append(point)

        angle = -math.radians(self.angle + 155)
        center_new = (center[0] + math.cos(angle) * 15, center[1] + math.sin(angle) * 15)
        point = find_point(center_new, math.cos(angle), math.sin(angle))
        vision.append(line_length(center_new, point))
        radar.append(point)

        if DEBUG: [draw.circle(window, (255, 0, 0), point, 3) for point in radar]

        vision.append(self.vel * 10)
        return vision
        

        

    def check_death(self, grid):
        center = self.img.get_rect(topleft=(self.x, self.y)).center

        try:
            angle = - math.radians(self.angle + 55)
            center_new = (center[0] + math.cos(angle) * 24, center[1] + math.sin(angle) * 24)
            if grid.get_at((int(center_new[0] + math.cos(angle)), int(center_new[1] + math.sin(angle)))) == (199, 199, 199, 255):
                return True
            if DEBUG: draw.circle(window, (0, 255, 255), center_new, 2) 

            angle = - math.radians(self.angle + 25)
            center_new = (center[0] + math.cos(angle) * 15, center[1] + math.sin(angle) * 15)
            if grid.get_at((int(center_new[0] + math.cos(angle)), int(center_new[1] + math.sin(angle)))) == (199, 199, 199, 255):
                return True
            if DEBUG: draw.circle(window, (0, 255, 255), center_new, 2) 

            angle = - math.radians(self.angle + 125)
            center_new = (center[0] + math.cos(angle) * 24, center[1] + math.sin(angle) * 24)
            if grid.get_at((int(center_new[0] + math.cos(angle)), int(center_new[1] + math.sin(angle)))) == (199, 199, 199, 255):
                return True
            if DEBUG: draw.circle(window, (0, 255, 255), center_new, 2) 

            angle = - math.radians(self.angle + 155)
            center_new = (center[0] + math.cos(angle) * 15, center[1] + math.sin(angle) * 15)
            if grid.get_at((int(center_new[0] + math.cos(angle)), int(center_new[1] + math.sin(angle)))) == (199, 199, 199, 255):
                return True
            if DEBUG: draw.circle(window, (0, 255, 255), center_new, 2) 
        except:
            pass
        return False

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration * 2, 0)
        self.move()

    def update_fitness(self,  count_roads):
        center = self.img.get_rect(topleft=(self.x, self.y)).center

        j, i = center[0]//GRID_SIZE, center[1]//GRID_SIZE

        if not self.fitness_map[i][j]:
            self.fitness_map[i][j] = True
            self.fitness += 1
            self.flag_update_map = True

            if self.fitness > count_roads + 10:
                self.fitness += (10 * count_roads) / self.ticks
                self.alive = False

        if i == 0 and j == 0 and self.fitness > 3 and self.flag_update_map:
            self.fitness_map = [[False for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
            self.fitness_map[i][j] = True
            self.flag_update_map = False
            self.fitness += 1

        if self.fitness < -1: 
            self.alive = False
            self.fitness -= 3


    def update_move(self, keys, left, right, forward):
        moved = False

        if keys[K_LEFT] or left:
            self.rotate(left=True)
        if keys[K_RIGHT] or right:
            self.rotate(right=True)
        if keys[K_UP] or forward:
            moved = True
            self.move_forward()

        if not moved:
            self.reduce_speed()
            self.fitness -= 0.01


    def update(self, grid, keys, count_roads, left=False, right=False, forward=False):
        if not self.alive: return

        self.ticks += 0.016

        self.update_move(keys, left, right, forward)
        
        if self.check_death(grid): 
            self.alive = False
            self.fitness -= 3
        
        # self.radars(grid)
        self.update_fitness(count_roads)


        # print(self.fitness)


def is_somebody_alive(cars):
    for car in cars:
        if car.alive:
            return True
    return False