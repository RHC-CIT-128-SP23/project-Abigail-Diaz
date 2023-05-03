from Surface import Surface
from Physics import Physics
import pygame as pg

class Rectangle (Surface, pg.sprite.Sprite, Physics):
    def __init__(self, image_width, image_length):
        Surface.__init__(self, image_width, image_length)
        self.rect = None
        #self.set_rectangle(self.surf_image)
        Physics.__init__(self, self.rect)
        self.update_spr = False

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def set_rectangle(self, surf_image): # create the rectangles of each surface
        self.rect = surf_image.get_rect() #fix vague numbers
    