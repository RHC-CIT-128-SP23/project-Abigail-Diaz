
import pygame as pg

class Counter:
    def __init__(self, screen):
        self.image = pg.image.load('media/bar.png').convert_alpha()
        self.heigth = 50
        self.length = 100
        self.image = pg.transform.smoothscale(self.image, (self.length, self.heigth))
        self.screen = screen
    
    def run(self):
        self.screen.blit(self.image, (400, 100))
        
    def collision(self):
        self.update_size()

    def update_size(self):
        self.length -= 10
        if self.length < 0:
            print('dead')
        else:
            self.image = pg.transform.smoothscale(self.image, (self.length, self.heigth))