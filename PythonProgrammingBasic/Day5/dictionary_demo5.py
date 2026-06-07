# Adding items to dictionary.

myDict7 = {
    'brand':'Ferrari',
    'model':'La Ferrari',
    'year': 2032,
    'engine':'v12',
    'color':'red'
}

myDict7['owner'] = 'Vishal Khairnar'

print("New item added is owner in myDict7:\t",myDict7)

# Remove the item from dictionary using pop().
myDict7.pop('engine')
print("key: engine is removed:\t",myDict7)

# Remove item from dictionary using del keyword.
del myDict7['color']
print("key: color is removed:\t",myDict7)

# Remove all items of dictionary at once clear().
myDict7.clear()
print("All items are deleted,but myDict7 variable is present:\t",myDict7)

# Delete complete Dictionary suing del key word.
del myDict7
print('myDict7 is deleted successfully with myDict7 variable, using del keyword')