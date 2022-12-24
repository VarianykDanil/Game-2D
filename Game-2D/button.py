import pygame
import models


class Button(models.Graphic):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def check_click(self,mouse_pos,mouse_click):
        if mouse_click[0] == 1:
            if self.rect.x < mouse_pos[0] < self.rect.x + self.rect.width:
                if self.rect.y < mouse_pos[1] < self.rect.y + self.rect.height:
                    return True            
                
menu_button_start = Button(x = 565, y = 200, width = 150, height = 100, img_path = 'images/start_button.jpg')
menu_button_settings = Button(x = 565, y = 350, width = 150, height = 100, img_path = 'images/settings_button.jpg')
menu_button_exit = Button(x = 565, y = 500, width = 150, height = 100, img_path = 'images/exit_button.jpg')

        
        
        
    