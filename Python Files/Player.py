from Sprites import Sprite
from Physics import Physics
from Counter import Counter
import pygame as pg



class Player(Sprite):
    def __init__(self, posx, posy, image_width, image_length, level, screen):
        self.level = level
        self.screen = screen
        self.initial_posx = 120
        self.initial_posy = 270
        self.rect = pg.Rect(posx, posy, image_width, image_length)
        self.action_array = ['idle', 'walk',  'damage']
        super().__init__(self.rect, image_width, image_length, self.action_array )
        self.visible = True
        self.physics = Physics(self, level)
        self.counter = Counter(screen, self, level)

    def restart(self):
        # move character back to starting position
        self.rect.x = self.initial_posx
        self.rect.y = self.initial_posy
        self.counter.won = False
        self.visible = True
        
    def run(self):
        '''Start the character's main functions'''

        # check if the win or lost window is being displayed
        if self.visible:
            # Display player
            self.screen.blit(self.image, self.rect)

        # Update the animation
        self.update_sprite()

        # Start the physics function
        self.physics.run()

        # check if there is a collision with an enemy object
        self.physics.collision_check()

        # check if the cat goes out of the screen's range
        self.physics.range_reached()

    def won(self):
        self.counter.won = True
        self.visible = False

