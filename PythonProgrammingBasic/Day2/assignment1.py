#Check if givern number is positive or negative
user_num1 = int(input("Enter a number: "))

if user_num1>0:
     print(f"{user_num1} is a positive integer")
else:
     print(f"{user_num1} is  a negative integer")

print(f"{user_num1} is  a positive integer") if user_num1>0 else print(f"{user_num1} is  a negative integer")

