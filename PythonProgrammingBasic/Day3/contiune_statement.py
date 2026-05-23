# continue statement

for i in range(0,11):
    if i == 5:
        continue
    print(i)
print("due to continue statement, when program execution is arrived at 5, 5 is skipped and next numbers from 5 onwards are also get printed")
print("*"*2000)

for j in range(1,11):
    if j==3 or j==5 or j==7:
        continue
    print(j)
print("3,5,7 are skipped")
print("*"*2000)


