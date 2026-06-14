"""Constructor"""

"""Method -> 1.Method can have any name.
             2. Method return the values.
            3. Method can take any number of parameters/Arguments.
            4. Method can be invoked by Object.
    
    Constructor -> 1.Name of Constructor always be fixed -> def __init__(self)
                    2. Constructor will NOT return value.
                     3. Constructor can also take arguments/parameters.
                     4. Constructor will be called at the time of Object Creation itself."""

class ClassDemo9:
    def __init__(self):
        print(f"This is Constructor...")
    def classdemo9_print(self):
        print(f"This is regular method")

obj1_cd9 = ClassDemo9() # This will Invoke Constructor Automatically.