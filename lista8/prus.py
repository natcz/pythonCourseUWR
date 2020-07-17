import random
def literki(s):
	slowo={}
	pomocniczy=set()
	for i in range(len(s)):
		if s[i] not in pomocniczy: 
			slowo[s[i]]=1
			pomocniczy.add(s[i])
		else:
			slowo[s[i]]+=1
	return slowo

def czy_ukladalne(s1,s2):
	pierwsze=literki(s1)
	drugie=literki(s2)
	zbior1=set(pierwsze)
	zbior2=set(drugie)
	ukladalne=True
	for i in range(len(s2)):
		if(s2[i] not in zbior1):
			ukladalne=False
			break
		elif(pierwsze[s2[i]]<drugie[s2[i]]):
			ukladalne=False
			break
		else:
			continue
			
	return ukladalne
	
def zagadka(osoba,lista):
	uklad=[]
	osoba=osoba.lower()
	''.join(osoba.split())
	for i in range(len(lista)):
		if(czy_ukladalne(osoba,lista[i])==True):
			uklad.append(lista[i])
	
	wynik=[]
	powt=set()
	for i in range(len(uklad)):
		for j in range (len(uklad)):
			gotowe=uklad[i]+" "+uklad[j]
			odwrotna=uklad[j]+" "+uklad[i]
			if(odwrotna not in powt):
				powt.add(gotowe)
				if(len(gotowe)==len(osoba)):
					if(czy_ukladalne(osoba,gotowe)==True):
						wynik.append(gotowe)
			
					
				
	return wynik				
				







plik=open('popularne.txt')
L=[]
for w in plik:
	w.split()
	w=str(w)
	w=w.strip()
	L.append(w)


print(zagadka('gabrys czerep',L))




