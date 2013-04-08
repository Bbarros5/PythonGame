import pygame, random
pygame.init()

class WallUp(pygame.sprite.Sprite):
    
     def __init__(self, screen):
         
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("hammer.png")
        self.image = pygame.transform.scale(self.image, (30,30))
        self.screen = screen
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        transcolor = self.image.get_at((0,1))
        self.image.set_colorkey(transcolor)
        self.rect.centerx = random.randrange(0, self.screen.get_width())
        self.rect.top = 0
        self.timer = 120
        
     def update(self):
         
        self.timer -= 1
       
        if self.timer == 0:
            self.kill()
