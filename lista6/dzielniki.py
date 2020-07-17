def sito(n):
    
    L=[0]+[0]+(n-1)*[1]
    pozycja=2
    licznik=pozycja*pozycja
    while (licznik<=n):
         if L[pozycja]==1:
            a=licznik
            while a<=n:
                L[a]=0
                a+=pozycja
         pozycja+=1
         licznik=pozycja*pozycja
         
    NOWA=[]
    for i in range (1,n+1):
        if L[i]==1:
           NOWA.append(i)  
    return NOWA
    
    
def dzielniki(n):
    L=sito(n)
    wynik=set()
    for i in range(len(L)):
        if n%L[i]==0:
            wynik.add(L[i])
        else: continue
    return wynik
   
print(dzielniki(7))
print(dzielniki(2))
print(dzielniki(45))
	
