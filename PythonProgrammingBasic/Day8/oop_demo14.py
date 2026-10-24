class EMP:
    def __init__(self,eid: int ,name:str, age:int, salary:int):
        self.name = name
        self.age = age
        self.eid = eid
        self.salary = salary

    def __str__(self):
        return f"eid:{self.eid}\t name:{self.name} \t salary:{self.salary}\t age:{self.age}"



obj1 = EMP(786,"Vishaal",36,38000)
print(obj1)

obj2 = EMP(3301,"Vishal",35,40000)
print(obj2)

