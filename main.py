# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from typing import Union

import pygame
import random

from pygame.surface import Surface, SurfaceType

pygame.init()

Screen: Union[Surface, SurfaceType] = pygame.display.set_mode((1000, 1000))
# Name and icon
pygame.display.set_caption("numero uno")
icon = pygame.image.load('001-spaceship.png')
pygame.display.set_icon(icon)
# loadimages
bg_Img = pygame.image.load('b.png')
up_e = pygame.image.load('eb.png')
# Player

playerImg = pygame.image.load('001-spaceship.png')
player1Img = pygame.image.load('o.png')
X = 370
Y = 680
X1 = 420
Y1 = 680
X2 = random.randint(0, 1000)
Y2 = random.randint(200, 400)
X3 = random.randint(0, 1000)
Y3 = random.randint(200, 400)
X4 = 365
Y4 = 676
X_change = 0
Y_change = 0
X1_change = 0
Y1_change = 0
X2_change = 0.3
Y2_change = 20
X3_change = 0.3
Y3_change = 20
eImg = pygame.image.load('002-monster.png')
e1Img = pygame.image.load('003-monster-1.png')
bullet_Img = pygame.image.load('003-monster-1.png')

def player(X1, Y1):
    Screen.blit(playerImg, (X1, Y1))


# player2
def player1(X, Y):
    Screen.blit(player1Img, (X, Y))


# e changes
def ups(X3, Y3):
    Screen.blit(eImg, (X3, Y3))


def downs(X2, Y2):
    Screen.blit(e1Img, (X2, Y2))


run= True
while run:
    Screen.blit(up_e, (0, 0))
    Screen.blit(bg_Img, (0, 700))

    player(X, Y)
    player1(X1, Y1)
    ups(X2, Y2)
    downs(X3, Y3)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                X_change = -0.4
                X1_change = -0.4

            if event.key == pygame.K_1:
                X_change = 0.4
                X1_change = 0.4

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_0 or event.key == pygame.K_1 or event.key == pygame.K_2:
                X_change = 0
                Y_change = 0
                X1_change = 0
                Y1_change = 0
    # Player changes
X += X_change
X1 += X1_change
if X <= 0:
    X = 0
elif X >= 936:
    X = 936
# UP and Down Changes
X2 += X2_change
X3 += X3_change
if X2 <= 0:
    X2_change = 0.3
    Y2 += Y2_change
elif X2 >= 1000:
    X2 = -0.3
    Y2 += Y2_change
if X3 <= 0:
    X3 = 0.3
    Y3 += Y3_change
elif X3 >= 1000:
    X3 = -0.3
    Y3 += Y3_change
pygame.display.update()
