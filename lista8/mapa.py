from turtle import *
import random 
BOK=5
tracer(0,1)
kolory = ['green', (0.5, 1, 0) , 'yellow', 'orange', 'red', (0.5, 0,0) ]
def move(x, y):
    pu()
    goto(x, y)
    pd()
def kwadrat(bok,a,x,y,wsk):
	move( bok* x+wsk,bok * y-wsk)
	begin_fill()
	color(kolory[a],kolory[a])
	for i in range(4):
		fd(bok)
		rt(90)
	end_fill()
  

L = [[0] * 100 for i in range(100)]

for i in range(5000):
	a=random.randint(1,100)
	b=random.randint(0,99)
	c=random.randint(0,99)
	if(L[b][c]==0):
		L[b][c]=a

for i in range(50000):
	b=random.randint(0,99)
	c=random.randint(0,99)
	if (b==0 and c==0):
		L[b][c]+=L[b+1][c]+L[b][c+1]+L[b+1][c+1]
		L[b][c]=L[b][c]/4
	elif(b==99 and c==0):
		L[b][c]+=L[b-1][c]+L[b][c+1]+L[b-1][c+1]
		L[b][c]=L[b][c]/4
	elif(b==0 and c==99):
		L[b][c]+=L[b][c-1]+L[b+1][c]+L[b-1][c-1]
		L[b][c]=L[b][c]/4
	elif(b==99 and c==99):
		L[b][c]+=L[b-1][c]+L[b][c-1]+L[b-1][c-1]
		L[b][c]=L[b][c]/4
	elif(b==0):
		L[b][c]+=L[b][c-1]+L[b+1][c]+L[b][c+1]+L[b+1][c+1]+L[b+1][c-1]
		L[b][c]=L[b][c]/6
	elif(b==99):
		L[b][c]+=L[b][c-1]+L[b-1][c]+L[b][c+1]+L[b-1][c-1]+L[b-1][c+1]
		L[b][c]=L[b][c]/6
	elif(c==0):
		L[b][c]+=L[b-1][c]+L[b+1][c]+L[b][c+1]+L[b+1][c+1]+L[b-1][c+1]
		L[b][c]=L[b][c]/6
	elif(c==99):
		L[b][c]+=L[b][c-1]+L[b-1][c]+L[b+1][c]+L[b-1][c-1]+L[b+1][c-1]
		L[b][c]=L[b][c]/6
	else:
		L[b][c]+=L[b][c-1]+L[b-1][c]+L[b+1][c]+L[b][c+1]+L[b-1][c-1]+L[b+1][c-1]+L[b+1][c+1]+L[b-1][c+1]
		L[b][c]=L[b][c]/9
	
	


for i in range(len(L)):
	for j in range(len(L[i])):
		if(L[i][j]<=50):
			L[i][j]=int(L[i][j]//10)
		else:
			L[i][j]=5
		kwadrat(5,L[i][j],i,-j,-300)


	
input()		



