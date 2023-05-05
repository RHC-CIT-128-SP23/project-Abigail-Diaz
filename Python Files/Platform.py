from Rectangle import Rectangle
import pygame as pg

class Platform(Rectangle):
    def __init__(self, file_name, image_width, image_length):
        super().__init__(file_name, image_width, image_length)
        self.collision = False
        self.recent_platform_collide = False
    def platform_collision(self, other_rect):
        self.collision = self.rect.colliderect(other_rect.rect)
        # Keep character on top of platform
        if self.collision == True:
            print('collision!')
            other_rect.jump = False
            other_rect.rect.bottom = self.rect.top
            self.recent_platform_collide = True
            # falls when outside platform
        if (other_rect.rect.x > self.rect.x or other_rect.rect.x < self.rect.x) and self.recent_platform_collide == True:
            other_rect.jump = True
            other_rect.fall = True
            self.recent_platform_collide = False