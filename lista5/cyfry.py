from turtle import *
import random 
from duze_cyfry import daj_cyfre
import numpy as np

tracer(0,1)

bok=10
D = 20

tab = np.random.rand(D, D, 3)



def move(x, y):
    pu()
    goto(x, y)
    pd()
    
def kwadrat(x, kolor):
    fillcolor([float(x) for x in kolor])
    
    begin_fill()
    for i in range(4):
        fd(bok)
        rt(90)
    end_fill()

def rysuj_cyfre(n,wsk):
    lista = daj_cyfre(n)
    dl=len(lista)
    k1=random.randint(1,D-1)
    k2=random.randint(1,D-1)
    for i in range (dl):
        napis=str(lista[i])
        for a in range(len(napis)):
             if napis[a]==' ':
                  continue
             move(bok*(a)+wsk,bok*(-i))
             kwadrat(bok,tab[k1,k2]) 
               
               
  
          
      
      
      
      
      

def rysuj_liczbe(n):
    
    wsk=-n*50
    for i in range(n):
         
         rysuj_cyfre(i,wsk)
         wsk+=70


rysuj_liczbe(9)

input()   

             




