"""
Portion of source code taken from Andy Harris MiniGui
with slight alterations (bgcolor and size) for use.

"""

import pygame
pygame.init()

class Label(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont(None, 30)
        self.text = ""
        self.fgColor = ((0, 0, 0))
        self.bgColor = ((0xCC, 0xCC, 0xCC))
        self.center = (100, 100)
        self.size = (200, 30)

    def update(self):
        self.image = pygame.Surface(self.size)
        self.image.fill(self.bgColor)
        fontSurface = self.font.render(self.text, True, self.fgColor, self.bgColor)
        #center the text
        xPos = (self.image.get_width() - fontSurface.get_width())/2
        
        self.image.blit(fontSurface, (xPos, 0))
        self.rect = self.image.get_rect()
        self.rect.center = self.center

class Button(Label):

    def __init__(self):
        Label.__init__(self)
        self.active = False
        self.bgColor = (0xCC, 0xCC, 0xCC)
    
    def update(self):
        Label.update(self)
        self.active = False
        
        #check for mouse input
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.active = True
