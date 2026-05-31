#joining of two list

#Using concatenation (+) operator
# In python " " and ' ' both used for characters as well as for string.
list1 = ['a','b','c']
list2 = ['d','e','f']

list_join = list1 + list2
print("Joining of list1 and list2 in list_join: ",list_join)

#joining two list using looping statement
list3 = ["a","b","C"]
list4 = [1,2,3]

for i in list4:
    list3.append(i)

print("list3: ",list3)

#By using extend()
list5 = ['a','b','c','d']
list6 = [1,2,3,4]
list5.extend(list6)
print("list5 after extend(): ",list5)

