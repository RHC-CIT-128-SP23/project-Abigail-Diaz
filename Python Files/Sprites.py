#from Rectangle import Rectangle
import pygame as pg
from Physics import Physics

class Sprite(pg.sprite.Sprite):

    def __init__(self, rect, posx, posy, image_width, image_length, image_paths_dict):
        pg.sprite.Sprite.__init__(self)
        self.image = None
        self.current_sprite = 0
        self.image_paths_dict = image_paths_dict
        self.sprite_images_dict = {'walk': None, 'idle': None, 'damage': None}
        self.current_sprite_array = []
        self.image_width = image_width
        self.image_length = image_length
        self.rect = rect
        self.update_spr = True
        # create rectangle as soon as object is made with the first image on the list
        self.initialize_sprite_dict()
        self.mask = pg.mask.from_surface(self.image)


    def set_rectangle(self, rect):
        self.rect = rect
    def update_rectangle(self):
        return self.get_updated_rect()
    
    def set_position(self, x, y): # should put in sprite class? physics?
        self.rect.x = x
        self.rect.y = y

    def get_rectangle(self, image): # create the rectangles of each surface
        return image.get_rect()
    
    def update_current_sprite(self, action):
        self.current_sprite = 0
        if action == 'idle':
            self.current_sprite_array = self.sprite_images_dict['idle']
            
        if action == 'walk': #not usable
            self.current_sprite_array = self.sprite_images_dict['walk']

        if action == 'damage': 
            self.current_sprite_array = self.sprite_images_dict['damage']
        
        if action == 'explode':
            self.current_sprite_array = self.sprite_images_dict['explode']

    def update_sprite(self): 
        '''Updates the sprite images to create animation'''

        # check if sprite animation is required
        if self.update_spr:
            if self.current_sprite < len(self.current_sprite_array) - 1:
                
                # update the sprite based on frame rate
                self.current_sprite += 0.2

                # reset the sprite image to the first one in the current sprite array
            else:
                self.current_sprite = 0

                #update current displayed image
        self.image = self.current_sprite_array[int(self.current_sprite)]
        self.mask = pg.mask.from_surface(self.image)
    
    def get_updated_rect(self):
        self.temp_rect = self.image.get_rect()
        return self.temp_rect
    
    def set_file_path_name(self, name):
        self.file_name = name
    
    # Import images
    def set_surface_image(self):
        self.image = pg.image.load(self.file_name).convert_alpha()
        self.resize_image()

    def resize_image(self):
        self.image = pg.transform.smoothscale(self.image, (self.image_width, self.image_length))
    
    def get_image(self):
        return self.image
    
    def initialize_sprite_dict(self):
        '''Assigns the animation images to local array image_paths by using array image_paths'''
        self.temp_array = []
        for sprite_paths_name, sprite_paths_array in self.image_paths_dict.items():
            self.walk_path_array =  sprite_paths_array
            for file_path in self.walk_path_array:
                self.set_file_path_name(file_path)
                self.set_surface_image()
                self.temp_array.append(self.image)
            self.sprite_images_dict[sprite_paths_name] = self.temp_array.copy()
            print(f' dict: {self.sprite_images_dict[sprite_paths_name]}: ', sprite_paths_name )
            self.temp_array.clear()
        self.update_current_sprite('idle')
    
    def get_collide_rect(self, colliding_group):
        collision = pg.sprite.spritecollide(self, colliding_group, False, pg.sprite.collide_mask)
        if collision:
            print('collision detected ^^^^^^^^^^^^^^^^^^^^^^')