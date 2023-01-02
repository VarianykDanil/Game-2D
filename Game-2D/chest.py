from models import Graphic, levels
from random import randint
from models import *
import pygame

class Drop(Graphic):
    def __init__(self, type, **kwargs):
        super.__init__(**kwargs)
        self.type = type

class Chest(Graphic):
    def __init__(self, drop_dict, **kwargs):
        super.__init__(**kwargs)
        self.drop_dict = {
            1 : "health_kit",
            2 : "nothing"    
            }

        def cheast_opening(main_hero):
            keys = pygame.key.get_pressed()

            if self.rect.coliderect(main_hero):
                if keys[pygame.K_e]:
                    pass


        def random_drop(random,):
            a = random.randint(1,2)
            if a == 1:
                pass



