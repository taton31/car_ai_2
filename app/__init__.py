import pygame
import sys
from config import WINDOW_SIZE

pygame.init()

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Drag and Drop')

from app.objects.grid import Grid
from app.objects.titles import Titles
from app.objects.menu import Menu


grid = Grid()
titles = Titles()
menu = Menu()

group_roads = pygame.sprite.Group()
from app.objects.road_block import RoadBlock
roads = RoadBlock(0, (0,0))
roads2 = RoadBlock(1, (0,1))

import app.loop