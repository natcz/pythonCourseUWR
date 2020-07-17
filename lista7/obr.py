from turtle import *
BOK=10
tracer(0,1)
def move(x, y):
    pu()
    goto(x, y)
    pd()
def kwadrat(x,z, kolor,wsk):
    move( BOK* x+wsk,BOK * z-wsk)
    fillcolor([float(x) for x in kolor])
    
    begin_fill()
    for i in range(4):
        fd(BOK)
        rt(90)
    end_fill()
    
    
    
plik=open('niespodzianka.txt')
wszystkie=[]
for wiersz in plik:
	wiersz=wiersz.strip()
	L=list(wiersz.split())
	wszystkie.append(L)
for y in range(len(wszystkie)):
	for x in range(len(wszystkie[y])):
		print(wszystkie[y][x])
		kolor=list( eval(wszystkie[y][x]))
		for i in range(len(kolor)):
			kolor[i]=kolor[i]/256
		kwadrat(y,-x,kolor,-300)
input()
plik.close()	




