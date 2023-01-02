import pygame
from models import *

pygame.init()

dummy_dialog_1 = {
    1 : "Я просто манекен.",
    2 : "И я говорю.",
    3 : "Какие то вопросы?",
}

class Vilagers(Graphic):
    def __init__(self, dialog, **kwargs):
        super().__init__(**kwargs)
        self.dialog = dialog
        self.dialog_counter = 0
        self.font_1 = pygame.font.Font("Font/Dama Bubey.ttf", 36)
        self.img_rect = pygame.Rect(0,0,64,72)

    def load_image(self):
        self.IMAGE = pygame.image.load(self.IMG_PATH)
        self.IMAGE = pygame.transform.scale(self.IMAGE, (64,72))
    
    def show_image(self, window):
        if self.IMAGE != None:
            window.blit(self.IMAGE, (self.img_rect.x, self.img_rect.y))
        

    def check_dialog(self, main_hero, dialog, dialog_counter, window, SCREEN_WIDTH, font_1):
        keys = pygame.key.get_pressed()
        if self.rect.colliderect(main_hero):
            if keys[pygame.K_e]:
                self.read_dialog(dialog, dialog_counter, window, SCREEN_WIDTH, font_1)
                dialog_counter = 0

    def read_dialog(self, dialog, dialog_counter, window, SCREEN_WIDTH, font_1):  
        if dialog_counter <= len(dialog):
            dialog_rect = pygame.rect(0, 55, SCREEN_WIDTH, 100) 
            dialog_rect.fill(107, 142, 35)
            window.blit(dialog_rect, (0,55))
            dialog_text = font_1.render(dialog[dialog_counter], True, (128, 128, 0))
            window.blit(dialog_text, (10,65))
            mouse = pygame.mouse.get_pressed()[2]
            if mouse:
                dialog_counter += 1



dummy = Vilagers(dummy_dialog_1, x = 1000, y = 684, width = 52, height = 148, img_path = 'images/dummy.png')

            