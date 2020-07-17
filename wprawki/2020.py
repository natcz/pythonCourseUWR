cyfry="0123456789"
znaki="+-* "
znaki1="+-*"

cyfry=list(cyfry)
znaki=list(znaki)
znaki1=list(znaki1)

def zle_wyrazenie(napis):
	if(napis[-1]=='+' or napis[-1]=='-'or napis[-1]=='*'):
		return True
	return False
	



def kombinacje(L):
	if L==[]:
		return ['']
	else:
		e=L[0]
		reszta=kombinacje(L[1:])
		if(e=='0'):
			return [e+x+r for x in znaki1 for r in reszta]
		else:
			return [e+x+r for x in znaki for r in reszta]
		
	

wszystkie=kombinacje(cyfry)

for napis in wszystkie:
	if (zle_wyrazenie(napis)==True):
		continue
	else:
		x=eval(napis.replace(" ",""))
		if(x==2020):
			print(napis.replace(" ",""))
		
	


