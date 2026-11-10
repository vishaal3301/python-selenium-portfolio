# Multiple Inheritance
class Mother:
    mothername = ""

    def mother(self):
        print(self.mothername)  

class Father:
    fathername = ""

    def father(self):
        print(self.fathername)

class Child(Mother, Father):
    def __init__(self):
        self.mothername = "Alice"
        self.fathername = "Bob"

    def child(self):
        print(self.mothername)
        print(self.fathername)

obj = Child()
obj.mother()
obj.father()
obj.child()

print(Child.mro())