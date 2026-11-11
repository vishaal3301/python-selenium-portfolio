#Accessing Parent class attributes/variable

class A:
    a,b=100,200

class B(A):
    i,j=1,2
    def m(self,x,y):
        print(f"x:{x} + y:{y} = {x+y}") #local variable
        print(f"i:{self.i} + j:{self.j} = {self.i+self.j}") # Class variable
        print(f"a:{self.a} + b:{self.b} = {self.a+self.b}") # Parent class variable

obj_B = B()
obj_B.m(10,20)