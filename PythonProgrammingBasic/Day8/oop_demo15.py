#Single Inheritance
#one parent and one child

class A:
    def m1(self):
        print(f"Inside Class A: def m1")


class B(A):
    def m2(self):
        print(f"Inside Class B: def m2")

obj_B= B()

obj_B.m1()
obj_B.m2()