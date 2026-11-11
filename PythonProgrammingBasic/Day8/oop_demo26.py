# Bank application

class Bank:
    def rate_of_intrest(self):
        return 0 

class SBI_Bank(Bank):
    def rate_of_interst(self):
        return 12

class Axis_Bank(Bank):
    def rate_of_interst(self):
        return 10



obj_SBI  = SBI_Bank()
print(obj_SBI.rate_of_interst())