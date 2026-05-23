num1 = input("Please enter a number: ")
print(f"number entered is {num1}")
num2 = input("Please enter a number: ")
print(f"number entered is {num2}")

print(type(num2))
print(type(num1))

"""When user input a data in python in RUN time, then it is always str type of data"""

print(num1+num2) #output is num1num2, this is concatenation.
print(int(num1) + int(num2)) #ouput is num1 + num2

"""Now covert str in python to int"""
first_number = int(input("Please enter a number: "))
second_number = int(input("Please enter a number: "))

print(type(first_number))
print(type(second_number))

print(f"{first_number} + {second_number} = {first_number + second_number}")

print("#"*1000)

first_float = float(input("Please enter a number: "))
second_float = float(input("Please enter a number: "))
print(type(first_float))
print(type(second_float))
print(f"{first_float} + {second_float} = {first_float + second_float}")