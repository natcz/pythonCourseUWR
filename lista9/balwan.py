
def  kolko(n):
	L = [[" "] * n for i in range(n)]
	promien=n/2
	a=n//2
	b=a
	for y in range(len(L)):
		for x in range(len(L[y])):
			if((x-a)**2 + (y-b)**2<=promien**2):
				L[y][x]='#'
	wynik=[]
	for y in range(len(L)):
		wynik.append(''.join(L[y]))
	return wynik
		
def balwan(kula1,kula2,kula3):
	kule=[kula1,kula2,kula3]
	for i in range(3):
		L=kolko(kule[i])
		for k in range(len(L)):
			a=str(L[k])
			print(" "*(3-i),a,sep='')
	

	
			
	
balwan(9,11,13)

