import pygame
from models import Graphic


class Main_hero(Graphic):
    def __init__(self, speed, **kwargs):
        super().__init__(**kwargs)
        self.SPEED = speed

    def gravity(self,map_level1):
        pass

    def collision_right(self,list_blocks):
        for list_b in list_blocks:
            if self.X + self.WIDTH >= list_b.X and self.Y >= list_b.Y or self.X + self.WIDTH >= list_b.X and self.Y + self.HEIGHT >= list_b.Y:
                self.MOVE_RIGHT = False  
            else:
                self.MOVE_RIGHT = True     

    def collision_left(self,list_blocks):
        for list_b in list_blocks:
            if self.X <= list_b.X + list_b.WIDTH and self.Y >= list_b.Y or self.X <= list_b.X + list_b.WIDTH and self.Y + self.HEIGHT >= list_b.Y:
                self.MOVE_LEFT = False
            else:
                self.MOVE_LEFT = True 

    def move_hero(self, list_blocks):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.Y -= self.SPEED
            
        if keys[pygame.K_s]:
            self.Y += self.SPEED 

        if keys[pygame.K_a]:
            self.collision_left(list_blocks)
            if self.MOVE_LEFT == True:
                self.X -= self.SPEED   

        if keys[pygame.K_d]:
            self.collision_right(list_blocks)
            if self.MOVE_RIGHT == True:
                self.X += self.SPEED
        
           
            
            
main_hero = Main_hero(speed = 1, x = 50, y = 25, width = 35, height = 60, img_path = 'images/main_hero_image.png')


