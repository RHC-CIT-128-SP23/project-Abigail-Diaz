#!/usr/bin/env python3
'''
    Rio Hondo College
    CIT 128: Python Programming II
    Student Directed Project
'''

import pygame as pg
import sys
import math
from Enemy import Enemy
from Player import Player

# start pygame
pg.init()

screen_width, screen_length = 850, 420
floor = 420
background_scroll = 0

cat_image_file_paths =[]
eye_image_file_paths = []

# Set window display
screen = pg.display.set_mode((screen_width, screen_length))
pg.display.set_caption('Space Cat')
clock = pg.time.Clock()
time = 60

# Import background
background = pg.image.load('media/background.jpg').convert()
background = pg.transform.smoothscale(background, (screen_width, screen_length))

tiles = math.ceil(screen_width / background.get_width()) + 1

# Set starting position of surfaces
#platform.set_position(screen_width/2, screen_length/2)

# Resize platform
#platform.resize_image(60, 60)

# Save the file names in an array
for item in range(6):
    cat_image_file_paths.append(f"media/cat_walk_{item + 1}.png")

for item in range(3):
    eye_image_file_paths.append(f'media/eye_{item + 1}.png')

# create objects
#platform = Platform(90, 50)
cat = Player(cat_image_file_paths, 80, 80)
eye = Enemy(eye_image_file_paths, 80, 80)

#platform.file_names.append('media/ground.png')###

cat.initialize_sprite()
cat.set_position(400, floor)

#platform.initialize_sprite()#########
#platform.set_position(screen_width/2, screen_length/2)###

eye.initialize_sprite()
eye.set_position(screen_width/2, screen_length/2)

# Assume game is running
running = True

while running:
    for event in pg.event.get():
        if event.type ==  pg.QUIT:
            pg.quit()
            sys.exit()
    
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                cat.gravity = -20
                cat.jump = True
        
        # move cat right with -> key
        if event.type ==  pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                cat.update_spr = True
                #cat.direction["right"] = True #########
                cat.move_left = False
                
            if event.key == pg.K_LEFT:
                cat.move_left = True
                cat.direction["right"] = False
                cat.update_spr = True
        
        if event.type == pg.KEYUP:
            if event.key == pg.K_RIGHT or event.key == pg.K_LEFT:
                #stop the cat
                cat.direction["right"] = False
                cat.move_left = False
                cat.update_spr = False

    # Display the background on the window
    screen.blit(background, (-100, 0))
    screen.blit(background, (0, 0))
    screen.blit(background, (100, 0))
    screen.blit(background, (550 , 0))

    i = 0
    while(i < tiles and cat.update_spr):
        screen.blit(background, (background.get_width()*i + background_scroll, 0))
        i += 1
        background_scroll -= .8
    
    if abs(background_scroll) > background.get_width():
        background_scroll = 0
    
    #Display Platform
    #screen.blit(platform.surf_image, platform.rect)#####
    
    # Check for user actions
    cat.move()
    
    # Check for collision
    #platform.platform_collision(cat)#########
    
    # check if cat reached the floor
    cat.floor_reached(floor)
    
    # check if the cat goes out of the screen's range
    cat.range_reached(screen_width, screen_length, 0)

    # Display Cat Character
    cat.update_sprite() # can add more animations here later
    screen.blit(cat.surf_image, cat.rect)

    # Enemy action
    eye.move()
    eye.update_spr = True
    eye.update_sprite()
    screen.blit(eye.surf_image, eye.rect)
    
    #update screen
    pg.display.flip()
    clock.tick(60)