import pygame
from pygame import *
import random
pygame.init()

screen = pygame.display.set_mode((1200, 800))
name = pygame.display.set_caption("Choose Correctly!")
icon = pygame.image.load("iconsquare.png")
pygame.display.set_icon(icon)
#Player
playerImg = pygame.image.load("student.png")
playerX = 99
playerY = 720
playerX_change = 0
playerY_change = 0

def player(x,y):
    screen.blit(playerImg, (x, y))

coinImg = pygame.image.load("background.png")

coinX = 0
coinY = 0

black = (0, 0, 0)

def spike(x,y):
    screen.blit(coinImg, (coinX, coinY))
# Ticks
enemyImg = pygame.image.load("Player.png")

emX = 400
emY = 0
sus = 1.25
score = 0

def enemy(x,y):
    screen.blit(enemyImg, (emX, emY))


running = True
while running:

    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord("a"):
                playerX_change = -sus
            if event.key == pygame.K_UP or event.key == ord("w"):
                playerY_change = -sus
            if event.key == pygame.K_RIGHT or event.key == ord("d"):
                playerX_change = sus
            if event.key == pygame.K_DOWN or event.key == ord("s"):
               playerY_change = sus
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == ord("a") or event.key == ord("w") or event.key == ord("s") or event.key == ord("d"):
                playerX_change = 0
                playerY_change = 0 
        

    playerX += playerX_change
    playerY += playerY_change

    if playerX <=0:
        playerX = 0
    elif playerX >=1136:
        playerX = 1136
    if playerY <=0:
        playerY = 0
    elif playerY >=736:
        playerY = 736
    if emY >=736:
        emY = 0
        emX = random.randint(0, 1134)
        score -= 1
    if playerX + 64 > emX and playerX < emX + 64 and playerY + 64 > emY and playerY < emY + 64:
       emY = 0
       emX = random.randint(0, 1134)  
       score += 1
       

    emY += 1
   
    
    player(playerX, playerY)
    enemy(emX, emY)


    font = pygame.font.Font("freesansbold.ttf", 32)
    
    cool = str(score)

    scoreText = font.render(cool, True, (0, 0, 0))

    scoreWon = font.render("You Passed!", True, (0, 0, 0))


    if cool == (100):
      screen.blit(scoreWon, (400, 400))
    screen.blit(coinImg, (coinX, coinY))
    screen.blit(playerImg, (playerX, playerY))
    screen.blit(enemyImg, (emX, emY))
    screen.blit(scoreText, (100, 110))
   

    
    pygame.display.update()