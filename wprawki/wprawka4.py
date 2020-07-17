L1=[[0,1,2],[6,7,8],[9,8,7]]
L2=[[0,1,2,3],[3,5,6,7],[4,5,4,5]]
L3=[]

def czydobra (L):
	
	jest=False
	dl=len(L)
	if (L==[]):
		return jest
		
	for i in range(dl):
		a=len(L[i])
		if (a!=dl):
			return jest
	jest=True
	return jest
	
def transpozycja(L):
	if (czydobra(L)==False):
		s="To nie jest macierz"
		return s
	nowa=[]
	pomoc=[]
	for i in range(len(L)):
		for j in range(len(L[i])):
			pomoc.append(L[j][i])
		nowa.append(pomoc)
		pomoc=[]
	return nowa
	
	
	
	
	
print(czydobra(L1))			
print(czydobra(L2))
print(czydobra(L3))
print(transpozycja(L1))			
print(transpozycja(L2))
print(transpozycja(L3))


 
		
		
	
