from Sprites import Sprites

class Enemy(Sprites):
    def __init__(self, image_paths, image_width, image_length):
        super().__init__(image_paths, image_width, image_length)
        self.initial_position = 900

    def move(self):
        # Moves from left to right
        self.rect.right -= 1
        if self.max_range_reached():
            self.rect.x = self.initial_position

    def max_range_reached(self):
        if self.rect.x < 0:
            return True
        return False