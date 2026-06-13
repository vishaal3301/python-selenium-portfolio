# Class Variables
class m2:
    a,b=10,20   # class variables

    def m2_print(self):
        print(f"{self.a,self.b}") #Class variables are access using self keyword.

    def m2_additon(self):
        print(f"a\t+\tb\t=\t{self.a+self.b}")
    def m2_multiply(self):
        print(f"a\t*\tb\t=\t{self.a*self.b}")

obj_m2 = m2()
obj_m2.m2_print()
obj_m2.m2_additon()
obj_m2.m2_multiply()