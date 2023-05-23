
import pygame as pg

class Physics:
    '''Manages player's movements and checks for collisions'''
    def __init__(self, player, level):
        self.player = player
        self.rect = player.rect
        self.level = level
        self.jump = False
        self.fall = True
        self.gravity = 0
        self.move_right = False
        self.move_left = False
        self.left_axis_movement = False
        self.velocity = 0
        self.direction = {"right": False, "left": False, 'down': True, 'up': False}
        self.current_direction = None
        self.on_floor_counter = 0
        self.non_col = 0
    
    def run(self):
        '''check player's actions'''
        self.horizontal_movement()
        self.jumping()
        self.falling()
    
    def horizontal_movement(self):
        '''Moves player left or right'''
        if self.move_right and self.player.rect.x < 300:
            self.rect.x += 3
            
        if self.move_left:
            self.rect.x -= 1

    def jumping(self):
        # Character will move on the x axis as it completes the jump
        if self.jump:
            self.fall = True 

            if self.move_left:
                self.rect.x -= 5
                
            elif self.move_right:
                self.level.move_screen_forward(-2)

    def falling(self):
        # Character will fall down as y value of rect increase
        if self.fall:
            self.gravity += 1
            self.rect.y += self.gravity 
    
    def make_jump(self):
        self.jump = True
        self.gravity = -15

    def stop_jump(self):
        self.jump = False
    
    def make_fall(self):
        self.fall = True
    
    def stop_fall(self):
        self.fall = False
    
    
    def floor_reached(self, floor):
        '''Keep player on the floor'''

            # prevent player from falling through the tiles
        if self.rect.bottom >= floor: 
            self.rect.bottom = floor
            self.jump = False                                                                                                  
    
    def range_reached(self):
        '''Reset cat position to the the start (left) of the screen if it goes out of the screen's range'''
        if self.rect.left < 0:  
            self.rect.x = 25
    
    def repel_to_left(self):
        '''Repel player to the left by decreasing x value '''
        self.rect.x -= 5

    def repel_to_right(self):
        '''Repel player to the right by increasing x value'''
        self.rect.x += 5

    def repel_down(self):
        '''Repel player down by increasing its y value'''
        print('down repelled')
        self.rect.y += 10
        self.fall = True

    
    def check_flag_collision(self):
        if self.player.visible:
            self.flag_collision = pg.sprite.spritecollide(self.player, self.level.flags, False, pg.sprite.collide_mask)
        
        if self.flag_collision:
            self.player.counter.menu.won_menu()
            self.player.won()
            

    def collision_check(self):

        left_collision = False

        '''Collision check with flag'''
        self.check_flag_collision()
        
        '''Collision Checks with enemy'''

        enemy_collision = pg.sprite.spritecollide(self.player, self.level.enemies, False, pg.sprite.collide_mask)
        enemy_rect_collision = self.level.get_enemy_collision_rect(self.player)
        if enemy_collision:
            if self.rect.x < enemy_rect_collision.x:
                self.player.update_current_sprite('damage')
                self.rect.x -= 20
            if self.rect.x > enemy_rect_collision.x: # replace with else?
                self.player.update_current_sprite('damage')
                self.rect.x += 20
            self.player.counter.collision()

        collision = pg.sprite.spritecollide(self.player, self.level.tiles, False, pg.sprite.collide_mask)

        if self.direction['right'] and self.player.rect.x >= 300 and left_collision == False:# and cat.rect.x > 200
            self.level.move_screen_forward(-2) 

        if collision:
            self.gravity = 0
            self.non_col = 0
            self.fall = False
            self.jump = False                                                                                             
            
            collision_rect = self.level.get_collision_rect(self.player)
    
            # Upon collision, check if cat is on top of a rectangle
            if  ((self.player.rect.left < collision_rect.right or self.player.rect.right > collision_rect.left) and ((abs(self.rect.bottom - collision_rect.top) < 50))):
                self.fall = False
                self.on_floor_counter += 1
            
                # Collision with the floor
                if (abs(self.rect.bottom - collision_rect.top)) < 50:
                    self.rect.bottom = collision_rect.top + 0.5

            elif  ((self.rect.left < collision_rect.right or self.rect.right > collision_rect.left) and (abs(self.rect.top - collision_rect.bottom) < 20)):
                self.repel_down()
        
            elif collision_rect.right > self.rect.right and (self.rect.bottom > collision_rect.top):
                self.fall = False
                self.on_floor_counter = 0
                self.repel_to_left()
                left_collision = True
        
            elif collision_rect.left < self.rect.left and (self.rect.bottom > collision_rect.top):
                self.repel_to_right()
                self.on_floor_counter = 0
                self.fall = False

        else:
            # prevents non-intended fall from becoming true when else becomes true for a moment
            # to avoid alternation between else and floor collision, so fall does not become true while being on the floor
            if self.non_col > 4: 
                self.fall = True
            self.non_col += 1