#Copying dictionary.
myDict8 = {
    1:'vishal',
    2:'vicky',
    3:'amit',
    4:'yash',
    5:'umesh'
}
# Without using copy()
myDict9 = myDict8
print('myDict9:\t',myDict9)

# copy()
myDict10 = myDict9.copy()
print("myDict10:\t",myDict10)