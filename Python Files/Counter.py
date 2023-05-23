
import pygame as pg
from Menu import Menu


class Counter():
    def __init__(self, screen, player, level):
        self.flag_width = 50
        self.flag_height = 50
        self.posx = 500
        self.posy = 409
        self.health_bar_posx = screen.get_width() - 150
        self.health_bar_posy = screen.get_height() - (screen.get_height() - 10)
        self.set_image_paths_dict()
        self.health_bar_height = 20
        self.initial_health_bar_length = 100
        self.health_bar_length = self.initial_health_bar_length
        self.original_image = pg.image.load('media/bar.png').convert_alpha()
        self.original_image = pg.transform.smoothscale(self.original_image, (self.health_bar_length, self.health_bar_height))
        self.red_block = pg.Surface((self.health_bar_length, self.health_bar_height))
        self.red_block.fill('red')
        self.lost = False
        self.won = False
        self.player = player
        self.green_bar_image = self.original_image
        self.screen = screen
        self.menu = Menu(screen)
        self.level = level
        self.flag_rect = pg.Rect(self.posx, self.posy, self.flag_width, self.flag_height)
    
    def run(self):
        self.check_lost() 
        self.screen.blit(self.red_block, (self.health_bar_posx, self.health_bar_posy))
        self.screen.blit(self.green_bar_image, (self.health_bar_posx, self.health_bar_posy))
        
    def collision(self):
        self.update_size()

    def update_size(self): 
        '''Reduce the length of the green health bar'''
        
        # reduce health bar length
        self.health_bar_length -= 10

        # check if health bar has run out of length
        if self.health_bar_length < 0:
            print('dead')
            self.lost = True
            self.player.physics.fall = False
            
        else:
            self.green_bar_image = pg.transform.smoothscale(self.original_image, (self.health_bar_length, self.health_bar_height))

    
    def check_lost(self):
        '''Check if player has either fallen off the screen or if lost'''
        
        # check if player has fallen off a cliff, update to 'lost' status if true
        if self.player.rect.y > 1000:
            self.lost = True
            self.player.physics.fall = False

            self.level.restart()
            self.player.restart()
        
        # check if player has lost 
        if self.lost:
            self.menu.restart_menu()
    

    def restart(self):
        self.lost = False
        self.health_bar_length = self.initial_health_bar_length
        self.green_bar_image = pg.transform.smoothscale(self.original_image, (self.health_bar_length, self.health_bar_height))
        

    def get_image_paths_array(self, path):
        self.image_file_paths = []
        for item in range(5):
            self.image_file_paths.append(f'{path}{item + 1}.png')
        return self.image_file_paths
    
    def set_image_paths_dict(self):
        self.image_paths_dict = {'idle': None} 
        self.image_paths_dict['idle'] = self.get_image_paths_array(f'media/flag_')
        