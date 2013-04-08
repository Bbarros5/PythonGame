import pygame
pygame.init()

class Arrow(pygame.sprite.Sprite):
    
    def __init__(self, pos, screen, arrow):
        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("arrow1.png")
        self.screen = screen
        self.arrow = arrow
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        transcolor = self.image.get_at((1,1))
        self.image.set_colorkey(transcolor)
        self.rect.center = pos
        self.add(self.arrow)        

    
    
    def update(self):
        if self.rect.top >= self.screen.get_height():
            self.kill()
        else:    
            self.rect.centery += 13
            
class Throw(pygame.sprite.Sprite):
    
    def __init__(self, pos, axes):

        #change arrow to axe when made
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("arrowm.png")
        self.thrown = axes
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        transcolor = self.image.get_at((1,1))
        self.image.set_colorkey(transcolor)
        self.rect.center = pos
        self.add(self.thrown)        
        #do a loadpics function to get axe animations
    
    
    def update(self):
        if self.rect.bottom == 0:
            self.kill()
        else:    
            self.rect.centery -= 8
