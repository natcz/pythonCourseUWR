from turtle import *
import random

tracer(0,1)
BOK1=5
     
def prostokat(a,b):
    fd(a)
    lt(90)
    fd(b)
    lt(90)
    fd(a)
    lt(90)
    fd(b)
    lt(90)
    pu()
    fd(a)
    pd()

    
     
     
x=10
for i in range (20):
    y = random.randint(1,10)
    prostokat(BOK1,random.randint(x-y,x))
    x+=5
input()
