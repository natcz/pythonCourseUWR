from collections import defaultdict as dd

alfabet = ['a','ą','b','c','ć','d','e','ę','f','g','h','i','j','k','l','ł','m','n','ń','o','ó','p','r','s','ś','t','u','w','y','z','ź','ż']
alf={}
zbiorliter=set(alfabet)

for i in range(len(alfabet)):
	alf[alfabet[i]]=i
	
def ceasar(s,k):
	wynik=''
	for i in range(len(s)):
		poz=alf[s[i]]
		if(poz+k<=31):
			wynik+=alfabet[poz+k]
		else:
			wynik+=alfabet[(poz+k)%31 -1]
		
	


	return wynik
	
def zle_slowo(w):
	for litera in w:
		if litera not in zbiorliter:
			return False
		elif len(w)==1:
			return False
	return True
	
	
def najdlcesarskie(dlugosci,slowa):
	
	for i in range(len(dlugosci)):
		L=set()
		for s in slowa[dlugosci[i]]:
			for k in range(1,32):
				slowo2=ceasar(s,k)
				
				if(slowo2 in slowa[dlugosci[i]]):
					L.add(s)
		if(L!=set()):
			return L
	return None
	
				

plik=open("popularne.txt")


slowa=dd(set)
dl=set()

for w in plik:
	w.split()
	w=w.strip()
	if (zle_slowo(w)==False):
		continue
	else:
		slowa[len(w)].add(w)
		dl.add(len(w))
dlugosci=list(dl)	
dlugosci.sort(reverse=True)


print(najdlcesarskie(dlugosci,slowa))





