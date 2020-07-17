
from turtle import *
import random
import numpy as np

tracer(0,1)
txt = """
......................
......................
......................
......................
......................
......................
......................
..###.................
....#.................
...#..................
......................
"""





tab = [ list(wiersz) for wiersz in txt.split()]
tab.reverse()
MY = len(tab)
MX = len(tab[0])
BOK=10
def move(x, y):
    pu()
    goto(x, y)
    pd()
def kwadrat(x,z, kolor):
    fillcolor([float(x) for x in kolor])
    
    begin_fill()
    for i in range(4):
        fd(BOK)
        rt(90)
    end_fill()
    move( BOK* x,BOK * z)
        
def rysuj_plansze(tab):
    clear()
    for y in range(MY):
        for x in range(MX):
            if tab[y][x] == '.':
                kolor = [0.2,0.3,0.3] 
            else:
                kolor =  [0.1,0.1,0.1]   
            kwadrat(x, y, kolor)
            
    update()        

def liczba_sasiadow(x, y):
    ls = 0
    for dx,dy in [ (1,0), (0,1), (-1, 0), (0, -1), (1,1), (-1,1), (1,-1), (-1,-1)]:
        nx = (x + dx) % MX
        ny = (y + dy) % MY
        if tab[ny][nx] == '#':
            ls += 1
    return ls
   
def pusta_plansza():
    return [MX * ['.'] for i in range(MY)]
            
# reguły gry w życie:
# jeżeli komórka pełna ma 2 lub 3 sąsiadów przeżywa, wpp ginie
# jeżeli komórka pusta ma 3 sąsiadów, to rodzi się nowa
#
#
nowa = pusta_plansza()

zbior_stanow = set()

while True:
    rysuj_plansze(tab)

    for y in range(MY):
        for x in range(MX):
            n = liczba_sasiadow(x, y)
            if tab[y][x] == '.' and n == 3:
                nowa[y][x] = '#'
            elif tab[y][x] == '#' and 2 <= n <= 3:
                nowa[y][x] = '#'
    tab = nowa  
    
    s_nowa = str(nowa)
    
    if s_nowa in zbior_stanow:
        break
    zbior_stanow.add(s_nowa)
          
    nowa = pusta_plansza()      

print ('Koniec')
input()
