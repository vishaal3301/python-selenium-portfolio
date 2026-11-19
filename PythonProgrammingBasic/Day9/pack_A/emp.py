class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display_info(self):
        print(f"Employee Name: {self.name}, Employee ID: {self.emp_id}")