import pygame
#from manage import game_loop

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 720))
font = pygame.font.Font(None, 55)
class Button:
    def __init__(self, text, pos):
        self.pressed = False

        self.animations_fonts = [pygame.font.Font(None, i) for i in range(55, 77, 2)]
        self.counter = 0
        self.text = text

        self.text_surf = font.render(text, True, '#F6FFFF')
        self.default_size = tuple([self.text_surf.get_width(), self.text_surf.get_height()])
        self.max_size = tuple(i for i in self.animations_fonts[10].size(text))
        self.rect = pygame.Rect(pos, self.default_size)
        
        self.push_up_size = tuple(i for i in self.animations_fonts[-5].size(text))

        self.text_rect = self.text_surf.get_rect(center = self.rect.center)
        
        self.top_color = '#475F77'
    def draw(self):
        pygame.draw.rect(screen, self.top_color, self.rect, -1) #-1
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.top_color = '#D74B4B'
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
                if self.rect.size != self.push_up_size:
                    self.counter-=1
                    self.text_surf = self.animations_fonts[self.counter].render(self.text, True, '#F6FFFF')
                    self.var_width = round((self.rect.size[0] - self.text_surf.get_width())/2)
                    self.var_height = round((self.rect.size[1] - self.text_surf.get_height())/2)
                    
                    self.rect.update(self.rect.x+self.var_width, self.rect.y+self.var_height, self.text_surf.get_width(), self.text_surf.get_height())
                    self.text_rect = self.text_surf.get_rect(center = self.rect.center)
            elif self.rect.size != self.max_size:
                self.counter+=1
                self.text_surf = self.animations_fonts[self.counter].render(self.text, True, '#F6FFFF')
                #Вычисление на разницу от позиции предыдущего кадра текста кнопки:
                self.var_width = round((self.text_surf.get_width() - self.rect.size[0])/2)
                self.var_height = round((self.text_surf.get_height() - self.rect.size[1])/2)
                #
                self.rect.update(self.rect.x-self.var_width, self.rect.y-self.var_height, self.text_surf.get_width(), self.text_surf.get_height())
                self.text_rect = self.text_surf.get_rect(center = self.rect.center)
            
            else:
                if self.pressed == True:
                    print("click")
                    self.pressed = False
        else:
            self.pressed = False
            self.top_color = '#475F77'
            if self.rect.size != self.default_size:
                self.counter-=1
                self.text_surf = self.animations_fonts[self.counter].render(self.text, True, '#F6FFFF')
                self.var_width = round((self.rect.size[0] - self.text_surf.get_width())/2)
                self.var_height = round((self.rect.size[1] - self.text_surf.get_height())/2)
                
                self.rect.update(self.rect.x+self.var_width, self.rect.y+self.var_height, self.text_surf.get_width(), self.text_surf.get_height())
                self.text_rect = self.text_surf.get_rect(center = self.rect.center)
            
button1 = Button(text="Start!", pos=(100,100))

button2 = Button(text="Settings", pos=(100,300))

button3 = Button(text="Quit", pos=(100,500))

def menu_loop():
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
        
        screen.fill([0, 0, 0])

        button1.draw()
        button2.draw()
        button3.draw()
        pygame.display.flip()
        clock.tick(60)

menu_loop()