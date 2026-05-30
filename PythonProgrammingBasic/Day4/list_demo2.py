#Accessing the items/elements from list

#Accessing single item/element from list
myList1 = [10,20,"vishal",30,'orange','banana',40]
#list items can be access by using index, and index starts from zero.
print("2nd item from list: ",myList1[2])
#List can be access by using negative index, last item in the list is at index -1
print("last item from list using negative index: ",myList1[-1])
print("2nd last item from list using negative index: ",myList1[-2])

#Accessing multiple items/elements at once from list.
myList2 = ['apple',1,'cherry','banana',2,'orange',3,'kiwi',3,4,"melon",5,6,'mango']
print("starting index and ending index[excluded]",myList2[2:5])

#passing negative index to a list,so it will count list from the last element
print("negative index, counting from last",myList2[-10:-1])
