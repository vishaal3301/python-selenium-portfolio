class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display_info(self):
        print(f"Student Name: {self.name}, Roll Number: {self.roll_no}")