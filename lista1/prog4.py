from losowanie_fragmentow import losuj_fragment

#for i in range(5):
	#print ( losuj_fragment() )
		

def losuj_haslo(n):
    tekst=""
    while True:
         x=losuj_fragment()
         a=len(x+tekst)
         if a<=n:
            if (n-a) !=1:
               tekst += x
         if len(tekst)==n:
            break
     
    return tekst

for i in range(10):
    print(losuj_haslo(8))
for i in range(10):
    print (losuj_haslo(12))
	
