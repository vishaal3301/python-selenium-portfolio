"""Dictionary is a collection which is unorder, changeable(Mutable) and indexed.
In Python dictionaries are written with curly braces, and they have keys and values.
Dictionary is MUTABLE"""

# Create a dictionary
myDict1 = {101:'x',102:'y',103:'z'}
print("myDict:\t", myDict1)

myDict2 = {'a':1,'b':2,'c':3}
print("myDict2:\t",myDict2)

# Access the element, i.e. key and value.
myDict3 = {'brand':'BMW',
           'model': 'x9',
           'year':2029,
           'engine':'v12',
           'colour':'white'
           }
print("myDict['brand]:\t",myDict3['brand'])
print("myDict[model]:\t",myDict3['model'])

# get()
print("myDict.get('brand):\t",myDict3.get('brand'))


# Accessing the values using loop
print("accessing all key and values of myDict3 using for loop")
for i in myDict3.items():
    print(i)

print("accessing only all values from myDict3")
for i in myDict3:
    print(myDict3[i])

print("accessing myDict3 by using values()")
for i in myDict3.values():
    print(i)

print("Accessing key and values using for loop")
for x,y in myDict3.items():
    print(x,y)