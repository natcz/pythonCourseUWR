from turtle import *
import random
import numpy as np
kolory=['blue', 'lightblue','pink','red','orange','purple']



def kwadrat(bok):
    begin_fill()
    for i in range(4):
      fd(bok)
      rt(90)
    end_fill()
    
def murek(s,bok):
  
  for a in s:
    
     if a == 'f':
         kwadrat(bok)
         fd(bok)
     elif a=='c':
     	color('black',random.choice(kolory))
     elif a=='k':
     	color('black',kolory[1])
     elif a=='p':
     	color('black',kolory[0])
     elif a=='j':
     	color('black',kolory[4])	
     	
     elif a == 'b':
         kwadrat(bok)
         fd(bok)         
     elif a == 'l':
         bk(bok)
         lt(90)
     elif a == 'r':
        rt(90)
        fd(bok)
def kwadratzkwadratow(x):
	napis=x*'f'
	for i in range (x-1):
		if i%2==1:
			napis+='clfl'
		else:
			napis+='crfr'
		napis+=(x-1)*'f'
	return napis

def spirala(x):
	napis='p'
	i=x
	while(i>0):
		napis+='f'*i
		napis+='r'
		if i%3==0:
			napis+='k'
		elif i%3==1:
			napis+='j'
		else:
			napis+='p'
		i-=1
	
	return napis
	
		
        


ht()


murek(spirala(10),10)
murek(kwadratzkwadratow(10),10)

 


input()
