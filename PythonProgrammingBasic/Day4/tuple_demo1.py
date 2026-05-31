# Tuple:
"""A Tuple is a collection which is ordered and unchangeable.
In Python tuples are written with round ( ) brackets.
Tuple is Immutable. """

myTuple = ("apple","orange","banana",1,2,3,0.25)
print("Elements from Tuple, myTuple: ",myTuple)

#Creating empty tuple
my_tuple = ()

#Access individual elements from tuple, using index and Tuple index starts from zero.
print("Zero element from myTuple: ",myTuple[0])

#Access individual elements from Tuple using Negative index, -1 means last element inside a tuple.
print("last element in myTUple: ",myTuple[-1])

#Range of Indexes.
print("Original Tuple, myTuple: ",myTuple)
print("printing elements from myTuple, from index 2 to 5[excluded]: ",myTuple[2:5])

#Range of Index with negative Indexes
print("Original Tuple, myTuple: ",myTuple)
print("Printing element, myTuple[-4:-1]: ",myTuple[-4:-1])
