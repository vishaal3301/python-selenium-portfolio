class ClassDemo10:
    name = "Vishaal" # Class variable
    def __init__(self,name): #constructor is expecting an argument.
        print(f"Class variable: {self.name}")
        print(f"Local variable:{name}")

ClassDemo10("James Bond") #Passing parameter to the Constructor.