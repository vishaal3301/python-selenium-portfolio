#Changing tuple elements
""" As Tuple is Immutable
1. We can NOT modify existing value.
2. We can NOT append new value.
3. We can NOT insert a new value.
4. We can NOT remove an exsiting value. """

#By default, tuple does NOT allow to change values because Tuple is Immutable.
# But we have an Indirect way to change the values/elements inside the Tuple.
#Tuple --> List{Modify this List} --> Tuple

myTuple1 = ('apple','banana','cherry')
print("myTuple1: ",myTuple1)
#covert this myTuple1 into myList1.
myList1 = list(myTuple1)
print("Element inside myList1, these are same as elements in myTuple1: ",myList1)

