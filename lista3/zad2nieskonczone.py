from math import sqrt



def czy_pierwsza(n):
    x=True
    i=2
    while(i*i<=n):
        if n % i==0:
           x=False
           break
        i+=1
    return x



ile_siodemek=7
ile_cyfr=10
pozostale=ile_cyfr-ile_siodemek

szczesliwa= int('7'*ile_siodemek)



