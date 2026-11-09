# multi-Level inheritance.
class A:
    x,y=10,20
    def m1(self):
        print(f"x:{self.x} + y:{self.y} = {self.x+self.y}")


class B(A):
    a,b=100,200
    def m2(self):
        print(f"a:{self.a} + b:{self.b} = {self.a+self.b}")

class C(B):
    i,j = 5,2
    def m3(self):
        print(f"i:{self.i} * j:{self.j} = {self.i*self.j}")


obj_C = C()
obj_C.m1()
obj_C.m2()
obj_C.m3()