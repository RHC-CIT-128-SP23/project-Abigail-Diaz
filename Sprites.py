from Rectangle import Rectangle

class Sprites(Rectangle):
    def __init__(self, image_paths, image_width, image_length):
        super().__init__(image_width, image_length)
        self.sprites = []
        self.current_sprite = 0
        self.image_paths = image_paths
        self.initialize_sprite()
    
    def initialize_sprite(self):
        for name in self.image_paths:
            self.file_name = name
            self.set_surface_image()
            self.resize_image(self.image_width, self.image_length)
            self.sprites.append(self.get_image())

        self.surf_image = self.sprites[self.current_sprite] #updated image 
        #self.resize_image(100, 100)## repeated????
        self.set_rectangle(self.surf_image)
    
    def update_sprite(self): 
        if self.update_spr:
            if self.current_sprite < len(self.sprites) - 1:
                self.current_sprite += 0.2
            else:
                self.current_sprite = 0
            self.surf_image = self.sprites[int(self.current_sprite)]