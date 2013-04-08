"""
Stephan Schutze of Soundbible.com created the sound for the arrow

http://soundbible.com/1780-Bow-Fire-Arrow.html


"""

import pygame
pygame.init()

pygame.mixer.init()

def crossbow():
    
    
    sndArrow = pygame.mixer.Sound("sounds\Fire.wav")
    sndArrow.play()

def themesong():


    sndtheme = pygame.mixer.Sound("sounds\super big theme.wav")
    sndtheme.play(-1)

