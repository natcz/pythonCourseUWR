
from math import pow
import random

def zle_slowo(w):
	return any(znak in w for znak in '/\_/”')
def kropka(w):
	return any(znak in w for znak in '.,…')
def myslnik1(w):
	return any(znak in w for znak in '–')
def myslnik2(w):
	return any(znak in w for znak in '-')
	
wystapienia={}	
plik=open('lalka.txt')

for x in plik:
    for slowo in x.split():
        slowo = slowo.lower()
        if zle_slowo(slowo):
        	continue
        if len(slowo)<4:
        	continue
        if kropka(slowo):
        	slowo=slowo[:-1]
        if myslnik1(slowo):
        	slowo=slowo.split('–')
        	if slowo[0] in wystapienia:
        		wystapienia[slowo[0]] += 1
        	else:
        		wystapienia[slowo[0]] = 1
        	if slowo[1] in wystapienia:
        		wystapienia[slowo[1]] += 1
        	else:
        		wystapienia[slowo[1]] = 1
        	continue
        	
        if myslnik2(slowo):
        	slowo=slowo.split('-')
        	if slowo[0] in wystapienia:
        		wystapienia[slowo[0]] += 1
        	else:
        		wystapienia[slowo[0]] = 1
        	if slowo[1] in wystapienia:
        		wystapienia[slowo[1]] += 1
        	else:
        		wystapienia[slowo[1]] = 1
        	continue
        	
        if slowo in wystapienia:
            wystapienia[slowo] += 1 
        else:
            wystapienia[slowo] = 1  
            
              
for i in range(3):
	alfa=random.randint(1,10)
	print("waga=",alfa)
	ciezkie = sorted( wystapienia.keys(), key=lambda x:wystapienia[x]*pow(len(x),alfa)) 
	ciezkie.reverse()

	for w in ciezkie[:10]:
		print (w)
	print()
	
plik.close()


