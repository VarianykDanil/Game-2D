import pygame

class Graphic:
    def __init__(self, x, y, width, height, img_path):
        self.IMG_PATH = img_path
        self.IMAGE = None
        self.rect = pygame.Rect(x, y, width, height)
        if self.IMG_PATH != None:
            self.load_image()
    
    
    def load_image(self):
        self.IMAGE = pygame.image.load(self.IMG_PATH)
        self.IMAGE = pygame.transform.scale(self.IMAGE, (self.rect.width, self.rect.height))
        
    
    def show_image(self, window):
        if self.IMAGE != None:
            window.blit(self.IMAGE, (self.rect.x, self.rect.y))

