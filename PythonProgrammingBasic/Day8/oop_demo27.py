# Method Overloading
# Polymorphism

class A:
    def add(self, a, b, c=0):
        return a + b + c
    
obj = A()
print(obj.add(2, 3))
print(obj.add(2, 3, 4))