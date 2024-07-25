from pygame import image, transform
from pygame import K_UP, K_LEFT, K_RIGHT
import math
from app.car.utils import blit_rotate_center
from config import CAR_IMAGE



class Car:
    def __init__(self, pos, max_vel, rotation_vel):
        self.img = image.load(CAR_IMAGE)
        self.img = transform.scale(self.img, (50, 30))
        self.img = transform.rotate(self.img, 90)
        self.img.fill((0,0,0))
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = pos
        self.acceleration = 0.1

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, win):
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)

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
