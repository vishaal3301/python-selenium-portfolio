""" Set: a Set is a collection which is unordered amd unindexed.
In Python sets are written with curly brackets { }. """

#Creating the set
mySet1 =  {"apple","banana","cherry"}
print("mySet1: ",mySet1)
print("#"*1000)
#Accessing items from the Set, using loop
print("Original mySet1: ",mySet1)
print("print using for loop:")
for i in mySet1:
    print(i)


#Check Element is present in Set or not.
# in operator
print("banana" in mySet1) # It will print True or False
print("orange" in mySet1)