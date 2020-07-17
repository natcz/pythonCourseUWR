def split(L):

	n=len(L)
	if(n%2==0):
		lewe=L[:(n//2)]
		prawe=L[n//2:]	
	else:
		lewe=L[:(n-1)//2]
		prawe=L[(n-1)//2:]
	return lewe,prawe
	
def merge(L1,L2):
	if(L1=[]):
		return(L2)
	if(L1=[]):
		return(L2)
	
		
		
		
	return wynik
	
def mergesort(L):
	
	if(len(L)==1):
		
		return L
	else:
		lewe,prawe=split(L)
		wynik=merge(mergesort(lewe),mergesort(prawe))
		
	return wynik






	
	
x,y=split([12,23,4,5,3,6,8])
print(x)
print(y)

a=[2,4,4,1,5]
b=[7,8,9]
print(merge(a,b))
print(merge(x,y))
print(mergesort(a))		
		
