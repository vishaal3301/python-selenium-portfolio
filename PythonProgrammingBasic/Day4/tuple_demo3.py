#Using for loop to read elements/items from tupple

new_tuple1 = ("apple",'banana','orange','melon','kiwi',1,2,0.25,'v')
print("new_tuple1: ",new_tuple1)
print("using for loop to print new_tuple1 elements: ")
for i in new_tuple1:
    print(i)
print("All element/item are printed:")

#To check an item is present inside in tuple or not.

if 0.225 in new_tuple1:
    print("The element is present in new_tuple1")
else:
    print("The element is NOT present inside new_tuple1")

# To find total element/items present inside a tuple.
print("new_tuple1: ",new_tuple1)
print("Total elements inside new_tuple1 is: ",len(new_tuple1))

