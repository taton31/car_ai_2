import pygame
import sys
from config import WINDOW_SIZE, CARS_NUMBER

import neat

pygame.init()

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Drag and Drop')

from app.objects.fps import draw_fps, draw_score
from app.objects.grid import Grid
from app.objects.titles import Titles
from app.objects.menu import Menu
from app.car.main import Car, is_somebody_alive
from app.objects.map import Map


grid = Grid()
titles = Titles()
menu = Menu()

map = Map()


group_roads = pygame.sprite.Group()
from app.objects.road_block import RoadBlock
RoadBlock(0, (0,0))
RoadBlock(1, (0,1))
RoadBlock(2, (0,2))
RoadBlock(3, (0,3))
RoadBlock(0, (0,0), True, [0])

from app.objects.button import Buttons
buttons = Buttons()

clock = pygame.time.Clock()

# from app.genoms import Checkpointer
# a=Checkpointer() 
import app.neat