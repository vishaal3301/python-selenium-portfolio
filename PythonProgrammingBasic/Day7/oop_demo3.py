# Instance method and Static method.
#Instance method -> can be called by using an Object.
#Static Method -> can be called by using class name, and it is common method for every Object.
""" Static methods belong to class only, but a soon as we create an object,
static methods also belongs to object."""

class VariousMethods:
    def method1(self):
        print(f"Method1 is a instance method")

    @staticmethod
    def method2(text):
        print(f"Method2 is static method, Notice an Annotation on the top of method {text}")
    @staticmethod
    def method3(self,num):
        print(f"inside method3, which is also static method with self argument:{self} and num argument:{num}")

obj1 = VariousMethods()

obj1.method1()
obj1.method2("in Python")
"""As here for demo, we are calling static method using an object,
which do NOT make sense but for learning we are doing, Static methods must be invoked by using
Respective Class Name.
Also self keyword is static method is NOT mandatory, in Static method self keyword reference as an separate 
argument.
Where as self keyword in NON-Static method reference to respective class and self keyword is mandatory in 
NON-Static method."""
obj1.method3("Vishal",786)

VariousMethods.method2("method2()")
