from collections import defaultdict as dd

	
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




plik=open('slowa.txt')

slowa=dd(set)

for w in plik:
	
	w=w.strip()
	slowa[len(w)].add(w)
	
		
szyfrogramy=dd(set)
szyfr=dict()
for dlugosc in slowa:
	for wyraz in slowa[dlugosc]:
		szyfrogramy[dlugosc].add(przek(wyraz))
		szyfr[przek(wyraz)]=wyraz

zdanie2='udhufńfd ąuąuęąę yrrożdśś śdśsdtsć'
zdanie='fulfolfu ćtąśśótą tlźlźltą'
zdanie=zdanie.split()
odsz=''
for slowo in zdanie:
	s=przek(slowo)
	dl=len(slowo)
	if s in szyfrogramy[dl]:
		odsz+=szyfr[s]
		odsz+=' '

print(odsz)



	
