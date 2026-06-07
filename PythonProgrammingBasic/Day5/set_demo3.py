"""Set is Mutable is, Hence we can Add,Remove,Update, Value inside Set"""
# Remove elements from the Set.
# remove(), discard()

# remove()
print("remove(): ")
mySet4 = {'apple','banana','cherry','orange','kiwi'}
print("Original mySet4:\t",mySet4)
mySet4.remove('cherry')
print("After removing cherry, mySet4:\t",mySet4)

print("*"*10000)

# If element is not present in set, and try to remove that element.
# as XYZ element is NOT present inside mySet4, try to remove XYZ, and observe the error.
print("Trying to remove XYZ, which is NOT present in mySet4, then it will give 'KeyError' ")
# mySet4.remove("XYZ") it will give, KeyError: 'XYZ'

print("*"*10000)
# discard()
print("discard(): ")
mySet5 = {"kiwi","grapes","Pear","peach","berry"}
print("Original list, myList5:\t ",mySet5)
mySet5.discard("kiwi")
print("After removing kiwi from mySet5:\t",mySet5)

print("*"*10000)
"""When we use discard() to remove an element which is NOT present inside Set,
        it will NOT give an error like remove() gives"""
print("discard() an element which is NOT in the Set")
mySet5.discard("XYZ")
print("After discard(XYZ), printing myList5:\t",mySet5)

print("*"*1000)
#Clear all elements from Set, clear().
print("cleaar(), will clear all Items from Set, but Set variable still present in memory ")
mySet6 = {1,2,3,"apple","banana","cucumber"}
print("Original mySet6:\t",mySet6)
mySet6.clear();
print("After clear(), mySet6, But the variable is available:\t",mySet6)

print("*"*1000)
# del keyword
print("del keyword will delete all element of Set with Set keyword, Set variab le will also deleted from memory")
mySet7 = {'a','b','c','d','e'}
print("Original mySet7:\t",mySet7)
del mySet7
print("After del(), mySet7 contents and mySet7 variable is also deleted")
# print(mySet7) will give NameError: name 'mySet7' is not defined.