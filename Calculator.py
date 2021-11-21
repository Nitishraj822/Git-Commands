class Calculator():
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a - self.b
    
    def multi(self):
        return self.a*self.b
    
a=Calculator(34,35)
print(a.add())
print(a.sub())