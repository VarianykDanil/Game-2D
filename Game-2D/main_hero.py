import pygame
from models import Graphic
#from modules import *

class Main_hero(Graphic):
    def __init__(self, speed, **kwargs):
        super().__init__(**kwargs)
        self.SPEED = speed

    def gravity(self,map_level1):
        pass
    def move_hero(self, map_level1):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.Y -= self.SPEED
        if keys[pygame.K_s]:
            self.Y += self.SPEED
        if keys[pygame.K_a]:
            self.X -= self.SPEED
        if keys[pygame.K_d]:
            self.X += self.SPEED
    
    # def collision_right(self):
    #     if self.X + self.block_width >= ,,,.X:
    #         if self.Y == ,,,.Y and self.Y + self.block_height == ,,,.Y + ,,,.block_height:


        



main_hero = Main_hero(speed = 5, x = 50, y = 25, width = 35, height = 61, img_path = 'images/main_hero_image.png')


