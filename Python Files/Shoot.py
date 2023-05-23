import pygame as pg
from Fire import Fire
from Sound import Sound

class Shoot:
    def __init__(self, image_width, image_length, shooting_obj, damaged_obj, surface):
        self.image_width  = image_width
        self.image_length = image_length
        self.running = False
        self.shooting = False
        self.surface = surface
        self.fire_sprite_group = pg.sprite.Group()
        self.fire = Fire(50, 50, shooting_obj) # might be able to delete
        self.fire_sprite_group.add(self.fire)
        self.shooting_obj = shooting_obj
        self.damaged_obj = damaged_obj
        self.sound = Sound()
        

    def run(self): # try to put on one event  x press
        ''' Activate the fire sprite group display and sprite update'''
        if self.running: # checks if user has pessed for the first time 'x'
            self.fire_sprite_group.draw(self.surface)
            self.fire_sprite_group.update()
            self.shot()
        
        #creates a new fire object if player is shooting
    def attack(self): # might have to change initial position here
            self.make_another_fire()
            self.sound.play_shot_sound()

    def make_another_fire(self):
        new_fire = self.fire = Fire(50, 50, self.shooting_obj)
        self.fire_sprite_group.add(new_fire)
    
    def clear_fire_group(self):
        pass

    def shot(self):
        self.collision = pg.sprite.groupcollide(self.damaged_obj, self.fire_sprite_group, True, True) # collision between two groups 
        
        if len(self.damaged_obj) < 1:
            print('empty')

        if self.collision:
            self.fire_sprite_group.update('hits')
        else:
            self.fire_sprite_group.update('spark')
    
