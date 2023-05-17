#!/usr/bin/env python3
'''
    Rio Hondo College
    CIT 128: Python Programming II
    Student Directed Project
'''

import pygame as pg
import sys
import math
from Counter import Counter
from Enemy import Enemy
from Player import Player
from Platform import Level, screen_width, screen_length
from Physics import Physics
from Sprites import Sprite
import random
from Fire import Fire
from Shoot import Shoot
from Levels import *
from Sound import Sound


# start pygame
pg.init()
floor = 420
fps = 60
non_col = 0
on_floor_counter = 0
press_x_key_count = 0


# Set window display
screen = pg.display.set_mode((screen_width, screen_length))
pg.display.set_caption('Space Cat')
clock = pg.time.Clock()
sound = Sound()


# Store file paths for each sprite image 
cat_walk_sprites_file_paths = []
cat_idle_sprites_file_paths = []
cat_damage_sprites_file_paths = []

eye_image_file_paths = []
platform_image_file_paths = []

# Will store all sprite file paths arrays according to their intended action
cat_sprites_file_paths = {'walk': None, 'idle': None, 'damage': None}     

# Save the file path names in their intended array
for item in range(6):
    cat_walk_sprites_file_paths.append(f"media/walk_{item + 1}.png")

for item in range(4):
    cat_idle_sprites_file_paths.append(f"media/idle_{item + 1}.png")

for item in range(5):
    cat_damage_sprites_file_paths.append(f"media/damage_{item + 1}.png")

on_floor = False # delete

for item in range(3):
    eye_image_file_paths.append(f'media/eye_{item + 1}.png')

# Assign the file path arrays to their corresponding place in the dict
cat_sprites_file_paths['walk'] = cat_walk_sprites_file_paths
cat_sprites_file_paths['idle'] = cat_idle_sprites_file_paths
cat_sprites_file_paths['damage'] = cat_damage_sprites_file_paths

# create objects 
cat = Player(120, 281,  60, 40, cat_sprites_file_paths)
cat_physics = Physics(cat.rect)

# Holds current level map
level = Level(screen)
counter = Counter(screen)
shoot = Shoot(90, 90, cat, level.enemies, screen)
sound.play_background_music()

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
                cat.update_current_sprite('walk')
                cat.update_spr = True
                cat_physics.move_right = True
                cat_physics.direction['left'] = False
                cat_physics.direction["right"] = True
                cat_physics.move_left = False
    
            if event.key == pg.K_LEFT:
                cat.update_current_sprite('walk')
                cat_physics.move_left = True
                cat_physics.move_right= False
                cat_physics.direction["right"] = False
                cat_physics.direction['left'] = True
                cat.update_spr = True

            if event.key == pg.K_x:
                shoot.running = True # prevents fire sprite from appearing before 'x' is pressed
                
                press_x_key_count += 1
                print('press_x_key_count: ', press_x_key_count)
                if press_x_key_count > 1:
                    shoot.attack()
                    if press_x_key_count > 2:
                        press_x_key_count = 0
                else:
                    shoot.shooting = False

        if event.type == pg.KEYUP:
            if event.key == pg.K_RIGHT or event.key == pg.K_LEFT:
                cat.update_current_sprite('idle')
                cat.update_spr = True
                cat_physics.direction["right"] = False
                cat_physics.move_left = False
                cat_physics.move_right = False
                cat_physics.direction["left"] = False
            if event.key == pg.K_x:
                pass
                #shoot.shooting = False

    level.run()
    counter.run()
    #sound.play_background_music()

    # Activate the fire sprite group display and sprite update
    shoot.run()
    
    ''' Cat Actions'''
    # Activate physics function checks
    cat_physics.move(level)
    
    # check if the cat goes out of the screen's range
    cat_physics.range_reached(screen_width, screen_length, 0)

    # Display Cat Character
    cat.update_sprite() 
    
    '''Collision Checks'''

    enemy_collision = pg.sprite.spritecollide(cat, level.enemies, False, pg.sprite.collide_mask)
    enemy_rect_collision = level.get_enemy_collision_rect(cat)
    if enemy_collision:
        if cat.rect.x < enemy_rect_collision.x:
            cat.update_current_sprite('damage')
            cat.rect.x -= 70
        if cat.rect.x > enemy_rect_collision.x:
            cat.update_current_sprite('damage')
            cat.rect.x += 70
        counter.collision()

    

    collision = pg.sprite.spritecollide(cat, level.tiles, False, pg.sprite.collide_mask)
    
    if collision:
        non_col = 0
        cat_physics.fall = False
        cat_physics.jump = False
        cat_col = cat.rect.bottom
        
        print('1: IN collision')
        collision_rect = level.get_collision_rect(cat)
        rect_col = collision_rect.top
    
            # Upon collision, check if cat is on top of a rectangle
        if  ((cat.rect.left < collision_rect.right or cat.rect.right > collision_rect.left) and ((abs(cat.rect.bottom - collision_rect.top) < 50))):
            cat_physics.fall = False
            on_floor_counter += 1
            
            # Collision with the floor
            if (abs(cat.rect.bottom - collision_rect.top)) < 50:
                cat.rect.bottom = collision_rect.top + 0.5
            
            if cat_physics.direction['right']:# and cat.rect.x > 200
                level.move_screen_forward(-2) 

            print('x pos: ', cat.rect.x)
            print('y pos: ', cat.rect.y)

        elif  ((cat.rect.left < collision_rect.right or cat.rect.right > collision_rect.left) and (abs(cat.rect.top - collision_rect.bottom) < 20)):
            print('bottom collision')
            cat_physics.repel_down()
        
        elif collision_rect.right > cat.rect.right and (cat.rect.bottom > collision_rect.top):
            cat_physics.fall = False
            on_floor_counter = 0
            cat_physics.repel_to_left()
        
        elif collision_rect.left < cat.rect.left and (cat.rect.bottom > collision_rect.top):
            cat_physics.repel_to_right()
            on_floor_counter = 0
            cat_physics.fall = False

    else:
            # prevents non-intended fall from becoming true when else becomes true for a moment
            # to avoid alternation between else and floor collision, so fall does not become true while being on the floor
        if non_col > 4: 
            cat_physics.fall = True
            print('greater than 3')
    
        print('else')
        cat_physics.direction['down'] = True
        non_col += 1
            

    '''Enemy Eye Actions'''

    #update screen
    screen.blit(cat.image, cat.rect) 
    
    pg.display.flip()
    clock.tick(fps)