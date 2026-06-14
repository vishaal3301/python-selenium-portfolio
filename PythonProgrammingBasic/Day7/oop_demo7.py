a,b=15,25 # Global Variables
class ClassDemo7:
    a,b=10,20 # Class Variables
    def classdemo7_print(self,a,b):
        print(f"Printing local variables ->\t a\t:\t{a} \tb\t:\t{b}")
        print(f"Printing Class variables ->\t a\t:\t{self.a} \tb\t:\t{self.b}")
        print(f"Printing Global Variables ->\t a\t:\t{globals()['a']}\tb\t:\t{globals()['b']}")

CD7 = ClassDemo7()
CD7.classdemo7_print(100,200)