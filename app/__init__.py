import pygame
import sys
from config import WINDOW_SIZE

pygame.init()

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Drag and Drop')

from app.objects.grid import Grid
from app.objects.titles import Titles
from app.objects.menu import Menu
from app.car.main import Car
from app.objects.map import Map


grid = Grid()
titles = Titles()
menu = Menu()
car = Car((11,11), 4, 4)
map = Map()


group_roads = pygame.sprite.Group()
from app.objects.road_block import RoadBlock
RoadBlock(0, (0,0))
RoadBlock(1, (0,1))
RoadBlock(2, (0,2))
RoadBlock(3, (0,3))

from app.objects.button import Buttons
buttons = Buttons()

import app.loop