"""Requirement:
Create a class Emp in that create a constructor with three arguments
eid,ename, and create a method display(): print eid,ename and sal."""

class ClassDemo11:

    def __init__(self,emp_id,emp_name,emp_sal):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_sal = emp_sal

    def display(self):
        print(f"employee ID : {self.emp_id}\n employee name: {self.emp_name}\n employee salary:{self.emp_sal}")


CD_11 = ClassDemo11(786,"Vishaal",7860000)
CD_11.display()

