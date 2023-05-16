import pygame as pg

from Sprites import Sprite

class Fire(Sprite):
    def __init__(self, image_width, image_length, shooting_obj):
        #pg.sprite.Sprite.__init__(self)
        self.set_image_paths_dict()
        #self.fire_sprite_group = pg.sprite.Group()
        self.shooting_obj = shooting_obj
        
        self.posx, self.posy = shooting_obj.rect.center
        #self.posy = shooting_obj.rect.y
        self.rect = pg.Rect(self.posx - 10, self.posy - 20, image_width, image_length)
        Sprite.__init__(self, self.rect, self.posx, self.posy, image_width, image_length, self.image_paths_dict)
        

    def get_image_paths_array(self, path):
        self.image_file_paths = []
        for item in range(5):
            self.image_file_paths.append(f'{path}{item + 1}.png')
        return self.image_file_paths
    
    def set_image_paths_dict(self):
        self.image_paths_dict = {'idle': None} # add explode after test
        self.image_paths_dict['idle'] = self.get_image_paths_array(f'media/spark-preview')
        self.image_paths_dict['explode'] = self.get_image_paths_array(f'media/hits-1-')
    
    def update(self, option = '', x_shift = 2):
        self.rect.x += x_shift
        self.update_sprite()
        if option == 'explode':
            self.update_current_sprite('explode')
    
    def get_collide_rect(self, colliding_group):
        collision = pg.sprite.spritecollide(self, colliding_group, False, pg.sprite.collide_mask)
        if collision:
            print('^^^^^^^^^^^^collision detected ^^^^^^^^^^^^^^^^^^^^^^')