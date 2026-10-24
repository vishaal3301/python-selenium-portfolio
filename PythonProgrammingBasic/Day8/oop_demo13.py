
class MyClass:
    name = "Vishaal"
    def __init__(self,name:str):
        print(f"Constructor is called with name: {name}")
        print(f"self.name: {self.name}")

obj1 = MyClass("Vishaal Khairnar")
# obj2 = MyClass(123)