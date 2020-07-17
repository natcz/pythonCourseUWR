#!/usr/bin/env python

import pygame
from pygame.locals import *


from sys import exit
from random import randint
import math
import random
 
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
N = 10

points = []
colors = []
rs = []
vs = []
forgotten=set()
  
def rand_color():
   r = 32*random.randint(0,7)
   g = 32*random.randint(0,7)
   b = 22*random.randint(0,7)
   return (r,g,b)
   
for i in range(N):
  points.append( [random.randint(0,639), random.randint(0,479)] )
  colors.append( rand_color() )
  rs.append(random.randint(3,10))
  vs.append( [random.randint(-2,2), random.randint(-2,2)])
  
dead=N*[False]
points[0] = [50,50]
colors[0] = [0,0,0]
rs[0] = 10
delta_x,delta_y = 3,3

while True:
    clock.tick(30)        

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        
    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[K_LEFT]:
          points[0][0] -= delta_x
          
    if pressed_keys[K_RIGHT]:
         points[0][0] += delta_x    
                                    
    if pressed_keys[K_UP]:
          points[0][1] -= delta_y  

    if pressed_keys[K_DOWN]:
         points[0][1]  += delta_y 

    for i in range(1, len(points)):
        points[i][0] += vs[i][0]
        points[i][1] += vs[i][1]
    
    for i in range(len(points)):
      if points[i][0] >= 640:
        points[i][0] = 0
      if points[i][1] >= 480:
        points[i][1] = 0
        
      if points[i][0] < 0:
        points[i][0] = 639
      if points[i][1] < 0:
        points[i][1] = 479
        
      if i!=0 and abs(points[0][1]-points[i][1])<=rs[0] and abs(points[0][0]-points[i][0])<=rs[0]:
      	dead[i]=True
      	
      	
         
    
    for i in range(len(points)):
        if random.randint(0,50) == 0:
            vs[i][0] = random.randint(-3,3)
            vs[i][1] = random.randint(-3,3)
    
    screen.fill((255,255,255))
    bigger=False
    for i in range(N):
      if rs[i] and dead[i]==False:
        pygame.draw.circle(screen, colors[i] ,points[i], int(rs[i]))
      if dead[i]==True and i not in forgotten:
      	bigger=True
      	forgotten.add(i)
    print(bigger)     
        
    if rs[0]:
    	if bigger==True:
    		rs[0]+=4
    	pygame.draw.circle(screen, (255,255,0) ,points[0], int(rs[0]-4))
    	pygame.display.update()
    
