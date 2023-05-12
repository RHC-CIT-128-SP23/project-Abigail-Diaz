from Sprites import Sprite
import pygame as pg

class Enemy(pg.sprite.Sprite):
    def __init__(self, posx, posy, image_width, image_length):
        super().__init__()
        #self.image = pg.Surface((size, size))
        #self.image.fill('grey')
        #self.rect = self.image.get_rect(topleft = pos)

        self.image = None
        self.current_sprite = 0
        #self.image_paths_dict = image_paths_dict
        self.set_image_paths_dict()
        self.sprite_images_dict = {'idle': None}
        self.current_sprite_array = []
        self.image_width = image_width
        self.image_length = image_length
        self.rect = pg.Rect(posx, posy, image_width, image_length)
        self.update_spr = True
        # create rectangle as soon as object is made with the first image on the list
        self.initialize_sprite_dict()
        self.mask = pg.mask.from_surface(self.image)
    
    def walk(self): # rename set to walk animation
        pass

    def set_rectangle(self, rect):
        self.rect = rect
    def update_rectangle(self):
        return self.get_updated_rect()
    
    def set_position(self, x, y): # should put in sprite class? physics?
        self.rect.x = x
        self.rect.y = y

    def get_rectangle(self, image): # create the rectangles of each surface
        return image.get_rect()
    
    def get_image_paths_array(self):
        self.image_file_paths = []
        for item in range(3):
            self.image_file_paths.append(f'media/eye_{item + 1}.png')
        return self.image_file_paths
    
    def set_image_paths_dict(self):
        self.image_paths_dict = {'idle': None}
        self.image_paths_dict['idle'] = self.get_image_paths_array()


    def update_current_sprite(self, action):
        self.current_sprite = 0
        if action == 'idle':
            self.current_sprite_array = self.sprite_images_dict['idle']
            #print('idle')
            
        if action == 'walk': #not usable
            self.current_sprite_array = self.sprite_images_dict['walk']

    def update_sprite(self): 
        '''Updates the sprite image when called'''
        if self.update_spr:
            if self.current_sprite < len(self.current_sprite_array) - 1: #-1
                self.current_sprite += 0.2
            else:
                self.current_sprite = 0
        #print('current sprite: ', self.current_sprite)
        #print('array: ',self.current_sprite_array)
        self.image = self.current_sprite_array[int(self.current_sprite)]
        #self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
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
        '''Assigns the animation images from array image_paths to local array image_paths'''
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
    
    def get_tile_rect(self):
        return self.rect