#!/usr/bin/env python

import pygame
from pygame.locals import *
from sys import exit
from random import randint
import math
import random

MX = 640
MY = 480
 
pygame.init()
screen = pygame.display.set_mode((MX, MY))
clock = pygame.time.Clock()

point = [200, 200]

delta_x,delta_y = 3,3
t = 0

while True:
    clock.tick(30)  
    t += 1      
    
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        
    pressed_keys = pygame.key.get_pressed()
          
    if pressed_keys[K_LEFT]:
          point[0] -= delta_x
          
    if pressed_keys[K_RIGHT]:
         point[0] += delta_x    
                                    
    if pressed_keys[K_UP]:
          point[1] -= delta_y  

    if pressed_keys[K_DOWN]:
         point[1]  += delta_y 
  
    screen.fill((255,255,255))
    
    pygame.draw.circle(screen, (0,0,0), point, 50)
    pygame.draw.circle(screen, (250,200,0), point, 20 + t % 15)
          
    pygame.display.update()

