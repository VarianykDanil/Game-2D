import pygame
from models import Graphic, levels
import modules



class Main_hero(Graphic):
    def __init__(self, SPEED, **kwargs):
        super().__init__(**kwargs)
        self.current_level = 0
        self.current_underlevel = 0
        self.hp = 100
        self.damage = 10
        self.main_hero_looks = 'R'
        self.SPEED = SPEED
        self.gravity_active = False
        self.jump_distance = 130
        self.isJump = False
        self.isWalk = False
        self.isAttack = False
        self.walk_counter = 0
        self.attack_counter = 0

        self.leave_x = None
        self.leave_y = None
        self.leave_level = None

        self.img_rect = pygame.Rect(0,0,64,72)

        self.list_walk_right = [
    'images/gribori/walk_r_1.png',
    'images/gribori/walk_r_2.png',
    'images/gribori/walk_r_3.png',
    'images/gribori/walk_r_4.png',
    'images/gribori/walk_r_5.png',
    'images/gribori/stay_r.png'
] 
        self.list_walk_left = [
    'images/gribori/walk_l_1.png',
    'images/gribori/walk_l_2.png',
    'images/gribori/walk_l_3.png',
    'images/gribori/walk_l_4.png',
    'images/gribori/walk_l_5.png',
    'images/gribori/stay_l.png'
]
        self.list_attack_right = [
    'images/gribori/attack_r_1.png',
    'images/gribori/attack_r_2.png',
    'images/gribori/attack_r_3.png',
    'images/gribori/attack_r_4.png',
    'images/gribori/attack_r_5.png'
]
        self.list_attack_left = [
    'images/gribori/attack_l_1.png',
    'images/gribori/attack_l_2.png',
    'images/gribori/attack_l_3.png',
    'images/gribori/attack_l_4.png',
    'images/gribori/attack_l_5.png'
]
        
        self.list_health = [
    'images/health/hp_11.png',
    'images/health/hp_10.png',
    'images/health/hp_9.png',
    'images/health/hp_8.png',
    'images/health/hp_7.png',
    'images/health/hp_6.png',
    'images/health/hp_5.png',
    'images/health/hp_4.png',
    'images/health/hp_3.png',
    'images/health/hp_2.png',
    'images/health/hp_1.png'
]

    def load_image(self):
        self.IMAGE = pygame.image.load(self.IMG_PATH)
        self.IMAGE = pygame.transform.scale(self.IMAGE, (64,72))
    
    def show_image(self, window):
        if self.IMAGE != None:
            window.blit(self.IMAGE, (self.img_rect.x, self.img_rect.y))

    def health_bar(self):
        if self.hp < 9:
            self.IMG_PATH = self.list_health[self.hp//10]
            self.load_image()
        else:
            self.IMG_PATH = self.list_health[1]
            self.load_image()
        #elif self.hp >= 80 and self.hp < 90:
        #    self.IMG_PATH = self.list_health[1]
        #    self.load_image()
        #elif self.hp >= 70 and self.hp < 80:
        #    self.IMG_PATH = self.list_health[2]
        #    self.load_image()
        #elif self.hp >= 60 and self.hp < 70:
        #    self.IMG_PATH = self.list_health[3]
        #    self.load_image()
        #elif self.hp >= 50 and self.hp < 60:
        #    self.IMG_PATH = self.list_health[4]
        #    self.load_image()
        #elif self.hp >= 40 and self.hp < 50:
        #    self.IMG_PATH = self.list_health[5]
        #    self.load_image()
        #elif self.hp >= 30 and self.hp < 40:
        #    self.IMG_PATH = self.list_health[6]
        #    self.load_image()
        #elif self.hp >= 20 and self.hp < 30:
        #    self.IMG_PATH = self.list_health[7]
        #    self.load_image()
        #elif self.hp >= 10 and self.hp < 20:
        #    self.IMG_PATH = self.list_health[8]
        #    self.load_image()
        #elif self.hp >= 0 and self.hp < 10:
        #    self.IMG_PATH = self.list_health[9]
        #    self.load_image()
        #elif self.hp == 0:
        #    self.IMG_PATH = self.list_health[10]
        #    self.load_image()

    def animation_walk(self):
        self.walk_counter += 1
        if self.main_hero_looks == 'R':
            if self.walk_counter == 0:
                self.IMG_PATH = self.list_walk_right[-1]
                self.load_image()
            elif self.walk_counter < 25:
                self.IMG_PATH = self.list_walk_right[self.walk_counter//5]
                self.load_image()
            elif self.walk_counter >= 25:
                self.walk_counter = 0
        if self.main_hero_looks == 'L':
            if self.walk_counter == 0:
                self.IMG_PATH = self.list_walk_left[-1]
                self.load_image()
            elif self.walk_counter < 25:
                self.IMG_PATH = self.list_walk_left[self.walk_counter//5]
                self.load_image()
            elif self.walk_counter >= 25:
                self.walk_counter = 0

    def animation_attack(self):
        self.attack_counter += 1
        if self.main_hero_looks == 'R':
            if self.attack_counter < 50:
                self.IMG_PATH = self.list_attack_right[self.attack_counter//10]
                self.load_image()
            else:
                self.isAttack = False
                self.attack_counter = 0
        if self.main_hero_looks == 'L':
            if self.attack_counter < 50:
                self.IMG_PATH = self.list_attack_left[self.attack_counter//10]
                self.load_image()
            else:
                self.isAttack = False
                self.attack_counter = 0
    def move(self, list_blocks):

        self.img_rect.center = self.rect.center
        
        if self.isAttack == False:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE] and self.gravity_active == False:
                self.isJump = True
                self.gravity_active = False
                
    
            if self.isJump == True:
                self.rect.y -= self.SPEED*4
                self.jump_distance -= self.SPEED*4
                if self.jump_distance <= 0:
                    self.isJump = False
                    self.gravity_active = True
                    self.jump_distance = 130 

            
                      
            if keys[pygame.K_a]:
                self.main_hero_looks = 'L'
                self.rect.x -= self.SPEED
                self.animation_walk()
            if keys[pygame.K_d]:
                self.main_hero_looks = 'R'
                self.rect.x += self.SPEED
                self.animation_walk()
    
            if keys[pygame.K_a] == False and keys[pygame.K_d] == False:
                self.walk_counter = -1
                self.animation_walk()
            #Гравитация
            if self.gravity_active == True:
                self.rect.y += self.SPEED
            self.gravity_active = True
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
                        #self.gravity_active = False
                        self.jump_distance = 130
                        self.isJump = False

                if block.rect.collidepoint(self.rect.x, self.rect.bottom + 1):
                    self.gravity_active = False

            
                #if self.rect.colliderect(block.rect) == False:
                #    if self.isJump == False:
                #        if self.rect.bottom < block.rect.top and self.rect.bottom + block.rect.height < block.rect.bottom:#
                #            if self.rect.left <= block.rect.right and self.rect.right >= block.rect.left:
                #                self.gravity_active = True
            

    def attack(self):
        mouse = pygame.mouse.get_pressed()[0]
        if mouse or self.isAttack:
            self.isAttack = True
            self.animation_attack()


        
main_hero = Main_hero(SPEED = 5, x = 700, y = 500, width = 20, height = 72, img_path = 'images/gribori/stay_r.png')