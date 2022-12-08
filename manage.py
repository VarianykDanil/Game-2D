import pygame
import menu

pygame.init()

clock = pygame.time.Clock()

screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill([0, 255, 255])

main_hero = pygame.Rect(640, 360, 10, 20)

moving_left = False
moving_right = False

jump = False
jump_counter = 0

def game_loop():
    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                game = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    moving_left = True
                    main_hero.x -= 3
                if event.key == pygame.K_d:
                    moving_right = True
                    main_hero.x += 3
                if event.key == pygame.K_SPACE:
                    jump = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    moving_left = False
                if event.key == pygame.K_a:
                    moving_right = False

        if jump == True:
            if jump_counter < 100:
                main_hero.y -= 5
                jump_counter += 5
            elif jump_counter >= 100 and jump_counter < 200:
                main_hero.y += 5
                jump_counter += 5
            else:
                jump_counter = 0
                jump = False


        screen.fill([0, 255, 255])
        pygame.draw.rect(screen, (255, 0, 0), main_hero)
        pygame.display.flip()
        clock.tick(60)

game_loop()
