"""

Brian Barros

"""
import pygame, random, sounds, scoreboard, sprites, powerup, gameover, button
pygame.init()


#wall scenary        
class Wall(pygame.sprite.Sprite):
    
    def __init__(self):
    
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("castlewall1.png")
        self.image = self.image.convert()
        self.image = pygame.transform.scale(self.image, (800,135))
        self.rect = self.image.get_rect()
        self.image.set_colorkey((255,255,255))
        self.rect.top = 0
        
    
#ground scenary
class Ground(pygame.sprite.Sprite):
    
    def __init__(self, screen):
        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("background1.png")
        self.image = self.image.convert()
        self.screen = screen
        self.image = pygame.transform.scale(self.image,(800, 480))
        self.rect = self.image.get_rect()
        self.rect.bottom = self.screen.get_height()

def game():
    
    #display and background
    
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption
    background = pygame.Surface(screen.get_size())
    background.fill((0,0,0))
    screen.blit(background, (0,0))

    highscore_filein = open("highscore.txt", "r")
    highscore = highscore_filein.read()
    ihighscore = int(highscore)
    highscore_filein.close()
    

    #set up sprites
    
    arrows = pygame.sprite.Group()
    score = scoreboard.Score()
    archer = sprites.Archer(screen, arrows)
    wall = Wall()
    ground = Ground(screen)

    #sprite groups
    axes = pygame.sprite.Group()
    backgroundsprite = pygame.sprite.Group(ground)
    wallsprite = pygame.sprite.Group(wall)
    Archersprite = pygame.sprite.Group(archer)
    enemysprites = pygame.sprite.Group()
    Wallpowerups = pygame.sprite.Group()
    scoreboardsprite = pygame.sprite.Group(score)
    gameoversprite = pygame.sprite.Group()
    
    clock = pygame.time.Clock()
    keepgoing = True
    enemycounter = 0
    fastenemycoutner = 0
    #when scoreboard made get rid of these two
    wallcollide = 0
    playercollide = 5
    pause = False
    
    #game loop
    while keepgoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepgoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepgoing = False
                
                    
        
        #update and draw sprites to screen
        arrows.update()
        Wallpowerups.update()
        Archersprite.update()
        enemysprites.update()
        scoreboardsprite.update()
        axes.update()
        gameoversprite.update()
        
        backgroundsprite.draw(screen)
        wallsprite.draw(screen)
        Archersprite.draw(screen)
        arrows.draw(screen)
        scoreboardsprite.draw(screen)
        enemysprites.draw(screen)
        axes.draw(screen)
        Wallpowerups.draw(screen)
        gameoversprite.draw(screen)
        pygame.display.flip()

        
        #drop a wallfix powerup, Rare drop
        wallpowerup = random.randint(1,2000)
        if wallpowerup >= 1995:
          Wallpowerups.add(powerup.WallUp(screen))

        #spawn eneimes
        if score.score >= 2500:
            enemycounter += 2.5
        if score.score >= 1000:
            enemycounter += 2
        if score.score >=  500:
            enemycounter += 1.5
        else:
            enemycounter += 1
        if enemycounter >= 45:
            enemysprites.add(sprites.Minotaur(screen, axes, score.score))
            enemycounter = 0

        #create fast enemy spawns every 45 seconds so 45*30
            
        # damage to 5 when pickedup
        if pygame.sprite.groupcollide(Archersprite, Wallpowerups, 0, 1):
            score.wallhealth = 5
            #pick up noise

        if pygame.sprite.groupcollide(arrows, enemysprites, 1,1):
            score.score += 50
            if score.score >= ihighscore:
                ihighscore = score.score
                highscore_fileout = open("highscore.txt", "w")
                writescore = str(score.score)
                highscore_fileout.writelines(writescore)
                highscore_fileout.close()
            #death noise
            
        if pygame.sprite.groupcollide(wallsprite, enemysprites, 0,1):
            score.wallhealth -= 1
            #thud noise
            if score.wallhealth == 0:
                #gameover screen goes here get rid of keepgoing
                gameoversprite.add(gameover.Gameover())
                gameoversprite.add(gameover.Gameoverprompt())
                Archersprite.remove(archer)

        if pygame.sprite.groupcollide(Archersprite, axes, 0,1):
            score.health -= 1
            #some noise
            if score.health == 0:
                #game over screen goes here get rid of keepgoing
                gameoversprite.add(gameover.Gamerover())
                gameoversprite.add(gameover.Gameoverprompt())
    
        
def aboutmenu():
    pygame.display.set_caption("Wall")
    screen = pygame.display.set_mode((800,600))

    
    background = Ground(screen)
    wall = Wall()
    backgroundsprites = pygame.sprite.Group(background, wall)
    
    insFont = pygame.font.SysFont(None, 55)
    insLabels = []
    instructions = (
    "",
    "",
    "",
    "",
    "",
    "Defend the Wall as long as you can.",
    "You can only be hit five times as well",
    "as the wall. You can replenish the walls",
    "health when the hammer shows up on the",
    "wall.",
    "",
    "Use the space bar to fire at enemies and",
    "the arrow keys to move left and right",    
    "along the wall. The enemies will get faster ",
    "and spawn more often as your score",
    "goes up"
    
    )
    
    for line in instructions:
        tempLabel = insFont.render(line, 1, (0, 0, 0))
        insLabels.append(tempLabel)

    keepgoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(True)    
    while keepgoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepgoing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepgoing = False
                    
                
        backgroundsprites.draw(screen)
        
        for i in range(len(insLabels)):
            screen.blit(insLabels[i], (50, 30*i))
            
        pygame.display.flip()
def menu():
    #display
    pygame.display.set_caption("Wall")
    screen = pygame.display.set_mode((800,600))
    
    #background sprites
    
    background = Ground(screen)
    wall = Wall()
    
    #read highscore
    highscore_file = open("highscore.txt", "r")
    highscore = highscore_file.read()
    highscore_file.close()
    
    #display highscore
    lblhighscore = button.Label()
    lblhighscore.text = "High Score: " + str(highscore)
    lblhighscore.center = (170,30)

    #buttons
    startbutton = button.Button()
    startbutton.text = "Start Game"
    startbutton.center = (400,300)

    aboutbutton = button.Button()
    aboutbutton.text = "About"
    aboutbutton.center = (400, 400)
    
    quitbutton = button.Button()
    quitbutton.text = "Quit"
    quitbutton.center = (400, 500)

    #sprite groups
    backgroundsprites = pygame.sprite.Group(background, wall)
    allsprites = pygame.sprite.Group(startbutton, aboutbutton, quitbutton,
                                     lblhighscore)
    keepgoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(True)
    while keepgoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepgoing = False
                playing = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepgoing = False
                    playing = False
        #different buttons active causes different
        if startbutton.active:
            keepgoing = False
            playing = True

        if aboutbutton.active:
            aboutmenu()
        if quitbutton.active:
            keepgoing = False
            playing = False
            
        allsprites.update()
        backgroundsprites.draw(screen)
        allsprites.draw(screen)

       

        pygame.display.flip()
        
      
    pygame.mouse.set_visible(True)
    return playing

def main():
    playing = True
    score = 0
    sounds.themesong()
    while playing:
        playing = menu()
        if playing:
            score = game()
           
            
if __name__ == "__main__":
    main()

        
    
