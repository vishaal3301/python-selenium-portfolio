# Testing strings: True/Falses
s = 'welcome to python'
print("1 ->",'welcome to python, all num?', s.isalnum()) #False
print("is 123 all num? ->",'123'.isalnum()) #False
print("2 ->",'welcome'.isalpha()) #True
print("3 ->",'2026'.isdigit()) #True
print(" is reserved keyword? ->","first Number".isidentifier()) #False
print("5 ->",s.islower()) #True
print("6 ->","WELCOME".isupper()) #True
print("  ->"," ".isspace()) #True
