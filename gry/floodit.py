#!/usr/bin/env python

import pygame
from pygame.locals import *
from sys import exit
from random import randint
import math
import random

DX = 14
DY = 14
DD = 20

MX = DX*DD
MY = DX*DD
 
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

def fields_around(start):
  x,y = start
  wynik = []
  for dx,dy in [ (0,1), (0,-1), (1,0), (-1,0)]:
     nx = x + dx
     ny = y + dy
     if (nx,ny) in P:
       wynik.append( (nx,ny) )
  return wynik
    
def neighbours(start):
  x,y = start
  k1 = P[x,y]
  wynik = []
  for f in fields_around(start):
    if P[f] == k1:
       wynik.append(f)
  return wynik
       

P = {}

colors = list(Col.keys())

def drawSquare(x,y,c):
  r = pygame.Rect(x * DD, y * DD, DD, DD)
  pygame.draw.rect(screen, Col[c], r)

x = 0
y = 0  


for x in range(DX):
  for y in range(DY):
    P[x,y] = random.choice(colors)
    

#TODO: jak ułatwić planszę?

def reachable(a):
    visited = {a}
    queue = [a]
    
    while queue != []:
        x = queue[0] #pobranie z kolejki
        del queue[0] #pobranie (cd)

        for n in neighbours(x):
            if n not in visited:
                visited.add(n)
                queue.append(n)
    return visited    
  
Start = (0,0)
zakolorowane =  reachable(Start)
nr = 1
      
while True:
    clock.tick(30)        
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == MOUSEBUTTONDOWN:
          x = event.pos[0] // DD
          y = event.pos[1] // DD
          c = P[x,y]  
          print ('Ruch nr',nr)
          nr += 1
          for p in zakolorowane:
            P[p] = c
          zakolorowane = reachable(Start)

    screen.fill((255,255,255))

    for x in range(DX):
      for y in range(DY):
         drawSquare(x,y,P[x,y])
    
    pygame.display.update()
    
