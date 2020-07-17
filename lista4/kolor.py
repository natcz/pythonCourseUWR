from turtle import *
from random import randint, random
import numpy as np

tracer(0,1)

BOK = 10
D = 20

tab = np.random.rand(D, D,3)

def move(x, y):
    pu()
    goto(x, y)
    pd()
    
def kwadrat(x, kolor):
    fillcolor([float(x) for x in kolor])
    
    begin_fill()
    for i in range(4):
        fd(BOK)
        rt(90)
    end_fill()



def rysuj_tablice(tab):
    for x in range(D):
        for y in range(D):
            move( BOK * x,BOK * y)
            kwadrat(BOK, tab[x,y])
       
tab[0:5, 0:5] *= 0.3
tab[10:15, 0:5] *= 0.3
tab[5:10, 5:10] *= 0.3
tab[15:20, 5:10] *= 0.3
tab[0:5, 10:15] *= 0.3
tab[10:15, 10:15] *= 0.3
tab[5:10, 15:20] *= 0.3
tab[15:20, 15:20] *= 0.3


rysuj_tablice(tab)
input() 
  
