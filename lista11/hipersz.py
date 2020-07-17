
from math import sqrt,floor

def czy_pierwsza(n):
    x=1
    a=floor(sqrt(n))
    for i in range(2,int(a)):
        if n % i==0:
           x=0
           break
    return x
    

cyfry=[str(x) for x in range (10)]

szczesliwa='7777777'

listap2=[x+y for x in cyfry for y in cyfry]
listap3=[x+y+z for x in cyfry for y in cyfry for z in cyfry]

lp3=[szczesliwa+a for a in listap3]+[b+szczesliwa for b in listap3]
lp2=[x+szczesliwa+y for x in cyfry for y in listap2]+[x+szczesliwa+y for x in listap2 for y in cyfry]

wszystkie=lp3+lp2


L=set()
for liczba in wszystkie:
	if (liczba[0]=='0'):
		continue
	if(czy_pierwsza(int(liczba))==1):
		L.add(liczba)
print(len(L))
	

