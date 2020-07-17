class RList(list):
    def __init__(self):
        super().__init__()
        
    def __getitem__(self, i):
        if i >= len(self):
            return None
        return super().__getitem__(i)
    
    def __setitem__(self, i, a):
        if i >= len(self):
            self += (i - len(self) + 1) * [None]
        super().__setitem__(i, a)
        
L = RList()
L += [0,1,2]
L[10] = 999
print (L)                    
