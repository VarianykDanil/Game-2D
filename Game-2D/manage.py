import pygame
from modules import *
from models import *
from main_hero import *



pygame.init()

clock = pygame.time.Clock()

#pygame.mixer.music.load('sounds/main_music.mp3')
#pygame.mixer.music.play(-1)

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = Graphic(x = 0,y = 0, width = 1280, height = 720, img_path = 'images/Fone.jpg')


def game_loop():  
    game = True
    scene = 'menu' 

    list_objects, list_blocks, list_doors = create_map(main_level_before)
    while game:

        # if main_hero_anim_count +1 >= 30:
        #     main_hero_anim_count = 0

        if scene == 'menu':
            mouse_pos = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()
            background.show_image(window) #menu scene
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False

                
            menu_button_start.show_image(window)
            menu_button_settings.show_image(window)
            menu_button_exit.show_image(window)
            if menu_button_start.check_click(mouse_pos,mouse_click) == True:
                scene = main_hero.current_level
            if menu_button_exit.check_click(mouse_pos, mouse_click) == True:
                game = False
        
        if scene == 0:#Main location - до событий игры
            background.show_image(window) #game scene

            for door in list_doors:
                door.check_collide(main_hero, pygame.key.get_pressed()[pygame.K_e])
            if main_hero.current_level != scene:
                scene = main_hero.current_level
                list_objects, list_blocks, list_doors = create_map(levels[main_hero.current_level])
            main_hero.attack()
            
            main_hero.move(list_blocks)
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
            

            for obj in list_objects:
                obj.show_image(window)


        if scene == 1:#Training location - Тренировка
            background.show_image(window) #game scene
            for door in list_doors:
                door.check_collide(main_hero, pygame.key.get_pressed()[pygame.K_e])
            if main_hero.current_level != scene:
                scene = main_hero.current_level
                list_objects, list_blocks, list_doors = create_map(levels[main_hero.current_level])




            main_hero.move(list_blocks)
        
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
            

            for obj in list_objects:
                obj.show_image(window)
                
        if scene == 2:#main_level_after - Тренировка
            background.show_image(window) #game scene
            for door in list_doors:
                door.check_collide(main_hero, pygame.key.get_pressed()[pygame.K_e])
            if main_hero.current_level != scene:
                scene = main_hero.current_level
                list_objects, list_blocks, list_doors = create_map(levels[main_hero.current_level])




            main_hero.move(list_blocks)
        
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
            

            for obj in list_objects:
                obj.show_image(window)

        if scene == 3:#Training location - Тренировка
            background.show_image(window) #game scene
            for door in list_doors:
                door.check_collide(main_hero, pygame.key.get_pressed()[pygame.K_e])
            if main_hero.current_level != scene:
                scene = main_hero.current_level
                list_objects, list_blocks, list_doors = create_map(levels[main_hero.current_level])




            main_hero.move(list_blocks)
        
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
            

            for obj in list_objects:
                obj.show_image(window)

        if scene == 4:#Training location - Тренировка
            background.show_image(window) #game scene
            for door in list_doors:
                door.check_collide(main_hero, pygame.key.get_pressed()[pygame.K_e])
            if main_hero.current_level != scene:
                scene = main_hero.current_level
                list_objects, list_blocks, list_doors = create_map(levels[main_hero.current_level])




            main_hero.move(list_blocks)
        
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        main_hero.IMG_PATH = 'images/gribori/normal_r.png'
                        main_hero.load_image()
                    if event.key == pygame.K_a:
                        main_hero.IMG_PATH = 'images/gribori/normal_l.png'
                        main_hero.load_image()
            

            for obj in list_objects:
                obj.show_image(window)

        if scene == 5:#Training location - Тренировка
            background.show_image(window) #game scene
            for door in list_doors:
                door.check_collide(main_hero, pygame.key.get_pressed()[pygame.K_e])
            if main_hero.current_level != scene:
                scene = main_hero.current_level
                list_objects, list_blocks, list_doors = create_map(levels[main_hero.current_level])




            main_hero.move(list_blocks)
        
            
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
