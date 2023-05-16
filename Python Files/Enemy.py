from Sprites import Sprite
import pygame as pg

class Enemy(Sprite):
    def __init__(self, posx, posy, image_width, image_length):
        self.set_image_paths_dict()
        self.rect = pg.Rect(posx, posy, image_width, image_length)
        super().__init__(self.rect, posx, posy, image_width, image_length, self.image_paths_dict)
    
    def get_image_paths_array(self):
        self.image_file_paths = []
        for item in range(3):
            self.image_file_paths.append(f'media/eye_{item + 1}.png')
        return self.image_file_paths
    
    def set_image_paths_dict(self):
        self.image_paths_dict = {'idle': None}
        self.image_paths_dict['idle'] = self.get_image_paths_array()

    def update(self, x_shift):
        self.rect.x += x_shift
        self.update_sprite()

    def get_enemy_rect(self):
        return self.rect