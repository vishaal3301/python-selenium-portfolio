# Raising our own Exception
def enter_Age(num):
    if num<0:
        raise ValueError("Only Positive Integer are allowed")
    if num%2==0:
        print(f'Number is even')
    else:
        print(f'Number is Odd')


enter_Age(-1)