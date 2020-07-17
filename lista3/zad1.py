def czy_pierwsza(n):
    x=1
    for i in range(2,n-1):
        if n % i==0:
           x=0
           break
    return x


licz=0
for i in range(1,100000):
    x=str(i)
    if "777" in x:
         x=int(x)
         if czy_pierwsza(x)==1:
             print(x)
             licz=licz+1

print("takich liczb jest:",licz)
    
