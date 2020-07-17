from collections import defaultdict as dd
 
plik=open("wyniki_wyborow.tsv")

okregi=dd(list)#nazwa okregu-wyniki poszczegolnych partii
dane=list()
mandaty=list()#nazwa okregu-ilosc wszystkich mandatow

for w in plik:
	w=list(w.split("\t"))
	dane.append(w[1:-1])
	

dane2=dane[1:]
komitety=dane[0][2:]

for lista in dane2:
	okregi[lista[0]]=lista[2:]
	mandaty.append((lista[0],lista[1]))
	
wyniki=dd(list) #miasto-wynik,partia


for i in range(len(mandaty)):
	L=list()
	miasto=mandaty[i][0]
	for j in range(1,int(mandaty[i][1])+1):
		for x in range(len(okregi[miasto])):
			procent=okregi[miasto][x]
			if(',' in procent):
				procent=procent.replace(',','.')
				procent=float(procent)
				L.append((procent/j,komitety[x]))
				continue
			if(procent=='–'):
				procent='0'
			procent=int(procent)
			L.append((procent/j,komitety[x]))		
	wyniki[miasto]=L

wygrane=dict()# miasto - ostateczne wyniki
ostateczne=dd()#miasto-partia-ile mandatow

for i in range(len(mandaty)):
	miasto=mandaty[i][0]
	ile=int(mandaty[i][1])
	wyniki[miasto].sort(reverse=True)
	wygrane[miasto]=wyniki[miasto][:ile]
	a=list(set([x[1] for x in wygrane[miasto]]))
	b=dict()
	for i in range(len(wygrane[miasto])):
		for x in range(len(a)):
			if(wygrane[miasto][i][1]==a[x]):
				if a[x] not in b:
					b[a[x]]=1
				else:
					b[a[x]]+=1
	ostateczne[miasto]=b
	
calykraj=dict([(x,0) for x in komitety])	

for miasto in ostateczne:
	for partia in ostateczne[miasto]:
		calykraj[partia]+=ostateczne[miasto][partia]	

	
print(calykraj)
		
	

	
	

	




		
		

