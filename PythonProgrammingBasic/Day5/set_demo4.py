# Joining of two Set. union()
mySet8 = {'Vishal'}
mySet9 = {'Khairnar'}

# union()
mySet8 = mySet8.union(mySet9)
print("mySet8.union(mySet9) :\t",mySet8)

#union()
mySet9 = mySet9.union(mySet8)
print("mySet9 = mySet9.union(mySet8):\t",mySet9)

#union() self join
mySet10 = {1,2}
mySet11 = mySet10.union(mySet10)
print("mySet10.union(mySet10):\t",mySet11)

#update()
mySet12 = {'a','b','c'}
mySet13 = {1,2,3}

mySet12.update(mySet13)
print("mySet12.update(mySet13):\t",mySet12)