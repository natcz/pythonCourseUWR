class ListItem:
    def __init__(self, e):
        self.e = e
        self.n = None
        
    def __str__(self):
        return str(self.e)    

class LinkedList:
    def __init__(self, elems):
        self.first = None
        self.last = None
        self.length = 0
        
        for e in elems:
            self.append(e)  
            
    def append(self, e):
        new = ListItem(e)
        if self.first == None:
            self.first = new
            self.last = new
        else:
            self.last.n = new
            self.last = new
        self.length += 1  
        
    def __len__(self):
        return self.length    
        
    def __iter__(self):
        elem = self.first
        while elem:
            yield elem.e
            elem = elem.n   

    def iterator_li(self):
        elem = self.first
        while elem:
            yield elem
            elem = elem.n   
            
    def __getitem__(self, i):
        pos = 0
        for e in self:
            if pos == i:
                return e
            pos += 1
        raise IndexError 
        
    def __setitem__(self, i, a):     
        pos = 0
        for li in self.iterator_li():
            if pos == i:
                li.e = a
                return
            pos += 1
        raise IndexError 
        
    def __str__(self):
        elems = [str(e) for e in list(self)]
        # elems = map(str, list(elems))
        return '-[' + ', '.join(elems) + ']-'    
    
    """
    def __delitem__(self, i):
    	if len(self) == 0:
            raise IndexError
        if i==1:
        	if len(self) == 1:
        	self.first = None
        	self.last = None
		    else:
		    	self.first = self.first.n
        	
    	if i == len(self)-1:
    		self[i-1].n=None
    	if i != 0:
            self[i-1].n=self[i+1].n

        self.length -= 1
    """
    def __delitem__(self,i):
    	if len(self)==0:
    		raise IndexError
    	if i==0:
    		if len(self) ==1:
    			self.first=None
    			self.last=None
    		else:
    			self.first=self.first.n
    	if i==len(self)-1:
    		self[i]=None
    	elif i!=0:
    		self[i-1]=self[i]
    	self.length -=1    
    #+=    
    def __iadd__(self,other):
    	if(type(other)==int):
    		self.append(other)
    		return self
    	for e in other:
    		print(e)
    		self.append(e)
    	return self
    
    #+
    def __add__(self,other):
    	self.append(other)
    	return self	
    #mnozenie
    def __mul__(self,number):
    	new=LinkedList([])
    	for e in self:
    		for i in range (number):
    			e=e+e
    		new.append(e)
    			
    	return new
    	
    def __rmul__(self,number):
    	new=LinkedList([])
    	for e in self:
    		x=e
    		for i in range (number-1):
    			e=e+x
    		new.append(e)
    			
    	return new
 
    
    
    
    
    
    
    
    
    
                          
L = LinkedList([2,3,4,5,5,6,7])
L+='ala'
L+=3
L+=[1,2,3]
print(L)
print(L+12)
print(3*L)


