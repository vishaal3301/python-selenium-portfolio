# Add elements/items to the Tuple.
"""We can NOT add items to a Tuple as Tuple is Immutable
so,
1.We can NOT modify existing elemets inside a Tuple.
2. We can NOT append new elements inside a Tuple.
3. We can NOT insert new elements inside a Tuple.
4. We can NOT remove elements from Tuple.
But we can Convert Tuple into List, and then perform operation
and then again conver that List into Tuple."""

# Copy the Tuple to a another Tuple.
new_tuple2 = ('apple','banana','cherry')
print("new_tuple2: ",new_tuple2)
new_tuple3 = new_tuple2
print("new_tuple3 : ",new_tuple3)

# Delete Tuple
print("new_tuple3: ",new_tuple3)
del new_tuple3
print("new_tuple3 is deleted")