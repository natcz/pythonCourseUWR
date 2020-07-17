def srednia_liczba_cyfr(L):
	return sum([len(str(a)) for a in L])/len(L)
	



L=[1,2,35,45,5]	
print(srednia_liczba_cyfr(L))

def maksymalny_zysk(L):
	return max([j -L[i] for i in range(len(L)-1) for j in L[i+1:]])
	
print(maksymalny_zysk(L))

def czy_jest_tytulem(s):
	return all([a[0].upper()==a[0] and a[1:].lower()==a[1:] for a in s.split()])
	
s='Tata Ma Kota'
print(czy_jest_tytulem(s))

def pom(D):
	return max([abs(x-D[x]) for x in D.keys()])
def maks_skok(D):
	return [ x for x in D if abs(x-D[x])==pom(D)][0]
	
D={1:4,3:4,5:6,6:7}

print(maks_skok(D))

def  leksy(L):
	return [int(y) for y in sorted(str(x) for x in L)]
	
print(leksy(L))


 
