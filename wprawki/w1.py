from turtle import *
from random import randint, random
import numpy as np

D=10
tab = np.random.rand(D, D,3)

def kwadrat(k,kolor):
   fillcolor([float(x) for x in kolor])
    
   begin_fill()
   for i in range(4):
        fd(k)
        rt(90)
   end_fill()

def move(x, y):
    pu()
    goto(x, y)
    pd()

def piramida(n,k):
    i=n
    while(i>0):
          j=i
          while(j>0):
                print(kwadrat(k,tab[i,j]))
                fd(k)
                j=j-1
          move((k*(n-i+1)/2),k*(n-i+1))
          i=i-1


piramida(5,10)
input()
