
from turtle import fd, bk, lt, rt,ht,  speed, penup, pendown
from math import sqrt

def kwadrat(bok):
    for i in range(4):
        fd(bok)
        rt(90)


i=10
while(i<250):
     kwadrat(i)
     lt(135)
     penup()
     fd(i/5)
     pendown()
     rt(135)
     i=i+i/5*sqrt(2)

input()
 

