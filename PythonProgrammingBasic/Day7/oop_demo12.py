"""Parameterised Constructor with printing constructor """

class ClassDemo12:
    def __init__(self,emp_id,emp_name,emp_sal):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_sal = emp_sal

    def __str__(self): # str representation method.
        return self.emp_name


CD_12 = ClassDemo12(786,"Vishaal Khairnar",786000)
print(CD_12)