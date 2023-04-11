#!/usr/bin/env python3
'''
    Rio Hondo College
    CIT 128: Python Programming II
    Student Directed Project
'''

import pygame as pg
import sys

# start pygame
pg.init()

screen_width, screen_length = 850, 420
floor = 420

# Set window display
screen = pg.display.set_mode((screen_width, screen_length))
pg.display.set_caption('Space Cat')
clock = pg.time.Clock()

# Import images
space_background = pg.image.load('media/background3Medium.jpeg').convert()
cat = pg.image.load('media/cat.png').convert_alpha()
bat = pg.image.load('media/bat-x1.gif').convert_alpha()

# create the rectangles of each character
cat_character = pg.transform.smoothscale(cat, (80, 80))
bat = pg.transform.smoothscale(bat, (80, 80))
cat_rect = cat_character.get_rect(midbottom = (0, floor + 30))
bat_rect = bat.get_rect(midbottom = (screen_width, floor - 10))