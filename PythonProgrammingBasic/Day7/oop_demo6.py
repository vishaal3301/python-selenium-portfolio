# Class with Global Variable
i,j = 15,25 # Global Variables
class ClassDemo6:
    a,b = 10,20 # Class Variables
    def classdemo6_print(self,x,y): # x,y are local variables
        print(f"x = {x}\ty = {y}") # As x and y are local variables we can direct access them.
        print(f"a = {self.a}\t b = {self.b}")
        """As a and b are class variables, we have to use
        Self keyword to Access them."""
        print(f"i = {i}\t j = {j}")
        """As i and j are global variables we can access them Directly"""

obj1_CD6 = ClassDemo6()
obj1_CD6.classdemo6_print(20,30)
