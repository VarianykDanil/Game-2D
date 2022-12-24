import pygame
from models import Graphic, levels
import modules


class Main_hero(Graphic):
    def __init__(self, SPEED, **kwargs):
        super().__init__(**kwargs)
        self.current_level = 0
        self.SPEED = SPEED
        self.gravity_active = False
        self.jump_distance = 120
        self.isJump = False
           
    #def draw_previous_level(self):
    #    self.current_level -= 1
    #    list_objects, list_blocks = create_map(levels[self.current_level])
    #    self.rect.x = screen_width 
    #    return list_objects, list_blocks
    #    
    #def draw_next_level(self):
    #    self.current_level += 1
    #    list_objects, list_blocks = create_map(levels[self.current_level])
    #    self.rect.x = 0 - self.rect.width
    #    return list_objects, list_blocks
    #
    #def check_level_changing(self):
    #    if self.rect.x <= 0 - self.rect.width:
    #        list_objects, list_blocks = self.draw_previous_level()
    #        return list_objects, list_blocks
    #    if self.rect.x >= 1280 + self.rect.width:
    #        list_objects, list_blocks = self.draw_next_level()
    #        return list_objects, list_blocks

    #def changing_level(self, list_objects, list_blocks):
    #    if self.rect.x <= 0 - self.rect.width/2:
    #        print("P")
    #        self.current_level -= 1
    #        new_list_objects, new_list_blocks = modules.create_map(levels[self.current_level])
    #        self.rect.x = 1280 - self.rect.width/2
    #        return new_list_objects, new_list_blocks
    #    elif self.rect.x >= 1280 + self.rect.width/2:
    #        print("N")
    #        self.current_level += 1
    #        new_list_objects, new_list_blocks = modules.create_map(levels[self.current_level])
    #        self.rect.x = 0 + self.rect.width/2
    #        return new_list_objects, new_list_blocks
    #    else:
    #        return list_objects, list_blocks

    def move(self, list_blocks):
        

        keys = pygame.key.get_pressed()
        
         
           
        if keys[pygame.K_SPACE]:
            self.isJump = True
        if self.isJump == True:
            self.rect.y -= self.SPEED 
            self.jump_distance -= self.SPEED
            if self.jump_distance <= 0:
                self.isJump = False
                self.gravity_active = True
                self.jump_distance = 120 
        
                  
        if keys[pygame.K_a]:
            self.rect.x -= self.SPEED         
        if keys[pygame.K_d]:
            self.rect.x += self.SPEED  
        #Гравитация
        if self.gravity_active == True:
            self.rect.y += self.SPEED - 1

        


        for block in list_blocks:            
            if self.rect.colliderect(block.rect):
                if self.rect.right >= block.rect.left and self.rect.right <= block.rect.left + self.SPEED:
                    self.rect.right = block.rect.left
                if self.rect.left <= block.rect.right and self.rect.left >= block.rect.right - self.SPEED:
                    self.rect.left = block.rect.right
                if self.rect.top <= block.rect.bottom and self.rect.top >= block.rect.bottom - self.SPEED:
                    self.rect.top = block.rect.bottom
                if self.rect.bottom >= block.rect.top and self.rect.bottom <= block.rect.top + self.SPEED:
                    self.rect.bottom = block.rect.top
                    self.gravity_active = False
                    self.jump_distance = 120
                    self.isJump = False

        
        
        
               
        
main_hero = Main_hero(SPEED = 5, x = 500, y = 600, width = 70, height = 70, img_path = 'images/gribori/gribori_normal_right.png')


