import pygame

class Graphic:
    def __init__(self, x, y, width, height, img_path):
        self.X = x
        self.Y = y  
        self.WIDTH = width
        self.HEIGHT = height
        self.IMG_PATH = img_path
        self.IMAGE = None
        if self.IMG_PATH != None:
            self.load_image()
    
    
    def load_image(self):
        self.IMAGE = pygame.image.load(self.IMG_PATH)
        self.IMAGE = pygame.transform.scale(self.IMAGE, (self.WIDTH, self.HEIGHT))
        
    
    def show_image(self, window):
        if self.IMAGE != None:
            window.blit(self.IMAGE, (self.X, self.Y))

