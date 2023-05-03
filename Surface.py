import pygame as pg
import sys

class Surface:
    def __init__(self, image_width, image_length, file_name = ''):
        self.file_name = file_name
        self.image_width = image_width
        self.image_length = image_length
        self.surf_image = None 
    # Import images
    def set_surface_image(self):
        self.surf_image = pg.image.load(self.file_name).convert_alpha()
    def get_image(self):
        return self.surf_image
    def resize_image(self, image_width = 80, image_length = 80):
        self.surf_image = pg.transform.smoothscale(self.surf_image, (image_width, image_length))