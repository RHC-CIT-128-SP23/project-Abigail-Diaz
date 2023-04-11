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

# Variables for cat movements
player_gravity = 0
cat_jump = False

# Background movement
background_motion = 0


# Assume game is running
running = True

while running:
    for event in pg.event.get():
        if event.type ==  pg.QUIT:
            pg.quit()
            sys.exit()
    
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                player_gravity = -20
                cat_jump = True

    # Display the background on the window
    background_motion += 1/4
    screen.blit(space_background, (-100 + background_motion, 0))
    screen.blit(space_background, (0, 0))
    screen.blit(space_background, (background_motion + 100, 0))
    screen.blit(space_background, (750 + background_motion, 0))
    
    
    # ~~~~ Cat Animation ~~~~
    # move cat to the right of window (from user perspective)
    cat_rect.left += 2
    
    # Gravity: Cat will fall down as y values increase
    player_gravity += 1
    cat_rect.y += player_gravity
    
    # cat will move on the x axis as it completes the jump
    if cat_jump == True:
        cat_rect.x += 3
    
    # check if cat reached the floor
    #Condition: If cat reached the floor, then it must
    # be false that he is jumping
    if cat_rect.bottom >= floor: 
        cat_rect.bottom = floor
        cat_jump = False
    
    # check if the cat goes out of the screen's range
    if cat_rect.left > screen_width:  
        cat_rect.x = 0
        
    screen.blit(cat_character, cat_rect)
    
    # Bat movements: Moves from left to right
    bat_rect.right -= 1
    screen.blit(bat, bat_rect)
    
    # check if the bat goes out of the screen's range    
    if bat_rect.left < 0:
        bat_rect.left = screen_width
    
    if background_motion == 100:
        background_motion  = -100
    
    #update screen
    pg.display.flip()
    clock.tick(60)
    
 