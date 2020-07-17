	
slo=set()
slowa=[]
wynik=set()
powt=set()
	
for slowo in open("slowa2.txt"):
	x=slowo[:-1]
	slowa.append(x)
	slo.add(x)
	
for i in range (len(slowa)):
	nowe=slowa[i][::-1]
	if(nowe in slo and slowa[i] not in powt ):
		wynik.add((nowe,slowa[i]))
		powt.add(nowe)
		


if(("pokaz","zakop") in wynik and ("zakop","pokaz") in wynik):
	print("ups")
print(wynik)
print(len(wynik))
	
		
	
			
#a="alicja"	
#print(a[::-1])





	

