
import pygame as pg
class Sound:
    def __init__(self):
        self.background_sound = pg.mixer.Sound('media/Battle in the Stars.ogg')
        self.background_sound.set_volume(0.01)
        self.shot_sound = pg.mixer.Sound('media/shot.wav')
        self.shot_sound.set_volume(.5)

    def play_background_music(self):
        pg.mixer.Channel(0).play(pg.mixer.Sound(self.background_sound))
    
    def play_shot_sound(self):
        pg.mixer.Channel(1).play(pg.mixer.Sound(self.shot_sound))