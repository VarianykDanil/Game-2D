import pygame
from models import Graphic

class Main_hero(Graphic):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def gravity(self,map_level1):
        
    def move_hero(self, map_level1):
        key = pygame.key.get_pressed()


main_hero = Main_hero(x = 50, y = 50, width = 64, height = 36, img_path = 'images/main_hero_image.png')


