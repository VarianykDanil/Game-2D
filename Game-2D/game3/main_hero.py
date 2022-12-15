import pygame
from models import Graphic

class Main_hero(Graphic):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.COOR = [2,1]
        self.DISTANCE_H = 0
        self.DISTANCE_V = 0 
    def gravity(self,map_level1):
        if map_level1[self.COOR[0]+1][self.COOR[1]] == '0':
            map_level1[self.COOR[0]][self.COOR[1]] = '0'
            map_level1[self.COOR[0]+1][self.COOR[1]] = 'h'
            self.Y += 36
            self.COOR[0]+=1
    def move_hero(self, map_level1):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            if map_level1[self.COOR[0]][self.COOR[1]-1] == '0' or self.DISTANCE_H != 0:
                self.X -= 2
                self.DISTANCE_H -= 2
                if self.DISTANCE_H == -64:
                    map_level1[self.COOR[0]][self.COOR[1]] = '0'
                    map_level1[self.COOR[0]][self.COOR[1]-1] = 'h'
                    self.COOR[1]-=1
                    self.DISTANCE_H = 0
        if key[pygame.K_d]:
            if map_level1[self.COOR[0]][self.COOR[1]+1] == '0' or self.DISTANCE_H != 0:
                self.X += 2
                self.DISTANCE_H += 2
                if self.DISTANCE_H == 64:
                    map_level1[self.COOR[0]][self.COOR[1]] = '0'
                    map_level1[self.COOR[0]][self.COOR[1]+1] = 'h'
                    self.COOR[1]+=1
                    self.DISTANCE_H = 0
        if key[pygame.K_SPACE]:
            if map_level1[self.COOR[0]-1][self.COOR[1]] == '0':
                map_level1[self.COOR[0]][self.COOR[1]] = '0'
                map_level1[self.COOR[0]-1][self.COOR[1]] = 'h'
                self.Y -= 36
                self.COOR[0]-=1
                
        print(self.COOR, self.X,self.DISTANCE_H)
        self.gravity(map_level1)

main_hero = Main_hero(x = 50, y = 50, width = 64, height = 36, img_path = 'images/main_hero_image.png')


