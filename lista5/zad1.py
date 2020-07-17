def F(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1

def energia(n):
    licznik=0
    while(n!=1):
       n= F(n)
       licznik+=1
    return licznik

def sredniazlisty(L):
    suma=0
    for i in range (len(L)):
        suma+=L[i]
    return suma/len(L)

def mediana(L):
    L.sort()
    if len(L)%2 != 0:
       return L[(len(L)-1)/2]
    else:
       x= L[(len(L)-1)//2]
       y=L[len(L)//2]
       sred=(x+y)/2
       return sred
        

def analiza_collatza(a,b):
    print("Analiza dla:",a,b)
    L=[]
    for i in range (a,b+1):
        x= energia(i)
        L.append(x)
    print("Energie:", L)
    print("Maksymalna energia:" , max(L))
    print("Najmniejsza energia:", min(L))
    print("Średnia energia:", sredniazlisty(L))
    print("Mediana energii:", mediana(L))
    print()



analiza_collatza(7,10)

analiza_collatza(20,25)

    
    

