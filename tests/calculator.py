class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def get_sum(self):
        return self.a + self.b
    
    def get_product(self):
        return self.a * self.b
    
    def get_difference(self):
        return self.a - self.b
    
    def get_quotient(self):
        return self.a / self.b
    
if __name__ == "__main__":
    myCalc = Calculator(a = 5, b = 6)
    print(myCalc.get_sum())
    print(myCalc.get_product())
    print(myCalc.get_difference())
    print(myCalc.get_quotient())