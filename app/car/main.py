from pygame import image, transform, draw
from pygame import K_UP, K_LEFT, K_RIGHT
# from pygame.math import Vector2
import math
from app.car.utils import blit_rotate_center, line_intersection, line_circle_intersection
from config import CAR_IMAGE, DEBUG, GRID_SIZE, VECTORS_LEN
from app import window


class Car:
    def __init__(self, pos, max_vel, rotation_vel):
        self.img = image.load(CAR_IMAGE)
        self.img = transform.scale(self.img, (50, 30))
        self.img = transform.rotate(self.img, 90)
        self.img.fill((0,0,0))
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = -90
        self.x, self.y = pos
        self.acceleration = 0.1


    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self):
        blit_rotate_center(window, self.img, (self.x, self.y), self.angle)


        if DEBUG:
            center = self.img.get_rect(topleft=(self.x, self.y)).center
            angle = -math.radians(self.angle + 90)
            x = center[0] + math.cos(angle) * VECTORS_LEN
            y = center[1] + math.sin(angle) * VECTORS_LEN
            # line_surface, line_mask = create_line_mask(center, (x, y), 3)

            # win.blit(line_mask.to_surface(), center)
            # mask.from_surface
            # mask.from_surface(draw.line(win, (0,0,0), center, (x, y)))



    def check_collision(self, roadblocks):
        self.radars()
        center = self.img.get_rect(topleft=(self.x, self.y)).center
        angle = -math.radians(self.angle + 90)
        x = center[0] + math.cos(angle) * VECTORS_LEN
        y = center[1] + math.sin(angle) * VECTORS_LEN
        
        # for roadblock in roadblocks:
        #     # a = line_intersection(roadblock.rect.topleft, roadblock.rect.topright, center, (x, y))
        #     # a = a or line_intersection(roadblock.rect.topleft, roadblock.rect.bottomleft, center, (x, y))
        #     # a = a or line_intersection(roadblock.rect.bottomright, roadblock.rect.bottomleft, center, (x, y))
        #     # a = a or line_intersection(roadblock.rect.bottomright, roadblock.rect.topright, center, (x, y))

        #     # if a and DEBUG: draw.circle(win, (255, 0, 0), a, 6)

        #     a = line_circle_intersection(center[0], center[1], x, y, roadblock.rect.center[0], roadblock.rect.center[1], GRID_SIZE // 1.5, VECTORS_LEN)
        #     if a and DEBUG: 
        #         # draw.circle(window, (255, 0, 0), a, 6)
        # draw.line(window, (125,0,0), center, (x, y))

    def radars(self):
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
            if window.get_at((int(center[0] + cos * len), int(center[1] + sin * len))) != (255, 255, 255):
                return (int(center[0] + cos * len), int(center[1] + sin * len))
            return find_point(center, cos, sin, len + 1)

        radar = []
        center = self.img.get_rect(topleft=(self.x, self.y)).center

        angle = -math.radians(self.angle + 90)
        center_new = (center[0] + math.cos(angle) * 30, center[1] + math.sin(angle) * 30)
        point = find_point(center_new, math.cos(angle), math.sin(angle))
        radar.append(point)

        if DEBUG: draw.circle(window, (255, 0, 0), point, 3)

        angle = -math.radians(self.angle + 55)
        center_new = (center[0] + math.cos(angle) * 33, center[1] + math.sin(angle) * 33)
        point = find_point(center_new, math.cos(angle), math.sin(angle))
        radar.append(point)

        if DEBUG: draw.circle(window, (255, 0, 0), point, 3)

        angle = -math.radians(self.angle + 25)
        center_new = (center[0] + math.cos(angle) * 25, center[1] + math.sin(angle) * 25)
        point = find_point(center_new, math.cos(angle), math.sin(angle))
        radar.append(point)

        if DEBUG: draw.circle(window, (255, 0, 0), point, 3)

        angle = -math.radians(self.angle + 125)
        center_new = (center[0] + math.cos(angle) * 33, center[1] + math.sin(angle) * 33)
        point = find_point(center_new, math.cos(angle), math.sin(angle))
        radar.append(point)

        if DEBUG: draw.circle(window, (255, 0, 0), point, 3)

        angle = -math.radians(self.angle + 155)
        center_new = (center[0] + math.cos(angle) * 25, center[1] + math.sin(angle) * 25)
        point = find_point(center_new, math.cos(angle), math.sin(angle))
        radar.append(point)

        if DEBUG: [draw.circle(window, (255, 0, 0), point, 3) for point in radar]


        
        # for roadblock in roadblocks:
        #     # a = line_intersection(roadblock.rect.topleft, roadblock.rect.topright, center, (x, y))
        #     # a = a or line_intersection(roadblock.rect.topleft, roadblock.rect.bottomleft, center, (x, y))
        #     # a = a or line_intersection(roadblock.rect.bottomright, roadblock.rect.bottomleft, center, (x, y))
        #     # a = a or line_intersection(roadblock.rect.bottomright, roadblock.rect.topright, center, (x, y))

        #     # if a and DEBUG: draw.circle(win, (255, 0, 0), a, 6)

        #     a = line_circle_intersection(center[0], center[1], x, y, roadblock.rect.center[0], roadblock.rect.center[1], GRID_SIZE // 1.5, VECTORS_LEN)
        #     if a and DEBUG: draw.circle(window, (255, 0, 0), a, 6)

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
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()

    def update(self, keys):
        moved = False

        if keys[K_LEFT]:
            self.rotate(left=True)
        if keys[K_RIGHT]:
            self.rotate(right=True)
        if keys[K_UP]:
            moved = True
            self.move_forward()

        if not moved:
            self.reduce_speed()
