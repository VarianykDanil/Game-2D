import pygame
import models


class Button(models.Graphic):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def check_click(self,mouse_pos,mouse_click):
        if mouse_click[0] == 1:
            if self.X < mouse_pos[0] < self.X + self.WIDTH:
                if self.Y < mouse_pos[1] < self.Y + self.HEIGHT:
                    return True            
                
# menu_button_start = Button(x = 565, y = 200, width = 150, height = 100, img_path = 'images/start_button.jpg')
# menu_button_settings = Button(x = 565, y = 350, width = 150, height = 100, img_path = 'images/settings_button.jpg')
# menu_button_exit = Button(x = 565, y = 500, width = 150, height = 100, img_path = 'images/exit_button.jpg')

        
        
        
    