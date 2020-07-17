from math import sqrt

def blok(n,a):
   
    return n*a
    
    
def bloki(m):
    L=[]
    for i in range(1,m+1):
        if i%6==0:
           L.append(blok(i,"$"))
        elif i%6==1:
           L.append(blok(i,"@"))
        elif i%6==2:
           L.append(blok(i,"*"))
        elif i%6==3:
           L.append(blok(i, "#"))
        elif i%6==4:
           L.append(blok(i,"&"))
        elif i%6==5:
           L.append(blok(i,"%"))
    return L
           
           
           
def filtr(L):
    NOWA=[]
    for i in range (len(L)):
        x=L[i]
        y=len(x)
        pierw=int(sqrt(y))
        if (y == pierw*pierw):
           NOWA.append(x)
        else: continue
    return NOWA
        
        

L=filtr(bloki(111))

for i in range (len(L)):
    print(L[i])











        
           
           

