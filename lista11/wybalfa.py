from collections import defaultdict as dd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

 
plik=open("wyniki_wyborow.tsv")

dane=list()#miasto-ilemandatow-wyniki

for w in plik:
	w=list(w.split("\t"))
	dane.append(w[1:-1])
	
komitety=dane[0][2:]#nazwy partii
dane=dane[1:]
wyniki=dd(list)#miasto,alfa -wyniki[wynik,partia] 

for lista in dane:
	miasto=lista[0]
	for dzielnik in range(1,int(lista[1])):
		alfa=0.1
		while(alfa<2):
			x=dzielnik**alfa
			for i in range(len(lista[2:])):
				partia=komitety[i]
				procent=lista[i+2]
				if(',' in procent):
					procent=procent.replace(',','.')
					procent=float(procent)
					wyniki[(miasto,alfa)].append([procent/x,partia])
					continue
				if(procent=='–'):
					procent='0'
				procent=int(procent)
				wyniki[(miasto,alfa)].append([procent/x,partia])
			alfa+=0.5


for lista in wyniki:
	wyniki[lista].sort(reverse=True)
	



ilemand=[]#miasto-ilemand
for lista in dane:
	ilemand.append([lista[0],int(lista[1])])
	
for i in range (len(ilemand)):
	for lista in wyniki:
		if(ilemand[i][0]==lista[0]):
			wyniki[lista]=wyniki[lista][:ilemand[i][1]]	

ostateczne=dd(int)#partia,alfa-wynik

for lista in wyniki:
	for i in range (len(wyniki[lista])):
		for partia in komitety:
			p=wyniki[lista][i][1]
			if p==partia:
				alfa=lista[1]
				ostateczne[(partia,alfa)]+=1
					
			
	
	
prawdziwewyn={'PiS': 235, 'KO': 134, 'SLD': 49, 'PSL': 30, 'KWiN': 11, 'MN': 1}
			
stopienprop=dd(list)

for wynik in ostateczne:
	for partia in prawdziwewyn:
		if(partia==wynik[0]):
			stopienprop[wynik[1]].append((partia,abs(prawdziwewyn[partia]-ostateczne[wynik])))
			
			

partie=[]
st=[]
alfa=1.1
for x in stopienprop[alfa]:
	partie.append(x[0])
	st.append(x[1])	


plt.title("Alfa:"+str(alfa))
plt.ylabel('Stopnień nieproporcjonalności')
plt.xlabel('Partia')
plt.bar(partie,st)
plt.show()
				
						




	




