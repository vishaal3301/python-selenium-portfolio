# Overriding Variables

class Parent:
    name = "Amit"

class Child(Parent):
    name = "Vishal" # Variable Override

obj_Child = Child()
print(obj_Child.name)