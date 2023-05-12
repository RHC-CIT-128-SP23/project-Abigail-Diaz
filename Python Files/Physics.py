
import copy
import pygame as pg

class Physics:
    def __init__(self, rect): # had a rect as an argument , should have a rectangle object instead, passed
        self.rect = rect
        self.jump = False
        self.fall = True
        self.gravity = 0
        self.move_right = False
        self.move_left = False
        self.left_axis_movement = False
        self.velocity = 0
        self.direction = {"right": False, "left": False, 'down': True, 'up': False}
        #self.direction = pg.math.Vector2(0,0)
        self.current_direction = None
    
    def move(self): # place on constructor
        self.movement()
        self.check_if_jumping()
        self.falling()
    
    def falling(self):
        # Character will fall down as y values increase
        if self.fall == True:
            self.direction['up'] = False
            self.gravity += 0.5  # can make into a function
            self.rect.y += self.gravity # gravity is never set back to zero
    
    def check_if_jumping(self):

        # Character will move on the x axis as it completes the jump
        if self.jump == True:
            self.fall = True # can add fall function here
            #self.gravity += 1
            #self.rect.y += self.gravity
            self.direction['down'] = True
            if self.move_left:
                #self.rect.x -= 5
                pass
            elif self.move_right:
                #self.rect.x += 5
                pass
    
    def make_jump(self):
        self.jump = True
        self.direction['up'] = True
        self.gravity = -10
    
    def stop_jump(self):
        self.jump = False
    
    def make_fall(self):
        self.fall = True
    
    def stop_fall(self):
        self.fall = False
    
    def stop(self):
        for key in self.direction:
            self.direction[key] = False

    def movement(self):
        if self.move_right:
            #self.rect.x += 2
            pass
        if self.move_left == True:
            #self.rect.x -= 2
            pass

    def floor_reached(self, floor):
        '''check if cat reached the floor # Condition: If cat reached the floor, then it must be false that he is jumping'''
        if self.rect.bottom >= floor: 
            self.rect.bottom = floor
            self.jump = False
    
    def range_reached(self, screen_width, screen_lenght, new_pos):
        '''Reset cat position the the start (left) of the screen if it goes out of the screen's range'''
        if self.rect.left > screen_width:  
            self.rect.x = new_pos
    
    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y
    
    def repel_to_left(self):
        '''Repel character to the left by decreasing x value '''
        print('left repelled')
        self.rect.x -= 5
     

    def repel_to_right(self):
        '''Repel character to the righ by increasing x value'''
        print('right repelled')
        self.rect.x += 5
       
    
    def repel_down(self):
        '''Repel character down by incresing its y value'''
        print('down repelled')
        self.rect.y += 10
        self.fall = True

    def collision_data(self, collision_rect):
        # left side of cat in between the rect
        self.left_in_between = self.rect.left > collision_rect.left and self.rect.left < collision_rect.right

        # right side of cat in between the rect
        self.right_in_between = self.rect.right > collision_rect.left and self.rect.right < collision_rect.right

        self.on_floor = (self.rect.bottom < collision_rect.bottom) and (self.left_in_between or self.right_in_between)

        if self.on_floor:
            print('on floor: ', self.on_floor)