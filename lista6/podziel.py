def podziel(napis):
	i=0
	L=[]
	x=''
	while(i<len(napis)):
		
			
		if(napis[i]!=' '):
			if(i==len(napis)-1):
				x+=napis[i]
				L.append(x)
				break
			x+=napis[i]
		else:
			if (x!=''):
				L.append(x)
			x=''
			if(napis[i+1]!=' '):
				x=napis[i+1]
			i+=1
		i+=1
		
	return L
	
print(podziel("ala ma kota"))
print(podziel(" alama   kota inata  lia miala"))
print(podziel("     a l a m a k o t a  "))

