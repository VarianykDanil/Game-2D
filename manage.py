import pygame
#import menu
from settings import*
from models import Graphic

pygame.init()

clock = pygame.time.Clock()



window = pygame.display.set_mode((screen_width, screen_height))

background = Graphic(x = 0,y = 0, width = 100, height = 100, img_path = 'images/Fone.jpg')




def game_loop():
    
    game = True
    scene = 'menu' 
    while game:
        
        
        if scene == 'menu':
            background.show_image(window) #menu scene
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                
            
        # if scene == 'game':
        #     background.showimage() #game scene
        
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             game = False
        #     main_hero.move_hero()

          

        
        pygame.display.flip()
        clock.tick(FPS)

game_loop()
