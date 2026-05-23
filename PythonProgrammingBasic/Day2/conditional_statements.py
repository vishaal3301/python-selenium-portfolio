"""There are 3 conditoinal statements in Python.
1. if statement
2. if...else statement
3. elif statement"""

#Print if a person is eligible for vote or not

age = float(input("Enter your age: "))
if age >= 18:
    print("you are eligible for Vote: ", age)
else:
    print("you are NOT eligible for Vote: ", age)

print("#"*2000)

if True:
    print("True")
else:
    print("False")

print("#"*2000)
if 1:
    print("1")
else:
    print("0")
print("#"*2000)

if 0:
    print("1")
else:
    print("0")

print("#"*2000)
print("Find a number is even or odd")

user_number = float(input("Enter any number:"))
if(user_number % 2 == 0):
    print("even",user_number)
else:
    print("odd",user_number)

print("#"*2000)
print("ternary Operator")

user_num1 = float(input("Enter any number:"))
print("Even number") if user_num1 % 2 == 0 else print("Odd number")
{print("Even"),print("Number")} if user_num1 % 2 == 0 else {print("Odd"),print("Number")}

print("#"*2000)

