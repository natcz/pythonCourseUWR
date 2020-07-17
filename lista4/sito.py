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



def palindromy(a,b):
    L1=sito(b+1)
    M=[]
  
    for i in range (a-1,b):
        if i  in L1:
           x=str(i)
           f=True
           for j in range (len(x)//2):
               if x[j] != x[len(x)-j-1]: 
                  f=False
           if f==True:
               M.append(i)
    return M









print(palindromy(99,100000))









     
      







