#!/usr/bin/env python3
'''
    Rio Hondo College
    CIT 128: Python Programming II
    Student Directed Project
'''

import pygame as pg
import sys

class Surface:
    def __init__(self, file_name, image_width, image_length):
        self.file_name = file_name
        self.image_width = image_width
        self.image_length = image_length
        self.set_surface_image()
        self.surf_image = self.get_image()
    # Import images
    def set_surface_image(self):
        self.surf_image = pg.image.load(self.file_name).convert_alpha()
        self.resize_image()
    def get_image(self):
        return self.surf_image
    def resize_image(self):
        self.surf_image = pg.transform.smoothscale(self.surf_image, (self.image_width, self.image_length))
    
class Rectangle (Surface):
    def __init__(self, file_name, image_width, image_length):
        super().__init__(file_name, image_width, image_length)
        self.rectangle = self.get_rectangle()
        self.physics = Physics(self.rectangle)
    def get_rectangle(self): # create the rectangles of each surface
        self.image = self.surf_image
        return self.image.get_rect(midbottom = (0, 420 + 30)) #fix vague numbers
    def set_position(self, x, y):
        self.rectangle.x = x
        self.rectangle.y = y
    def set_fall(self, boolean_factor):
        self.physics.fall = boolean_factor

class Physics:
    def __init__(self, rect):
        self.rect = rect
        self.jump = False
        self.fall = False
        self.gravity = 0
        self.move_right = False
        self.move_left = False
    def move(self):
        self.y_axis_movement()
        self.make_jump()
        self.falling()
    def falling(self):
        # Character will fall down as y values increase
        if self.fall == True:
            self.gravity += 1  # can make into a function
            self.rect.y += self.gravity
    def make_jump(self):
        # Character will move on the x axis as it completes the jump   
        if self.jump == True:
            self.fall = False # can add fall function here
            self.gravity += 1
            self.rect.y += self.gravity
        #if self.move_right == True:
            self.rect.x += 3
        #if self.move_left:
        #    self.rect.x += 3
    def y_axis_movement(self):
        if self.move_right == True:
            self.rect.x += 2
        if self.move_left == True:
            self.rect.x -= 2
    def floor_reached(self, floor):
    # check if cat reached the floor # Condition: If cat reached the floor, then it must
    # be false that he is jumpin
        if self.rect.bottom >= floor: 
            self.rect.bottom = floor
            self.jump = False
    def range_reached(self, screen_width, screen_lenght, new_pos):
        if self.rect.left > screen_width:  
            self.rect.x = new_pos
    
class Platform(Rectangle):
    def __init__(self, file_name, image_width, image_length):
        super().__init__(file_name, image_width, image_length)
        self.collision = False
        self.recent_platform_collide = False
    def platform_collision(self, other_rect):
        self.collision = pg.Rect.colliderect(other_rect.rectangle, self.rectangle)
        # Keep character on top of platform
        if self.collision:
            other_rect.physics.jump = False
            other_rect.rectangle.bottom = self.rectangle.top
            self.recent_platform_collide = True
            self.collision = pg.Rect.colliderect(other_rect.rectangle, self.rectangle)
            # falls when outside platform
        if other_rect.rectangle.x > self.rectangle.x and self.recent_platform_collide == True:
            other_rect.physics.jump = True
            self.recent_platform_collide = False

# start pygame
pg.init()

screen_width, screen_length = 850, 420
floor = 420

# Set window display
screen = pg.display.set_mode((screen_width, screen_length))
pg.display.set_caption('Space Cat')
clock = pg.time.Clock()

# Import background
background = pg.image.load('media/background3Medium.jpeg').convert()

# create the rectangles of each surface
platform = Platform('media/ground.png', 90, 50)
cat = Rectangle('media/cat.png', 80, 80)
bat = Rectangle('media/bat-x1.gif', 80, 80)

platform.set_position(screen_width/2, screen_length/2)
bat.set_position(screen_width, floor - 10)

# Cat Actions
recent_platform_collide = False

# Assume game is running
running = True

while running:
    for event in pg.event.get():
        if event.type ==  pg.QUIT:
            pg.quit()
            sys.exit()
    
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                cat.physics.gravity = -20
                #player_gravity = -20  # make a physics.gravity.cat (a physics class that takes an object from the rectangle class)
                #cat_jump = True         # as an argument
                cat.physics.jump = True
        
        # move cat right with -> key
        if event.type ==  pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                cat.physics.move_right = True      # number of steps to the right
                cat.physics.move_left = False
            elif event.key == pg.K_LEFT:
                cat.physics.move_left = True
                cat.physics.move_right = False
        
        if event.type == pg.KEYUP:
            if event.key == pg.K_RIGHT or event.key == pg.K_LEFT:
                #stop the cat
                cat.physics.move_right = False
                cat.physics.move_left = False

    # Display the background on the window
    screen.blit(background, (-100, 0))
    screen.blit(background, (0, 0))
    screen.blit(background, (100, 0))
    screen.blit(background, (550 , 0))
    
    #Display Platform
    screen.blit(platform.image, platform.rectangle)
    
    # Check for user actions
    cat.physics.move()
    
    # Check for collision with platform
    platform.platform_collision(cat)
    
    # check if cat reached the floor
    cat.physics.floor_reached(floor)
    
    # check if the cat goes out of the screen's range
    cat.physics.range_reached(screen_width, screen_length, 0)
    
    # Display Cat Character
    screen.blit(cat.image, cat.rectangle)
    
    # Bat movements: Moves from left to right
    bat.rectangle.right -= 1
    screen.blit(bat.image, bat.rectangle)
    
    # check if the bat goes out of the screen's range    
    if bat.rectangle.left < 0:
        bat.rectangle.left = screen_width
    
    #update screen
    pg.display.flip()
    clock.tick(60)