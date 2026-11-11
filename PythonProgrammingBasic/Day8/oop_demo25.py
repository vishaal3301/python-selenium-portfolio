# Acessing parent class variable

class A:
    name = "Vishal"

class B(A):
    name = "Vickey"
    def m(self):
        print(super().name)


obj_B = B()
obj_B.m()