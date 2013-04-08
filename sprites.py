import pygame, firing, sounds, random
pygame.init()

class Archer(pygame.sprite.Sprite):
    
    def __init__(self, screen, arrows):
        
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.arrow = arrows
        self.image = pygame.image.load("walking/archer0.png")
        self.image = self.image.convert()
        self.image = pygame.transform.scale(self.image,(45,50))
        self.rect = self.image.get_rect()
        transcolor = self.image.get_at((1,1))
        self.image.set_colorkey(transcolor)
        self.rect.centerx = 400
        self.rect.top = 0
        self.dx = 20
        #for arrow delay
        self.arrowtimer = 0
        self.arrowmax =15
        #for animation
        self.img = []
        self.loadwalk()
        self.delay = 3
        self.pause = self.delay
        self.frame = 0
        
    def update(self):

        keystate = pygame.key.get_pressed()
        #walk left with animation
        if keystate[pygame.K_LEFT]:
            
            if self.rect.left > 0:
                self.pause -= 1
                
                if self.pause <= 0:
                   self.pause = self.delay
                   self.frame += 1
                   
                   if self.frame > 3:
                       self.frame = 0
            
                   self.image = self.img[self.frame]
                   self.rect.centerx -= self.dx
             #walk right with animation   
        if keystate[pygame.K_RIGHT]:
            
            if self.rect.right  < self.screen.get_width():
                self.pause -= 1
                
                if self.pause <= 0:
                   self.pause = self.delay
                   self.frame += 1
                   
                   if self.frame > 3:
                       self.frame = 0
            
                   self.image = self.img[self.frame]
                   self.rect.centerx += self.dx
          #fires arrows makes arrow sprite after delay occurs      
        if keystate[pygame.K_SPACE]:
            
             self.arrowtimer += 1
             if self.arrowtimer== self.arrowmax:
                 
               firing.Arrow(self.rect.midbottom, self.screen, self.arrow)
               sounds.crossbow()
               self.arrowtimer = 0
               
     #load pictures of walking append to self.img for walking motoin
               
    def loadwalk(self):
        
        for i in range(4):
            
            imgName = "walking/archer%i.bmp" % i
            tmpImg = pygame.image.load(imgName)
            tmpImg.convert()
            tmpImg = pygame.transform.scale(tmpImg, (45, 50))
            tranColor = tmpImg.get_at((4, 2))
            tmpImg.set_colorkey(tranColor)
            self.img.append(tmpImg)
            
class Minotaur(pygame.sprite.Sprite):
    
    def __init__(self, screen, throw, score):
        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("walking/minotaur0.png")
        self.screen = screen
        self.arrow = throw
        self.faster = score
        self.image = pygame.transform.scale(self.image, (45,50))
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        transcolor = self.image.get_at((1,1))
        self.image.set_colorkey(transcolor)
        self.img = []
        self.loadwalk()
        self.delay = 5
        self.pause = self.delay
        self.frame = 0
        self.reset()
        # do a loadpics function to get walking animation


#take in score once score is above certain increase self.dy
    def reset(self):
        
        self.dy = 3
        #this works 
        if self.faster >= 100:
            self.dy += .5
        if self.faster >= 200:
            self.dy += .5
        if self.faster >= 400:
            self.dy += 1
        if self.faster >= 800:
            self.dy += 1
        if self.faster >= 1000:
            self.dy += 1
        if self.faster >= 2000:
            self.dy += 2
        self.rect.centerx = random.randrange(0, self.screen.get_width())
        self.rect.centery = 600
        
    def update(self):
        #add axe throw do same as arrow make range bigger
       self.time = random.randrange(1,500)
       if self.time == 1:
           firing.Throw(self.rect.midtop, self.arrow)
       if self.rect.top >= 0:
           self.pause -= 1
           if self.pause <= 0:
              self.pause = self.delay
              self.frame += 1
                   
              if self.frame > 3:
                 self.frame = 0
              self.image = self.img[self.frame]
              self.rect.centery -= self.dy
       else:
           self.reset()
           
    def loadwalk(self):
        
        for i in range(4):
            
            imgName = "walking/minotaur%i.bmp" % i
            tmpImg = pygame.image.load(imgName)
            tmpImg.convert()
            tmpImg = pygame.transform.scale(tmpImg, (45, 50))
            tranColor = tmpImg.get_at((4, 2))
            tmpImg.set_colorkey(tranColor)
            self.img.append(tmpImg)
            
