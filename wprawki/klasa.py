

	

class Num:

	def __init__(self,arg):
		self.val=arg
		
	def eval(self,variables):
		x=self.val
		return x
	
class Var:
	
	def __init__(self,arg):
		self.name=arg

	def eval(self,slownik):
		x=self.name
		return slownik[x]
		
class Exp:

	def __init__(self,znak,a,b):
		self.tree=[znak,a,b]
		
		
		
	def eval(self,slownik):
		znak,x,y=self.tree
		s=str(x.eval(slownik))+str(znak)+str(y.eval(slownik))
		return eval(s)
		
	
		
		
		
		
		
letters=['x','y','z','q','e','u','p']
variables=dict(zip([letter for letter in letters],[num for num in range(7)]))		
		
		
		
		

e1=Num(5)
e2=Var('q')	
w=Exp("+",e1,e2)

print(e1.eval(variables))
print(e2.eval(variables))
print(w.eval(variables))
		
	

		
	
	

