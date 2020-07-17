from math import log

def silnia(n):	
    s=1
    for i in range(1,n+1):
        print(i)
        s=s*i
       
        print(i)
    return s       
      

for i in range(4,101):
    a=silnia(i)
    x=str(a)
    liczba=len(x)
    if liczba%100==13 or liczba%100==14 or liczba%100==12:
       print (i,"! ma ",liczba,"cyfr")
    elif liczba%10==2 or liczba%10==3 or liczba%10==4:
         print(i,"! ma ",liczba,"cyfry")
    else:
         print(i,"! ma ",liczba,"cyfr")

print (silnia(5))
