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
from Platform import Level, screen_width, screen_length
from Physics import Physics
from Sprites import Sprite
import random
from Levels import *

# start pygame
pg.init()

floor = 420
fps = 60


# Set window display
screen = pg.display.set_mode((screen_width, screen_length))
pg.display.set_caption('Space Cat')
clock = pg.time.Clock()

# Store file paths for each sprite image 
cat_walk_sprites_file_paths = []
cat_idle_sprites_file_paths = []
eye_image_file_paths = []
platform_image_file_paths = []

# To store all sprite file paths arrays according to their intended animation
cat_sprites_file_paths = {'walk': None, 'idle': None}     

# Save the file path names in their intended array
for item in range(6):
    cat_walk_sprites_file_paths.append(f"media/walk_{item + 1}.png")

for item in range(4):
    cat_idle_sprites_file_paths.append(f"media/idle_{item + 1}.png")

on_floor = False

for item in range(3):
    eye_image_file_paths.append(f'media/eye_{item + 1}.png')

# Assign the file path arrays to their corresponding place in the dict
cat_sprites_file_paths['walk'] = cat_walk_sprites_file_paths
cat_sprites_file_paths['idle'] = cat_idle_sprites_file_paths

# create objects and sprite groups
cat = Player(400, floor - 100,  60, 40, cat_sprites_file_paths)
player_group = pg.sprite.Group()
player_group.add(cat)
cat_physics = Physics(cat.rect)

# Holds current level map
level = Level(screen)



#eye = Enemy(eye_image_file_paths, 80, 80)
#platform = Platform(platform_image_file_paths, 90, 80)
#platform_group = pg.sprite.Group()
#platform_group.add(platform)

#cat.set_position(400, floor)
#platform.set_position(screen_width/2, screen_length/2)

#eye.set_position(screen_width/2, screen_length/2)


running = True

while running:
    for event in pg.event.get():
        if event.type ==  pg.QUIT:
            pg.quit()
            sys.exit()
    
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                cat_physics.make_jump()
                touching_floor = False

        
        if event.type ==  pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                #cat.update_current_sprite('walk')
                cat.update_spr = True
                cat_physics.move_right = True
                cat_physics.direction['left'] = False
                cat_physics.direction["right"] = True
                cat_physics.move_left = False
    
            if event.key == pg.K_LEFT:
                #cat.update_current_sprite('walk')
                cat_physics.move_left = True
                cat_physics.move_right= False
                cat_physics.direction["right"] = False
                cat_physics.direction['left'] = True
                cat.update_spr = True
        
        if event.type == pg.KEYUP:
            if event.key == pg.K_RIGHT or event.key == pg.K_LEFT:
                #cat.update_current_sprite('idle')
                cat.update_spr = True
                cat_physics.direction["right"] = False
                cat_physics.move_left = False
                cat_physics.move_right = False
                cat_physics.direction["left"] = False

    level.run()
    
    ''' Cat Actions'''
    # Check for user actions
    cat_physics.move()
    
    # check if the cat goes out of the screen's range
    cat_physics.range_reached(screen_width, screen_length, 0)

    # Display Cat Character
    cat.update_sprite()
    
    '''Collision Checks'''
    
    collision = pg.sprite.spritecollide(cat, level.tiles, False, pg.sprite.collide_mask)
    
    if collision:
        cat_physics.fall = False
        cat_physics.jump = False
    
        collision_rect = level.get_collision_rect(cat)

        if cat_physics.direction['up']:    
            on_floor = False

        if  ((cat.rect.left < collision_rect.right) or (cat.rect.right > collision_rect.left)) and abs((cat.rect.bottom - collision_rect.top)) < 20:

            # Cat collision was with the floor (collision on top of a top or free standing tile)
            if abs((cat.rect.bottom - collision_rect.top)) < 20:
                cat_physics.direction['down'] = False # False since there was a collision with the ground
                cat.rect.bottom = collision_rect.top + 0.5
                print('cat.rect.bottom: ', cat.rect.bottom)
                print('collision_rect.top :', collision_rect.top )
                print('floor assignment')
                on_floor = True

        elif cat_physics.direction['right'] and collision_rect.x > cat.rect.x and (cat.rect.bottom > collision_rect.top ):
            cat_physics.repel_to_left()
    
        elif cat_physics.direction['left'] and collision_rect.x < cat.rect.x and (cat.rect.bottom > collision_rect.top):
            cat_physics.repel_to_right()    
    else:
        cat_physics.fall = True
        cat_physics.direction['down'] = True

    
    '''Enemy Eye Actions'''
    # Enemy action
    #eye.move()
    #eye.update_spr = True
    #eye.update_sprite()
    #screen.blit(eye.surf_image, eye.rect)
    

    
    #update screen
    screen.blit(cat.image, cat.rect)
    pg.display.flip()
    clock.tick(fps)