from turtle import *


def prostokat(x,y):
        fd(x)
        rt(90)
        fd(y)
        rt(90)
    
        fd(x)
        rt(90)
        fd(y)
        rt(90)
        
        
    
    
def konwertuj(n):
    liczba=[]
    while(n!=0):
        if (n%2==0):
            liczba.append(0)
        else: liczba.append(1)
        n=n//2
    return liczba


def rysuj(n):
    L=konwertuj(n)
    i=len(L)-1
    while(i>=0):
    	if (L[i]==0):
    	    prostokat(20,30)
    	    pu()
    	    fd(40)
    	    pd()
    	elif(L[i]==1):
    	
    	    rt(90)
    	    fd(30)
    	    lt(90)
    	    pu()
    	    fd(20)
    	    lt(90)
    	    fd(30)
    	    rt(90)
    	    
    	    pd()
    	    
    	i=i-1
    		
    		
    		
    		
    		
    		
rysuj(40)

input()
