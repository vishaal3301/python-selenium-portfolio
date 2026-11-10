# Multiple Inheritance

class Grandfather:
    grandfathername = ""
    def grandfather(self):
        print(self.grandfathername)
class Mother:
    mothername = ""

    def mother(self):
        print(self.mothername)  

class Father:
    fathername = ""

    def father(self):
        print(self.fathername)

class Child(Grandfather,Mother, Father):
    def __init__(self):
        self.mothername = "Alice"
        self.fathername = "Bob"
        self.grandfathername = "Charlie"

    def child(self):
        print(self.mothername)
        print(self.fathername)

obj = Child()
obj.grandfather()
obj.mother()
obj.father()
obj.child()

print(Child.mro())