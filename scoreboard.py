import pygame
pygame.init()

class Score(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.health = 5
        self.wallhealth = 5
        self.score = 0
        self.font = pygame.font.SysFont("None", 35)
        
    def update(self):
        self.text = "Health: %d     Wall: %d    Score: %d" % (self.health, self.wallhealth, self.score)
        self.image = self.font.render(self.text, 1, (0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (195, 585)
    

                                                               
