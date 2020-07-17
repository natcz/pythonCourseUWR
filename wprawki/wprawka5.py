def pary(n):
	L=[(i,j-i) for j in range(n+1) for i in range(j+1) ]
	return L



print(pary(3))

