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
platform = pg.image.load('media/ground.png').convert_alpha()

# create the rectangles of each character
cat = pg.transform.smoothscale(cat, (80, 80))
platform = pg.transform.smoothscale(platform, (90, 50))
bat = pg.transform.smoothscale(bat, (80, 80))
cat_rect = cat.get_rect(midbottom = (0, floor + 30))
bat_rect = bat.get_rect(midbottom = (screen_width, floor - 10))
platform_rect = platform.get_rect(midbottom= (screen_width/2, screen_length/2))

# Variables for cat movements
player_gravity = 0
cat_jump = False
cat_fall = False

# Cat movement
move_right = False
move_left = False

# Cat Actions
recent_platform_collide = False

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
        
        # move cat right with -> key
        if event.type ==  pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                move_right = True      # number of steps to the right
                move_left = False
            elif event.key == pg.K_LEFT:
                move_left = True
                move_right = False
        
        if event.type == pg.KEYUP:
            if event.key == pg.K_RIGHT or event.key == pg.K_LEFT:
                #stop the cat
                move_right = False
                move_left = False

    # Display the background on the window
    #background_motion += 1/4
    screen.blit(space_background, (-100, 0))
    screen.blit(space_background, (0, 0))
    screen.blit(space_background, (100, 0))
    screen.blit(space_background, (550 , 0))
    
    #Display Platform
    screen.blit(platform, platform_rect)
    
    # ~~~~ Cat Animation ~~~~
    # Cat movement
    # move cat to the right of window (from user perspective)
    if move_right == True:
        cat_rect.x += 2
    if move_left == True:
        cat_rect.x -= 2
    
    # Collision with platform
    collide_platform = pg.Rect.colliderect(cat_rect, platform_rect)
    
    # Keep cat on top of platform
    if collide_platform:
        cat_jump = False
        cat_rect.bottom = platform_rect.top
        recent_platform_collide = True
    
    # Cat falls when outside platform
    if cat_rect.x > platform_rect.x and recent_platform_collide == True:
        cat_fall = True
        recent_platform_collide = False
    
    # ~~ Jump Dynamics ~~
    # Gravity: Cat will fall down as y values increase
    if cat_fall == True:
        player_gravity += 1
        cat_rect.y += player_gravity
        
    # cat will move on the x axis as it completes the jump
    if cat_jump == True:
        cat_fall = False
        player_gravity += 1
        cat_rect.y += player_gravity
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
    
    screen.blit(cat, cat_rect)
    
    # Bat movements: Moves from left to right
    bat_rect.right -= 1
    screen.blit(bat, bat_rect)
    
    # check if the bat goes out of the screen's range    
    if bat_rect.left < 0:
        bat_rect.left = screen_width
    
    #update screen
    pg.display.flip()
    clock.tick(60)