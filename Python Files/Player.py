from Sprites import Sprite
import pygame as pg

class Player(Sprite):
    def __init__(self, posx, posy, image_width, image_length, image_paths_dict):
        self.fire_sprite_group = pg.sprite.Group() 
        self.rect = pg.Rect(posx, posy, image_width, image_length)
        super().__init__(self.rect, posx, posy, image_width, image_length, image_paths_dict)