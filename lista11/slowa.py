def przek(slowo):
	cyferki=dict()
	for litera in slowo:
		cyferki[litera]=-1
	i=1
	for litera in slowo:
		if (cyferki[litera]==-1):
			cyferki[litera]=i
			i+=1
	wynik=''
	
	for a in range (len(slowo)):
		wynik+=str(cyferki[slowo[a]])
		if(a!=len(slowo)-1):
			wynik+='-'
		
	
	return wynik
	

print(przek('indianin'))
print(przek('tak'))
		
