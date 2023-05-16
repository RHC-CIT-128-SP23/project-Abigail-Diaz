
import pygame as pg
from Sprites import Sprite
from Rectangle import Rectangle
from Levels import *
import pytmx
from Enemy import Enemy
import random

tile_size = 64
screen_width, screen_length = 850, tile_size * len(level_map)


class Tile (pg.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pg.Surface((size, size))
        self.image.fill('grey')
        self.rect = self.image.get_rect(topleft = pos)

    def get_tile_position(self):
        return (self.rect.x, self.rect.y)
    
    def get_tile_rect(self):
        return self.rect
    
    def update(self, x_shift):
        self.rect.x += x_shift


class Level:
    def __init__(self, surface):
        self.surface = surface
        self.setup_level(level_map)
        self.background = pg.image.load('media/Galaxy12.jpg').convert()
        self.background = pg.transform.smoothscale(self.background, (screen_width, screen_length))
        self.shift = 0
        

    def setup_level(self, layout):
        self.tiles = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                if col == 'x':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                if col == 'E':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    enemy = Enemy(x, y, 50, 50)
                    self.enemies.add(enemy)

    def set_next_layout(self):
        pass

    def run(self):
        self.enemies.update(-2) 
        self.surface.blit(self.background, (0, 0))
        self.tiles.draw(self.surface)
        self.enemies.draw(self.surface)
        self.respawn()
    
    def get_collision_coordinate(self, sprite):
        self.x_collision = 0
        self.y_collision = 0
        for tiles in self.tiles:
            if pg.sprite.collide_mask(sprite, tiles):
                self.x_collision, self.y_collision = tiles.get_tile_position()
        return (self.x_collision, self.y_collision)
    
    def get_collision_rect(self, sprite):
        self.collision_rect = None
        for t in self.tiles:
            if t.rect.colliderect(sprite.rect):
                self.collision_rect = t.get_tile_rect()
                return self.collision_rect
    def get_enemy_collision_rect(self, sprite):
        self.collision_rect = None
        for t in self.enemies:
            if t.rect.colliderect(sprite.rect):
                self.collision_rect = t.get_enemy_rect()
                return self.collision_rect

    def move_screen_forward(self, x_shift):
        self.tiles.update(x_shift)
    
    def get_enemy_collision(self, obj):
        collision = pg.sprite.spritecollide(obj, self.enemies, False, pg.sprite.collide_mask)
        collision_rect = self.get_collision_rect(obj)

        # left collision
        if obj.rect.x < collision_rect.x:
            collision_type = 1
        if obj.rect.x < collision_rect.x:
            collision_type = 2

        return (collision, collision_type)
    
    def respawn(self):
        if len(self.enemies) > 1:
            self.list_of_alive_sprites = self.enemies.sprites()

            # check if enemy sprite is out of range
            for sprite in self.list_of_alive_sprites:
                if sprite.rect.x < 0:
                    print('enemy gone out of range')
                    self.enemies.remove(sprite) # remove if out of range
        else:
            print('empty')
            for num in range(20):
                rand = random.randint(200, 500)
                rand2 = random.randint(800, 1000)
                enemy = Enemy(rand2, rand, 50, 50)
                self.enemies.add(enemy)
