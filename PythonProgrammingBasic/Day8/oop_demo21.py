# Method Overriding

class A:
    def m1(self):
        print("Inside Class A")

class B:
    def m1(self):
        print("Inside Class B")


obj_B = B()
obj_B.m1()
