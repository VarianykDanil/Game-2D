import pygame
from modules import *
from models import *
from main_hero import *



pygame.init()

clock = pygame.time.Clock()

#pygame.mixer.music.load('sounds/main_music.mp3')
#pygame.mixer.music.play(-1)

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = Graphic(x = 0,y = 0, width = 1280, height = 730, img_path = 'images/Fone.png')


def game_loop():  
    game = True
    scene = 'menu' 

    MUSIK_STATUS = True
    SOUNDS = True


    dict_objects = create_map(main_level_before)
    while game:
        mouse_pos = pygame.mouse.get_pos()
        # if main_hero_anim_count +1 >= 30:
        #     main_hero_anim_count = 0

        if scene == 'menu':
            background.show_image(window) #menu scene
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if menu_button_start.check_click(mouse_pos) == True:
                        scene = main_hero.current_level
                    if menu_button_settings.check_click(mouse_pos) == True:
                        scene = 'settings'
                    if menu_button_exit.check_click(mouse_pos) == True:
                        game = False

                
            menu_button_start.show_image(window)
            menu_button_settings.show_image(window)
            menu_button_exit.show_image(window)
        
        if scene == 0:#Main location - до событий игры
            background.show_image(window) #game scene

            for door in dict_objects["list_doors"]:
                door.check_collide(main_hero, pygame.key.get_pressed()[pygame.K_e])
            if main_hero.current_level != scene:
                scene = main_hero.current_level
                dict_objects = create_map(levels[main_hero.current_level])
            main_hero.attack()
            
            main_hero.move(dict_objects["list_blocks"])
            dummy.show_image(window)
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
            

            for obj in dict_objects["list_objects"]:
                obj.show_image(window)


        if scene == 1:#Training location - Тренировка
            background.show_image(window) #game scene
            for door in dict_objects["list_doors"]:
                door.check_collide(main_hero, pygame.key.get_pressed()[pygame.K_e])
            if main_hero.current_level != scene:
                scene = main_hero.current_level
                dict_objects = create_map(levels[main_hero.current_level])




            main_hero.move(dict_objects["list_blocks"])
        
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
            

            for obj in dict_objects["list_objects"]:
                obj.show_image(window)
                
        if scene == 2:#main_level_after - Тренировка
            background.show_image(window) #game scene
            for door in dict_objects["list_doors"]:
                door.check_collide(main_hero, pygame.key.get_pressed()[pygame.K_e])
            if main_hero.current_level != scene:
                scene = main_hero.current_level
                dict_objects = create_map(levels[main_hero.current_level])




            main_hero.move(dict_objects["list_blocks"])
        
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
            

            for obj in dict_objects["list_objects"]:
                obj.show_image(window)

        if scene == 3:#level1 - уровень с под уровнями
            background.show_image(window) #game scene
            for door in dict_objects["list_doors"]:
                door.check_collide(main_hero, pygame.key.get_pressed()[pygame.K_e])
            if main_hero.current_level != scene:
                scene = main_hero.current_level
                if type(main_hero.current_level) == int:
                    dict_objects = create_map(levels[main_hero.current_level])
                else:
                    dict_objects = create_map(under_levels[main_hero.current_level])




            main_hero.move(dict_objects["list_blocks"])
        
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
            

            for obj in dict_objects["list_objects"]:
                obj.show_image(window)

        if scene == 4:#level2 - уровень с под уровнями
            background.show_image(window) #game scene
            for door in dict_objects["list_doors"]:
                door.check_collide(main_hero, pygame.key.get_pressed()[pygame.K_e])
            if main_hero.current_level != scene:
                scene = main_hero.current_level
                if type(main_hero.current_level) == int:
                    dict_objects = create_map(levels[main_hero.current_level])
                else:
                    dict_objects = create_map(under_levels[main_hero.current_level])




            main_hero.move(dict_objects["list_blocks"])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
        

            for obj in dict_objects["list_objects"]:
                obj.show_image(window)

        if scene == 5:#boss_level - уровень с под уровнями
            background.show_image(window) #game scene
            for door in dict_objects["list_doors"]:
                door.check_collide(main_hero, pygame.key.get_pressed()[pygame.K_e])
            if main_hero.current_level != scene:
                scene = main_hero.current_level
                if type(main_hero.current_level) == int:
                    dict_objects = create_map(levels[main_hero.current_level])
                else:
                    dict_objects = create_map(under_levels[main_hero.current_level])




            main_hero.move(dict_objects["list_blocks"])
        
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
            

            for obj in dict_objects["list_objects"]:
                obj.show_image(window)                        

        if scene == "under1":#under1 - Под уровень 1
            background.show_image(window) #game scene
            for door in dict_objects["list_doors"]:
                door.check_collide(main_hero, pygame.key.get_pressed()[pygame.K_e])
            if main_hero.current_level != scene:
                scene = main_hero.current_level
                if type(main_hero.current_level) == int:
                    dict_objects = create_map(levels[main_hero.current_level])
                else:
                    dict_objects = create_map(under_levels[main_hero.current_level])




            main_hero.move(dict_objects["list_blocks"])
        
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
            

            for obj in dict_objects["list_objects"]:
                obj.show_image(window)                        

        if scene == "under2":#under2 - Под уровень 2
            background.show_image(window) #game scene
            for door in dict_objects["list_doors"]:
                door.check_collide(main_hero, pygame.key.get_pressed()[pygame.K_e])
            if main_hero.current_level != scene:
                scene = main_hero.current_level
                if type(main_hero.current_level) == int:
                    dict_objects = create_map(levels[main_hero.current_level])
                else:
                    dict_objects = create_map(under_levels[main_hero.current_level])




            main_hero.move(dict_objects["list_blocks"])
        
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
            

            for obj in dict_objects["list_objects"]:
                obj.show_image(window)                        

        if scene == "under3":#under3 - Под уровень 3d
            background.show_image(window) #game scene
            for door in dict_objects["list_doors"]:
                door.check_collide(main_hero, pygame.key.get_pressed()[pygame.K_e])
            if main_hero.current_level != scene:
                scene = main_hero.current_level
                if type(main_hero.current_level) == int:
                    dict_objects = create_map(levels[main_hero.current_level])
                else:
                    dict_objects = create_map(under_levels[main_hero.current_level])




            main_hero.move(dict_objects["list_blocks"])
        
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
            

            for obj in dict_objects["list_objects"]:
                obj.show_image(window)                        


        if scene == 'settings':
            background.show_image(window) #game scene

            #game loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if settings_button_sounds.check_click(mouse_pos) == True:
                        if SOUNDS == True:
                            settings_button_sounds.IMG_PATH = 'images/sounds_off.png'
                            settings_button_sounds.load_image()
                            SOUNDS = False

                        elif SOUNDS == False:
                            settings_button_sounds.IMG_PATH = 'images/sounds_on.png'
                            settings_button_sounds.load_image()
                            SOUNDS = True


                    if settings_button_music.check_click(mouse_pos) == True:
                        if MUSIK_STATUS == True:
                            settings_button_music.IMG_PATH = 'images/music_off.png'
                            settings_button_music.load_image()
                            MUSIK_STATUS = False

                        elif MUSIK_STATUS == False:
                            settings_button_music.IMG_PATH = 'images/music_on.png'
                            settings_button_music.load_image()
                            MUSIK_STATUS = True

                    if button_back.check_click(mouse_pos) == True:
                        scene = 'menu'
                        #buttons
                        
            button_back.show_image(window)
            settings_button_sounds.show_image(window)
            settings_button_music.show_image(window)
        
        pygame.display.flip()
        clock.tick(FPS)

game_loop()
