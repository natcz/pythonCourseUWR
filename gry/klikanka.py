#!/usr/bin/env python3

import pygame
from pygame.locals import *
from sys import exit
from random import randint
import math
import random

DX = 14
DY = 14
DD = 30

MX = DX*DD
MY = DX*DD

SX = DD * DX / 2
SY = DD * DY / 2
 
pygame.init()
screen = pygame.display.set_mode((MX,MY))
clock = pygame.time.Clock()

Col = {
  'r' : (255,20,0),
  'g' : (20,200,0),
  'y' : (250,250,0),
  'b' : (40,40,255),
  'm' : (200,0,200),
  'o' : (250,150,0)
}


P = {}
colors = list(Col.keys())

def drawSquare(x,y,c):
    r = pygame.Rect(x * DD, y * DD, DD, DD)
    pygame.draw.rect(screen, Col[c], r)

for x in range(DX):
  for y in range(DY):
    P[x,y] = random.choice(colors)
    
while True:
    clock.tick(30)        
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == MOUSEBUTTONDOWN:
          x = event.pos[0] // DD
          y = event.pos[1] // DD
          c = P[x,y]
          
          while P[x,y] == c:
            P[x,y] = random.choice(colors)
          
    screen.fill((255,255,255))
    for x in range(DX):
      for y in range(DY):
         drawSquare(x,y,P[x,y])
    
    pygame.display.update()
    
