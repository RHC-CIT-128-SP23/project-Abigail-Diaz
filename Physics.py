
class Physics:
    def __init__(self, rect): # had a rect as an argument
        self.rect = rect
        self.jump = False
        self.fall = False
        self.gravity = 0
        self.move_right = False
        self.move_left = False
        self.left_axis_movement = False
        self.direction = {"right": False, "left": False}
        self.current_direction = None
    def move(self): # place on constructor
        self.movement()
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
            if self.move_left:
                self.rect.x -= 3
            elif self.move_right:
                self.rect.x += 3
    def movement(self):
        if self.direction['right']:
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