
print("Check the largest of three numbers")

user_num1 = int(input("Enter first number: "))
user_num2 = int(input("Enter second number: "))
user_num3 = int(input("Enter third number: "))

if user_num1 > user_num2 and user_num1 > user_num3:
    print(f"{user_num1} is greatest")
elif user_num2 > user_num1 and user_num2 > user_num3:
    print(f"{user_num2} is greatest")
else:
    print(f"{user_num3} is greatest")

