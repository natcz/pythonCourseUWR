from itertools import permutations

def lamiglowka(napis):
	slowa,wynik=napis.split('=')
	slowo1,slowo2=slowa.split('+')
	zlepek=slowo1+slowo2+wynik
	literki=set() #unikalne litery wszystkich slow
	for litera in zlepek:
		literki.add(litera)
	if len(literki)>10: 
		return None
	listaperm=list(permutations(range(10),len(literki))) #lista permutacji liczb od 0 do 9 (tyle liczb ile jest unikalnych literek)
	for i in range(len(listaperm)):
		kodowanie=dict()
		kodowanie=dict(zip(literki,listaperm[i]))
		if (kodowanie[slowo1[0]]==0 or kodowanie[slowo2[0]]==0 or kodowanie[wynik[0]]==0):#pierwsza cyfra to nie moze byc 0
				continue
		else:
			liczba1=''
			liczba2=''
			liczbaw=''
			for litera in slowo1:
					liczba1+=str(kodowanie[litera])
			for litera in slowo2:
					liczba2+=str(kodowanie[litera])
			for litera in wynik:
					liczbaw+=str(kodowanie[litera])
			
				
			if(eval(liczba1+'+'+liczba2)==eval(liczbaw)):
					return kodowanie
		
	return None
		
	
	
print(lamiglowka("send+more=money"))
print(lamiglowka("ciacho+ciacho=nadwaga"))

	
	

