#Single inheritance with parametrized methods

class A:
    x,y = 10,20
    def m1(self):
        print(f"x = {self.x} and y =  {self.y}")


class B(A):
    u,v = 100,200
    def m2(self):
        print(f"u+v = {self.u+self.v}")


obj_B = B()

obj_B.m1()
obj_B.m2()