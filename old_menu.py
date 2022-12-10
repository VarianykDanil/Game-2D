import pygame
#from manage import game_loop

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 720))
font = pygame.font.SysFont("Comic Sans MS", 20)
class Button:
    def __init__(self, text,  pos, font, bg="black", feedback=""):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Comic Sans MS", font)
        self.feedback = feedback
        self.callback = None
        self.change_text(text, bg)
 
    def change_text(self, text, bg="black"):
        self.text = self.font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
 
    def show(buttons):
        for button in buttons:
            screen.blit(button.surface, (button.x, button.y))
 
    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.change_text(self.feedback, bg="red")
                    self.callback = "Start"
            
button1 = Button(
    "Start",
    (100, 100),
    font=30,
    bg="navy",
    feedback="You clicked me")

button2 = Button(
    "Options",
    (100, 300),
    font=30,
    bg="navy",
    feedback="You clicked me")

button3 = Button(
    "Quit",
    (100, 500),
    font=30,
    bg="navy",
    feedback="You clicked me")
buttons = [button1, button2, button3]
def menu_loop():
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                menu = False
            for button in buttons:
                button.click(event)
        
        screen.fill([0, 0, 255])
        Button.show(buttons)

        pygame.display.flip()
        clock.tick(60)
        if button1.callback == "Start":
            menu = False
            game_loop()

menu_loop()