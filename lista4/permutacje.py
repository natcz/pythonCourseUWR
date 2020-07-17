import random


def randperm(n):
	L=[]
	NOWA=[]
	for i in range (n):
	   L.append(i)
	   
	for i in range (n):
		x=random.choice(L)
		NOWA.append(x)
		L.remove(x)
		
	return NOWA
	
	



for i in range(10):
	print(randperm(10))	

	
