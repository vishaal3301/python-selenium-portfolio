#copy list
my_list = ['apple','banana','orange','kiwi']
print("original list: ",my_list)

#copy elements of my_list into my_list_copy
my_list_copy = list() #just to show we have created a new empty list
print("new empty my_list_copy: ",my_list_copy)
my_list_copy = list(my_list) # copied the element from my_list
print("after elements are copied form my_list into my_list_copy: ",my_list_copy)

#copy list using copy()
myListCopy = my_list.copy()
print("myListCopy has copied element from my_list using copy(): ",myListCopy)