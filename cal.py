class Calculator:
    def __init__(self,a):
        self.a = a
        
    def square(self):
        return self.a**2
    
a = Calculator(3)
print(a.square())