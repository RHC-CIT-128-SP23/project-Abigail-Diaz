#!/usr/bin/env python3
'''
    Rio Hondo College
    CIT 128: Python Programming II
    Student Directed Project
'''

import pygame as pg
import sys
from Player import Player
from Platform import Level, screen_width, screen_length
from Shoot import Shoot
from Levels import *
from Sound import Sound
from Menu import Menu

def main():

    # start pygame
    pg.init()

    fps = 60

    # Set window display
    screen = pg.display.set_mode((screen_width, screen_length))
    pg.display.set_caption('Space Cat')
    clock = pg.time.Clock()
    
    # game feautures objects
    sound = Sound()
    menu = Menu(screen)
    level = Level(screen)

    cat = Player(120, 281,  60, 40, level, screen)

    shoot = Shoot(90, 90, cat, level.enemies, screen)

    running = True

    while running:
        sound.play_background_music()
    
        for event in pg.event.get():
            if event.type ==  pg.QUIT:
                pg.quit()
                sys.exit()
    
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    cat.physics.make_jump()
        
            if event.type ==  pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    cat.update_current_sprite('walk')
                    cat.update_spr = True
                    cat.physics.move_right = True
                    cat.physics.direction['left'] = False
                    cat.physics.direction["right"] = True
                    cat.physics.move_left = False
    
                if event.key == pg.K_LEFT:
                    cat.update_current_sprite('walk')
                    cat.physics.move_left = True
                    cat.physics.move_right= False
                    cat.physics.direction["right"] = False
                    cat.physics.direction['left'] = True
                    cat.update_spr = True

                if event.key == pg.K_x:
                    shoot.running = True # prevents fire sprite from appearing before 'x' is pressed
                    shoot.attack()

            if event.type == pg.KEYUP:
                if event.key == pg.K_RIGHT or event.key == pg.K_LEFT:
                    cat.update_current_sprite('idle')
                    cat.update_spr = True
                    cat.physics.direction["right"] = False
                    cat.physics.move_left = False
                    cat.physics.move_right = False
                    cat.physics.direction["left"] = False
        
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    mouse_click_pos = pg.mouse.get_pos()
                    if menu.start_text_rect.collidepoint(mouse_click_pos):
                        cat.counter.menu.start = False
                    if cat.counter.menu.restart_rect.collidepoint(mouse_click_pos):
                        
                        cat.restart()
                        cat.counter.restart()
                        level.restart()
        level.run()
        cat.counter.run() 
        cat.run()
        shoot.run()

        cat.counter.menu.start_menu() 
        pg.display.flip()
        clock.tick(fps)

if __name__ == "__main__":
    main()