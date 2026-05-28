# Reverse a str
s = input("Enter a Valid String:\t")
print(s)
rev_s = ""

for i in s:
    rev_s = i + rev_s
print("Reverse is: ", rev_s)
