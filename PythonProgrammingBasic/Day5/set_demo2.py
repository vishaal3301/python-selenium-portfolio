# Add element to the Set
# add() update()
# add() -> add single element at a time.
# update() -> it will insert multiple elements at a time.

# add()
mySet2 = {'apple','banana','cherry'}
print("Original mySet2: ",mySet2)
mySet2.add("orange")
print("after adding orange to mySet2: ",mySet2)

# update()
mySet3 = {'apple','banana','cherry'}
print("original mySet3: ",mySet3)
mySet3.update(["mango","grapes","kiwi"])
print("after update(), mySet3 : ",mySet3)

#Find Total Number of items in a Set
# len()

print("total number of items in mySet3:\t", len(mySet3))