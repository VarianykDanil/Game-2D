import pygame

# class Main_hero():
#     def __init__(self,x,y,width,height):
#         self.hp = 100
#         self.mana = 100
#         self.nick = "Гриборий" 
#         self.weapon = None
#        self.
#        # main_hero = pygame.Rect(640, 360, 50, 75)
#         self.RECT # Rect(x,y,width,height)
#     def move_hero(self):
#         # pygame нажатия с клавиатуры 
#           if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_f:
#                 game = False
#             if event.key == pygame.K_a:
#                 moving_left = True
#             if event.key == pygame.K_d:
#                 moving_right = True

#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_a:
#                 moving_left = False
#             if event.key == pygame.K_a:
#                 moving_right = False
        
#             if moving_left == True:
#                 main_hero.x -= 15
#             if moving_right == True:
#                 main_hero.x += 15
#         #method
#         pygame.draw.rect(screen, (255, 0, 0), main_hero)
      
# class Dammy():
#     def __init__(self):
#         self.health = 200

# class Enemy_trees():
#     def __init__(self,weapon):
#         self.hp = 125
#         self.dmg = 15
#         self.weapon = weapon

# class Enemy_castle():
#     def __init__(self,weapon):   
#         self.hp = 175
#         self.dmg = 35
#         self.weapon = weapon

# class Giga_enemy():
#     def __init__(self,weapon):
#         self.hp = 99999
#         self.dmg = 99999
#         self.weapon = weapon
 
# class Vilager():
#     def __init__(self, speak):
#         self.speak = speak   
        

    
class Graphic:
    def __init__(self, x, y, width, height, img_path):
        self.X = x
        self.Y = y
        self.WIDTH = width
        self.HEIGHT = height
        self.IMG_PATH = img_path
        self.load_image()
    
    
    def load_image(self):
        self.IMAGE = pygame.image.load(self.IMG_PATH)
        self.IMAGE = pygame.transform.scale(self.IMAGE, (500, 500))
    
    def show_image(self, window):
        window.blit(self.IMAGE, (self.X, self.Y))
    
   
        
        
