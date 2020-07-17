from collections import defaultdict as dd
import random

pol_ang = dd(list)
wyrazy=set()
popularne={}



def tlumacz(zdanie):
    wynik = []
    for w in zdanie:
        if w in pol_ang:
           a=pol_ang[w]
           maks=a[0]
           powtorzenia=[]
           powt=False
           for i in range(1,len(a)):
           		try:
           			if (popularne[a[i]]>popularne[maks]):
           				maks=a[i]
           			elif(popularne[a[i]]==popularne[maks]):
           				powtórzenia.append(a[i])
           				powt=True
           				
           		except KeyError:
           
           			continue 
           			
           if(powt==True):
           	maks=random.choice(powtorzenia)
           	powtorzenia.clear()
           	powt=False
           	
           wynik.append(maks)
           		
        else:
            wynik.append('[?]')
    return ' '.join(wynik)
    
    
    
for wiersz in open('brown.txt'):
	wiersz=wiersz.strip()
	slowa=wiersz.split()
	for i in range(len(slowa)):
		if(slowa[i] not in wyrazy):
			popularne[slowa[i]]=1
			wyrazy.add(slowa[i])
		else:
			popularne[slowa[i]]+=1
			
	
   
for wiersz in open('pol_ang.txt'):
    
    wiersz = wiersz.strip()
    if '=' not in wiersz:
        continue
    pola = wiersz.split('=')
    if len(pola) != 2:
        continue
    p, a = pola
    pol_ang[p].append(a)
    

zdanie=input('Zadanie do przetlumaczenia:')
zdanie = zdanie.split()
print (tlumacz(zdanie))


