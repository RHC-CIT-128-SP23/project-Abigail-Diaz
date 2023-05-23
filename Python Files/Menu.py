from Platform import screen_width, screen_length


import pygame as pg

class Menu:
    def __init__(self, screen):
        self.start = True
        self.screen = screen
        green = (0, 255, 0)
        blue = (0, 0, 128)
        purple = (128, 0, 128)
        self.font = pg.font.Font('freesansbold.ttf', 32)
        self.blue_square_width = 300
        self.blue_square_length = 300
        self.blue_square_posx = screen_width/2 - 150
        self.blue_square_posy = screen_length/3
        self.restart = pg.image.load('media/restart.png').convert_alpha()
        self.restart = pg.transform.smoothscale(self.restart, (self.blue_square_width/2, 50))
        self.restart_rect = self.restart.get_rect()
        self.start_text = self.font.render('Start', True, green, blue)
        self.start_text_rect = self.start_text.get_rect()
        
        self.text = self.font.render('You lose!', True, green, blue)
        self.textRect = self.text.get_rect()

        self.win_text = self.font.render('You won!', True, purple, blue)
        self.win_text_rect = self.win_text.get_rect()

        self.blue_square = pg.Surface((self.blue_square_width, self.blue_square_length))
       # self.blue_square2 = pg.Surface((self.blue_square_width, self.blue_square_length))
        self.blue_square.fill('blue')
        #self.blue_square2.fill('blue')
        

        self.restart_posx = self.blue_square_posx + self.blue_square_width/4
        self.restart_posy = self.blue_square_posy + self.blue_square_length/2
        self.restart_rect.x = self.restart_posx
        self.restart_rect.y = self.restart_posy
        self.start_text_rect.x = self.restart_posx
        self.start_text_rect.y = self.restart_posy
        
        self.loosing_message_posx = self.blue_square_posx + self.blue_square_width/4
        self.loosing_message_posy = self.blue_square_posy + self.blue_square_length/4
        self.textRect.topleft = (self.loosing_message_posx - 10, self.loosing_message_posy)

        self.win_text_rect.topleft = (self.loosing_message_posx - 10, self.loosing_message_posy)

    def start_menu(self):
        if self.start:
            print('start menu') 
            self.screen.blit(self.blue_square, (self.blue_square_posx, self.blue_square_posy))
            self.screen.blit(self.start_text, self.start_text_rect)
    
    def restart_menu(self): 
        self.screen.blit(self.blue_square, (self.blue_square_posx, self.blue_square_posy))
        self.screen.blit(self.restart, self.restart_rect)
        self.screen.blit(self.text, self.textRect)

    def won_menu(self):
        '''Menu announces player has won and allows for a restart'''
        self.screen.blit(self.blue_square, (self.blue_square_posx, self.blue_square_posy))
        self.screen.blit(self.restart, self.restart_rect)
        self.screen.blit(self.win_text, self.win_text_rect)
    
    