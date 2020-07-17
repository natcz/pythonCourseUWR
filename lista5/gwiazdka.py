import random



def usun_duplikaty(L):
    par=[]
    wynik=[]
    for i in range(len(L)):
    	par.append((L[i],i))
    	
    par.sort()	
    
    
    wart=par[0][0]
    poz=par[0][1]
    
    for i in range(1,len(par)):
    	
    	if wart == par[i][0]:
    		if par[i][1]<poz:
    			poz=par[i][1]
    	else:
    		wynik.append((poz,wart))
    		wart=par[i][0]
    		poz=par[i][1]
    	if(i==len(par)-1):
    		if(par[i][0]!=par[i-1][0]):
    			wynik.append((par[i][1],par[i][0]))
    		else:
    			wynik.append((par[i-1][1],par[i-1][0]))
    			
    wynik.sort()
    ostateczna=[]
    	
    for i in range(len(wynik)):
    	ostateczna.append(wynik[i][1])
    	
    	
    return ostateczna
    
    
    
def losowa_lista(N):
    wynik = []
    for i in range(N):
        wynik.append(random.randint(0,100000))
    return wynik 
    
       
   
print (usun_duplikaty([1,2,3,8,3,1,8,4,4,9,9]))

print (len(usun_duplikaty(losowa_lista(500000))))
print ("Skonczyłem!")       
    
print(usun_duplikaty([1,2,4,4,6,2,3,4,7,5]))

