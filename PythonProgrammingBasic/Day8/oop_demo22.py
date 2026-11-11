# Method Overridding
#Invoking Parent class method

class A:
    def m1(self):
        print(f"Inside Class A")

class B(A):
    def m1(self):
        print(f"Inside Class B")
        super().m1()

obj_B = B()
obj_B.m1()
