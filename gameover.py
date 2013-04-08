import pygame
pygame.init()

class Gameover(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("None", 50)
        
    def update(self):
        self.text = ("GAME OVER")
        self.image = self.font.render(self.text, 1, (0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (400,300)
        
class Gameoverprompt(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("None", 30)
        
    def update(self):
        self.text = "PRESS ESC TO RETURN TO MENU"
        self.image = self.font.render(self.text, 1, (0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (400,400)
