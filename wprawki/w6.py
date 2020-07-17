def nowa(L):
	new=[]
	j=0
	while j<len(L)-1:
		
		i=j
		a=[]
		ile=0
		while i<len(L) and L[i]==L[j] :
			
			a.append(L[i])
			i+=1
			ile+=1
		if a != []:	
			new.append(a)
		j+=ile
		
	return new
	
	
L=[1,2,3,2,3,3,4,5,5,5,5]
print(nowa(L))
			
