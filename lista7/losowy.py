
		
	
from turtle import *
import random
tracer(0,1)

BOK=10
y=-400

def move(x, y):
    pu()
    goto(x, y)
    pd()
def kwadrat(x,z, kolor,wsk):
    move(x+wsk, z+wsk)
    fillcolor([float(x) for x in kolor])
    
    begin_fill()
    for i in range(4):
        fd(BOK)
        rt(90)
    end_fill()
    
    
    
plik=open('niespodzianka.txt')
wszystkie=[]
for wiersz in plik:
	
	L=wiersz.split()
	x=0
	for i in range (len(L)):
		x+=BOK
		teraz=L[i][1:-1]
		wszystkie.append([x,y,teraz])
	y=y+BOK
			
	
	
i=len(wszystkie)
while (i>0):
	losowy=random.choice(wszystkie)
	kolor=list( eval(losowy[2]))
	for a in range(len(kolor)):
		kolor[a]=kolor[a]/256
	kwadrat(losowy[1],-losowy[0],kolor,250)
	wszystkie.remove(losowy)
	i=len(wszystkie)
	if((i%5)==0):
		update()
	
	
	
input()
plik.close()	



	

