import pygame
from modules import *
#import menu
from models import *


pygame.init()

clock = pygame.time.Clock()



window = pygame.display.set_mode((screen_width, screen_height))

background = Graphic(x = 0,y = 0, width = 1280, height = 720, img_path = 'images/Fone.png')


 
   


def game_loop():  
    game = True
    scene = 'game' 
    while game:
        if scene == 'menu':
            mouse_pos = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()
            background.show_image(window) #menu scene
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
            # menu_button_start.show_image(window)
            # menu_button_settings.show_image(window)
            # menu_button_exit.show_image(window)
            # if menu_button_start.check_click(mouse_pos,mouse_click) == True:
            #     scene = 'game'
            # if menu_button_exit.check_click(mouse_pos, mouse_click) == True:
            #     game = False
        if scene == 'game':
            background.show_image(window) #game scene
            main_hero.move_hero(map_level1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False

            for obj in list_objects:
                obj.show_image(window)

        if scene == 'settings':
            background.show_image(window) #game scene
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False

        
        pygame.display.flip()
        clock.tick(FPS)

game_loop()
