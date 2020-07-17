def suma(L):
	if L==[]:
		return [0]
	else:
		e=suma(L[1:])
		return e+[L[0]+reszta for reszta in e]
		
zbior=set(suma([1,2,3,4]))
print(zbior)
